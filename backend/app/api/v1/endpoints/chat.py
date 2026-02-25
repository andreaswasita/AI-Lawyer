"""
AI Chat Endpoint - The Core AI Legal Assistant
Handles user legal questions in Bahasa Indonesia using Azure OpenAI + RAG
"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.query_log import QueryLog

router = APIRouter()


# ── Models ──────────────────────────────────────────────────────────────────

class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class ChatMessage(BaseModel):
    role: MessageRole
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ChatRequest(BaseModel):
    """User sends a legal question"""
    message: str = Field(..., min_length=1, max_length=4000, description="User's legal question in Bahasa Indonesia or English")
    conversation_id: Optional[str] = Field(None, description="Existing conversation ID for context")
    language: str = Field("id", description="Language code: 'id' for Bahasa Indonesia, 'en' for English")

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Bagaimana cara mengurus perceraian di Indonesia?",
                "language": "id",
            }
        }


class TriageResult(BaseModel):
    """AI determines if user needs self-service or lawyer"""
    category: str = Field(..., description="Legal category (divorce, business, employment, etc.)")
    complexity: str = Field(..., description="simple, moderate, complex")
    recommendation: str = Field(..., description="self_service, template, or lawyer_consultation")
    confidence: float = Field(..., ge=0, le=1, description="AI confidence score")


class LegalSource(BaseModel):
    """Reference to Indonesian law used in the response"""
    law_name: str = Field(..., description="Name of the law (e.g., 'UU No. 1 Tahun 1974')")
    article: Optional[str] = Field(None, description="Specific article reference")
    description: str = Field(..., description="Brief description of the legal reference")
    url: Optional[str] = Field(None, description="Link to official source")


class ChatResponse(BaseModel):
    """AI response with legal information"""
    conversation_id: str
    message: str = Field(..., description="AI response in user's language")
    triage: TriageResult
    sources: list[LegalSource] = Field(default_factory=list, description="Legal references cited")
    suggested_templates: list[str] = Field(default_factory=list, description="Relevant document templates")
    suggested_actions: list[str] = Field(default_factory=list, description="Recommended next steps")
    disclaimer: str = Field(
        default="⚠️ Informasi ini bersifat umum dan bukan merupakan nasihat hukum. "
                "Untuk nasihat hukum resmi, silakan konsultasi dengan Advokat berlisensi.",
        description="Legal disclaimer"
    )


# ── System Prompt ───────────────────────────────────────────────────────────

SYSTEM_PROMPT_ID = """Kamu adalah AI Lawyer (Hukum AI), asisten hukum AI untuk warga Indonesia.

PERAN:
- Memberikan informasi hukum umum dalam Bahasa Indonesia yang mudah dipahami
- Membantu pengguna memahami hak dan kewajiban hukum mereka
- Mengarahkan pengguna ke template dokumen yang sesuai
- Merekomendasikan konsultasi dengan Advokat untuk kasus yang kompleks

ATURAN PENTING:
1. JANGAN PERNAH memberikan nasihat hukum spesifik untuk kasus individual
2. Selalu sertakan disclaimer bahwa ini adalah informasi umum
3. Selalu rujuk ke undang-undang dan peraturan yang relevan
4. Jika kasus kompleks, rekomendasikan konsultasi dengan Advokat
5. Gunakan Bahasa Indonesia yang sederhana dan mudah dipahami
6. Berikan langkah-langkah praktis yang bisa dilakukan pengguna

BIDANG KEAHLIAN:
- Perceraian (UU 1/1974, KHI, PP 9/1975)
- Pendirian Usaha (UU 40/2007, UU 11/2020 Cipta Kerja, OSS RBA)
- Ketenagakerjaan (UU 13/2003, PP 35/2021, UU 6/2023)
- Waris & Wasiat (KUH Perdata, KHI, Hukum Adat)
- Perlindungan Konsumen (UU 8/1999)
- Kekayaan Intelektual (UU 28/2014, UU 20/2016)
- Pertanahan (UU 5/1960 UUPA)
- Perjanjian & Kontrak (KUH Perdata Buku III)

FORMAT RESPONS:
- Mulai dengan ringkasan singkat
- Jelaskan dasar hukumnya
- Berikan langkah-langkah praktis
- Sarankan template atau layanan yang relevan
- Akhiri dengan disclaimer
"""

SYSTEM_PROMPT_EN = """You are AI Lawyer (Hukum AI), an AI legal assistant for Indonesian citizens.

ROLE:
- Provide general legal information about Indonesian law in simple language
- Help users understand their legal rights and obligations
- Direct users to relevant document templates
- Recommend lawyer consultation for complex cases

IMPORTANT RULES:
1. NEVER provide specific legal advice for individual cases
2. Always include a disclaimer that this is general information
3. Always reference relevant Indonesian laws and regulations
4. If the case is complex, recommend consultation with a licensed Advocate (Advokat)
5. Use simple, easy-to-understand language
6. Provide practical steps the user can take

EXPERTISE AREAS:
- Divorce (UU 1/1974, KHI, PP 9/1975)
- Business Formation (UU 40/2007, UU 11/2020 Cipta Kerja, OSS RBA)
- Employment (UU 13/2003, PP 35/2021, UU 6/2023)
- Inheritance & Wills (KUH Perdata, KHI, Adat Law)
- Consumer Protection (UU 8/1999)
- Intellectual Property (UU 28/2014, UU 20/2016)
- Land/Property (UU 5/1960 UUPA)
- Contracts & Agreements (KUH Perdata Book III)

RESPONSE FORMAT:
- Start with a brief summary
- Explain the legal basis
- Provide practical steps
- Suggest relevant templates or services
- End with disclaimer
"""


# ── Triage Logic ────────────────────────────────────────────────────────────

CATEGORY_KEYWORDS = {
    "perceraian": ["cerai", "divorce", "talak", "gugat cerai", "pisah", "perceraian", "perkawinan", "nikah"],
    "bisnis": ["usaha", "bisnis", "pt", "cv", "perusahaan", "business", "company", "nib", "siup", "oss"],
    "ketenagakerjaan": ["kerja", "phk", "resign", "gaji", "upah", "employment", "kontrak kerja", "pkwt", "pekerja"],
    "waris": ["waris", "warisan", "inheritance", "harta", "pusaka", "ahli waris"],
    "wasiat": ["wasiat", "testament", "will", "hibah"],
    "properti": ["tanah", "property", "rumah", "sertifikat", "shm", "hgb", "land"],
    "konsumen": ["konsumen", "consumer", "pengembalian", "garansi", "refund", "complain"],
    "kontrak": ["kontrak", "perjanjian", "agreement", "contract", "nda", "mou"],
    "kekayaan_intelektual": ["merek", "trademark", "hak cipta", "copyright", "paten", "patent"],
}


def triage_question(message: str) -> TriageResult:
    """
    Analyze the user's question to determine category and complexity.
    In production, this would use AI classification.
    """
    message_lower = message.lower()
    
    # Detect category
    detected_category = "umum"  # default: general
    max_matches = 0
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        matches = sum(1 for keyword in keywords if keyword in message_lower)
        if matches > max_matches:
            max_matches = matches
            detected_category = category
    
    # Determine complexity based on heuristics
    complex_indicators = ["pengadilan", "court", "gugatan", "lawsuit", "somasi", "sengketa", "dispute", "pidana", "criminal"]
    moderate_indicators = ["dokumen", "template", "cara", "how", "prosedur", "procedure", "syarat", "requirement"]
    
    complexity = "simple"
    if any(word in message_lower for word in complex_indicators):
        complexity = "complex"
    elif any(word in message_lower for word in moderate_indicators):
        complexity = "moderate"
    
    # Determine recommendation
    recommendation = "self_service"
    confidence = 0.7
    
    if complexity == "complex":
        recommendation = "lawyer_consultation"
        confidence = 0.85
    elif complexity == "moderate":
        recommendation = "template"
        confidence = 0.75
    
    return TriageResult(
        category=detected_category,
        complexity=complexity,
        recommendation=recommendation,
        confidence=confidence,
    )


# ── Template Suggestions ───────────────────────────────────────────────────

CATEGORY_TEMPLATES = {
    "perceraian": ["Surat Gugatan Cerai", "Surat Permohonan Cerai Talak", "Surat Kuasa Perceraian"],
    "bisnis": ["Akta Pendirian PT", "Akta Pendirian CV", "Surat Izin Usaha", "Anggaran Dasar PT"],
    "ketenagakerjaan": ["Kontrak Kerja PKWT", "Surat Pengunduran Diri", "Surat Peringatan Karyawan", "PKB"],
    "waris": ["Surat Keterangan Waris", "Akta Pembagian Harta Waris", "Surat Pernyataan Ahli Waris"],
    "wasiat": ["Surat Wasiat", "Akta Hibah", "Wasiat Umum"],
    "kontrak": ["Perjanjian Kerjasama", "NDA", "MOU", "Perjanjian Sewa Menyewa"],
    "properti": ["Perjanjian Jual Beli Tanah", "Surat Kuasa Jual", "Akta Jual Beli"],
    "konsumen": ["Surat Pengaduan Konsumen", "Surat Somasi", "Surat Klaim Garansi"],
    "kekayaan_intelektual": ["Permohonan Merek", "Perjanjian Lisensi", "Perjanjian Pengalihan Hak Cipta"],
}


# ── Endpoints ──────────────────────────────────────────────────────────────

@router.post("/", response_model=ChatResponse)
async def send_message(request: ChatRequest, db: AsyncSession = Depends(get_db)):
    """
    Send a legal question to the AI assistant.
    
    The AI will:
    1. Analyze your question (triage)
    2. Search Indonesian legal knowledge base (RAG)
    3. Generate a helpful response in your language
    4. Suggest relevant templates and next steps
    """
    # Generate or use existing conversation ID
    conversation_id = request.conversation_id or str(uuid.uuid4())
    
    # Triage the question
    triage = triage_question(request.message)
    
    # Get suggested templates based on category
    suggested_templates = CATEGORY_TEMPLATES.get(triage.category, [])
    
    # For MVP demo, generate a structured response
    response_message = _generate_demo_response(request.message, triage, request.language)
    
    # Build legal sources
    sources = _get_demo_sources(triage.category)
    
    # Build suggested actions
    actions = _get_suggested_actions(triage, request.language)
    
    # Set disclaimer based on language
    disclaimer = (
        "⚠️ Informasi ini bersifat umum dan bukan merupakan nasihat hukum. "
        "Untuk nasihat hukum resmi, silakan konsultasi dengan Advokat berlisensi."
        if request.language == "id"
        else "⚠️ This is general information, not legal advice. "
             "For official legal advice, please consult with a licensed Advocate (Advokat)."
    )

    # Log the query for later review and analysis
    log_entry = QueryLog(
        conversation_id=conversation_id,
        message=request.message,
        language=request.language,
        category=triage.category,
        complexity=triage.complexity,
        recommendation=triage.recommendation,
        confidence=triage.confidence,
        response_preview=response_message[:500],
    )
    db.add(log_entry)
    
    return ChatResponse(
        conversation_id=conversation_id,
        message=response_message,
        triage=triage,
        sources=sources,
        suggested_templates=suggested_templates[:3],
        suggested_actions=actions,
        disclaimer=disclaimer,
    )


@router.get("/categories")
async def get_categories():
    """Get all available legal categories"""
    categories = {
        "perceraian": {"name_id": "Perceraian", "name_en": "Divorce", "icon": "💔"},
        "bisnis": {"name_id": "Bisnis & Perusahaan", "name_en": "Business & Company", "icon": "🏢"},
        "ketenagakerjaan": {"name_id": "Ketenagakerjaan", "name_en": "Employment", "icon": "👷"},
        "waris": {"name_id": "Waris", "name_en": "Inheritance", "icon": "📜"},
        "wasiat": {"name_id": "Wasiat & Hibah", "name_en": "Wills & Grants", "icon": "✍️"},
        "kontrak": {"name_id": "Kontrak & Perjanjian", "name_en": "Contracts & Agreements", "icon": "📋"},
        "properti": {"name_id": "Properti & Pertanahan", "name_en": "Property & Land", "icon": "🏠"},
        "konsumen": {"name_id": "Perlindungan Konsumen", "name_en": "Consumer Protection", "icon": "🛡️"},
        "kekayaan_intelektual": {"name_id": "Kekayaan Intelektual", "name_en": "Intellectual Property", "icon": "💡"},
    }
    return {"categories": categories}


# ── Helper Functions (Demo) ────────────────────────────────────────────────

def _generate_demo_response(message: str, triage: TriageResult, language: str) -> str:
    """Generate a demo response. In production, this uses Azure OpenAI."""
    
    if language == "id":
        return (
            f"Terima kasih atas pertanyaan Anda tentang **{triage.category}**.\n\n"
            f"Berdasarkan analisis AI kami, pertanyaan Anda termasuk kategori "
            f"**{triage.complexity}** dengan tingkat keyakinan {triage.confidence:.0%}.\n\n"
            f"**Rekomendasi:** {_get_recommendation_text_id(triage.recommendation)}\n\n"
            f"---\n\n"
            f"🤖 *Catatan: Ini adalah respons demo. Setelah integrasi penuh dengan Azure OpenAI, "
            f"AI Lawyer akan memberikan jawaban detail berdasarkan hukum Indonesia yang relevan, "
            f"lengkap dengan rujukan pasal dan langkah-langkah praktis.*"
        )
    else:
        return (
            f"Thank you for your question about **{triage.category}**.\n\n"
            f"Based on our AI analysis, your question falls under the "
            f"**{triage.complexity}** category with {triage.confidence:.0%} confidence.\n\n"
            f"**Recommendation:** {_get_recommendation_text_en(triage.recommendation)}\n\n"
            f"---\n\n"
            f"🤖 *Note: This is a demo response. After full Azure OpenAI integration, "
            f"AI Lawyer will provide detailed answers based on relevant Indonesian law, "
            f"complete with article references and practical steps.*"
        )


def _get_recommendation_text_id(recommendation: str) -> str:
    texts = {
        "self_service": "Anda dapat menyelesaikan ini sendiri! Lihat template dan panduan yang kami sarankan di bawah.",
        "template": "Kami menyarankan menggunakan template dokumen kami. Klik template yang disarankan untuk memulai.",
        "lawyer_consultation": "Kasus ini cukup kompleks. Kami menyarankan konsultasi dengan Advokat mitra kami untuk hasil terbaik.",
    }
    return texts.get(recommendation, "Silakan lihat saran di bawah.")


def _get_recommendation_text_en(recommendation: str) -> str:
    texts = {
        "self_service": "You can handle this yourself! Check the suggested templates and guides below.",
        "template": "We recommend using our document templates. Click a suggested template to get started.",
        "lawyer_consultation": "This case is fairly complex. We recommend consulting with one of our partner Advocates for best results.",
    }
    return texts.get(recommendation, "Please see the suggestions below.")


def _get_demo_sources(category: str) -> list[LegalSource]:
    """Return demo legal sources based on category"""
    sources_map = {
        "perceraian": [
            LegalSource(
                law_name="UU No. 1 Tahun 1974 tentang Perkawinan",
                article="Pasal 38-41",
                description="Mengatur tentang putusnya perkawinan dan akibat hukumnya",
                url="https://peraturan.bpk.go.id/Details/47406/uu-no-1-tahun-1974",
            ),
            LegalSource(
                law_name="Kompilasi Hukum Islam (KHI)",
                article="Pasal 113-148",
                description="Mengatur perceraian bagi umat Islam di Indonesia",
            ),
        ],
        "bisnis": [
            LegalSource(
                law_name="UU No. 40 Tahun 2007 tentang Perseroan Terbatas",
                article="Pasal 7-14",
                description="Mengatur pendirian dan tata kelola Perseroan Terbatas (PT)",
                url="https://peraturan.bpk.go.id/Details/39965/uu-no-40-tahun-2007",
            ),
            LegalSource(
                law_name="UU No. 11 Tahun 2020 tentang Cipta Kerja",
                description="Omnibus law yang menyederhanakan perizinan berusaha melalui OSS RBA",
            ),
        ],
        "ketenagakerjaan": [
            LegalSource(
                law_name="UU No. 13 Tahun 2003 tentang Ketenagakerjaan",
                description="Undang-undang pokok ketenagakerjaan Indonesia",
                url="https://peraturan.bpk.go.id/Details/43013/uu-no-13-tahun-2003",
            ),
            LegalSource(
                law_name="PP No. 35 Tahun 2021",
                description="Mengatur PKWT, alih daya, waktu kerja, PHK, dan pesangon",
            ),
        ],
    }
    return sources_map.get(category, [])


def _get_suggested_actions(triage: TriageResult, language: str) -> list[str]:
    """Get suggested next actions based on triage result"""
    if language == "id":
        actions = {
            "self_service": [
                "📖 Baca panduan lengkap di Perpustakaan Hukum kami",
                "📝 Gunakan template dokumen yang disarankan",
                "❓ Ajukan pertanyaan lanjutan jika masih bingung",
            ],
            "template": [
                "📝 Pilih dan isi template dokumen yang sesuai",
                "👁️ Review dokumen yang dihasilkan",
                "📞 Konsultasi dengan Advokat jika perlu review profesional",
            ],
            "lawyer_consultation": [
                "👨‍⚖️ Jadwalkan konsultasi dengan Advokat mitra kami",
                "📋 Siapkan dokumen-dokumen pendukung",
                "💬 Gunakan AI chat untuk persiapan sebelum konsultasi",
            ],
        }
    else:
        actions = {
            "self_service": [
                "📖 Read the full guide in our Legal Library",
                "📝 Use the suggested document template",
                "❓ Ask follow-up questions if still unclear",
            ],
            "template": [
                "📝 Select and fill in the appropriate document template",
                "👁️ Review the generated document",
                "📞 Consult with an Advocate if you need professional review",
            ],
            "lawyer_consultation": [
                "👨‍⚖️ Schedule a consultation with our partner Advocates",
                "📋 Prepare supporting documents",
                "💬 Use AI chat to prepare before your consultation",
            ],
        }
    
    return actions.get(triage.recommendation, [])
