"""
Document Generation Endpoint
Handles AI-powered legal document creation for Indonesian users
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum
import uuid

router = APIRouter()


class DocumentFormat(str, Enum):
    DOCX = "docx"
    PDF = "pdf"


class DocumentStatus(str, Enum):
    DRAFT = "draft"
    GENERATED = "generated"
    REVIEWED = "reviewed"
    FINALIZED = "finalized"


class DocumentField(BaseModel):
    """A field that needs to be filled in the document"""
    name: str
    label_id: str  # Indonesian label
    label_en: str  # English label
    field_type: str  # text, date, number, select, textarea
    required: bool = True
    placeholder: Optional[str] = None
    options: Optional[list[str]] = None  # For select fields


class DocumentRequest(BaseModel):
    """Request to generate a legal document"""
    template_id: str = Field(..., description="Template identifier")
    fields: dict = Field(..., description="Filled-in template fields")
    language: str = Field("id", description="Output language")
    format: DocumentFormat = Field(DocumentFormat.DOCX, description="Output format")

    class Config:
        json_schema_extra = {
            "example": {
                "template_id": "surat-gugatan-cerai",
                "fields": {
                    "nama_penggugat": "Siti Nurhaliza",
                    "nama_tergugat": "Ahmad Dahlan",
                    "alamat_penggugat": "Jl. Sudirman No. 100, Jakarta Selatan",
                    "alamat_tergugat": "Jl. Gatot Subroto No. 50, Jakarta Selatan",
                    "alasan_cerai": "Tidak ada keharmonisan dalam rumah tangga",
                    "tanggal_nikah": "2020-01-15",
                    "jumlah_anak": 1,
                },
                "format": "docx",
            }
        }


class DocumentResponse(BaseModel):
    """Generated document response"""
    document_id: str
    template_id: str
    status: DocumentStatus
    title: str
    preview_text: str = Field(..., description="First 500 chars of the document")
    download_url: Optional[str] = None
    created_at: datetime
    fields_used: dict


@router.post("/generate", response_model=DocumentResponse)
async def generate_document(request: DocumentRequest):
    """
    Generate a legal document from a template.
    
    The AI will:
    1. Load the appropriate template
    2. Fill in the provided fields
    3. Generate contextually appropriate legal language
    4. Return a preview and download link
    """
    document_id = str(uuid.uuid4())
    
    # TODO: In production:
    # 1. Validate template exists and user has access
    # 2. Validate all required fields are provided
    # 3. Use Jinja2 + python-docx to generate document
    # 4. Optionally use AI to enhance/customize language
    # 5. Store document and generate download URL
    
    preview = _generate_preview(request.template_id, request.fields)
    
    return DocumentResponse(
        document_id=document_id,
        template_id=request.template_id,
        status=DocumentStatus.GENERATED,
        title=_get_template_title(request.template_id),
        preview_text=preview,
        download_url=None,  # TODO: Generate actual file and return URL
        created_at=datetime.utcnow(),
        fields_used=request.fields,
    )


@router.get("/{document_id}")
async def get_document(document_id: str):
    """Get a previously generated document"""
    # TODO: Retrieve from database
    raise HTTPException(status_code=404, detail="Document not found")


@router.get("/")
async def list_documents(skip: int = 0, limit: int = 20):
    """List user's generated documents"""
    # TODO: Query database for user's documents
    return {
        "documents": [],
        "total": 0,
        "skip": skip,
        "limit": limit,
    }


def _get_template_title(template_id: str) -> str:
    titles = {
        "surat-gugatan-cerai": "Surat Gugatan Cerai",
        "surat-permohonan-cerai-talak": "Surat Permohonan Cerai Talak",
        "kontrak-kerja-pkwt": "Kontrak Kerja PKWT",
        "perjanjian-kerjasama": "Perjanjian Kerjasama",
        "surat-pengunduran-diri": "Surat Pengunduran Diri",
        "akta-pendirian-pt": "Akta Pendirian PT",
        "nda": "Non-Disclosure Agreement (NDA)",
        "surat-somasi": "Surat Somasi",
    }
    return titles.get(template_id, template_id.replace("-", " ").title())


def _generate_preview(template_id: str, fields: dict) -> str:
    """Generate a text preview of the document"""
    nama = fields.get("nama_penggugat", fields.get("nama_pihak_pertama", "[Nama]"))
    
    previews = {
        "surat-gugatan-cerai": (
            f"SURAT GUGATAN CERAI\n\n"
            f"Kepada Yth.\nKetua Pengadilan Agama Jakarta Selatan\n"
            f"di Jakarta\n\n"
            f"Dengan hormat,\n\n"
            f"Yang bertanda tangan di bawah ini:\n"
            f"Nama: {fields.get('nama_penggugat', '[Nama Penggugat]')}\n"
            f"Alamat: {fields.get('alamat_penggugat', '[Alamat]')}\n\n"
            f"Selanjutnya disebut sebagai PENGGUGAT;\n\n"
            f"Dengan ini mengajukan gugatan cerai terhadap:\n"
            f"Nama: {fields.get('nama_tergugat', '[Nama Tergugat]')}\n"
            f"..."
        ),
    }
    
    return previews.get(
        template_id,
        f"[Preview untuk template '{template_id}' akan tersedia setelah integrasi penuh]"
    )
