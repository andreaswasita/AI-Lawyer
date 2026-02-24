"""
Lawyer Network Endpoint
Browse and connect with licensed Indonesian lawyers (Advokat)
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

router = APIRouter()


class LawyerSpecialty(str, Enum):
    PERCERAIAN = "perceraian"
    BISNIS = "bisnis"
    KETENAGAKERJAAN = "ketenagakerjaan"
    WARIS = "waris"
    PROPERTI = "properti"
    PIDANA = "pidana"
    KONSUMEN = "konsumen"
    KEKAYAAN_INTELEKTUAL = "kekayaan_intelektual"
    IMIGRASI = "imigrasi"


class ConsultationType(str, Enum):
    CHAT = "chat"
    PHONE = "phone"
    VIDEO = "video"
    IN_PERSON = "in_person"


class LawyerProfile(BaseModel):
    """Partner lawyer profile"""
    id: str
    name: str
    license_number: str = Field(..., description="PERADI/KAI registration number")
    bar_association: str = Field(..., description="PERADI, KAI, or IKADIN")
    specialties: list[LawyerSpecialty]
    years_experience: int
    location: str
    languages: list[str]
    rating: float = Field(..., ge=0, le=5)
    reviews_count: int
    bio_id: str  # Indonesian bio
    bio_en: str  # English bio
    consultation_types: list[ConsultationType]
    pricing: dict  # {type: price_idr}
    available: bool = True
    photo_url: Optional[str] = None


class ConsultationRequest(BaseModel):
    """Request to book a consultation"""
    lawyer_id: str
    consultation_type: ConsultationType
    preferred_date: str = Field(..., description="Preferred date (YYYY-MM-DD)")
    preferred_time: str = Field(..., description="Preferred time (HH:MM)")
    topic: str = Field(..., description="Brief description of legal issue")
    language: str = Field("id", description="Preferred language for consultation")


class ConsultationResponse(BaseModel):
    """Consultation booking response"""
    booking_id: str
    lawyer_id: str
    lawyer_name: str
    consultation_type: ConsultationType
    scheduled_date: str
    scheduled_time: str
    price: int
    payment_url: Optional[str] = None
    status: str


# ── Demo Lawyer Database ──────────────────────────────────────────────────

DEMO_LAWYERS = [
    LawyerProfile(
        id="lawyer-001",
        name="Dr. Ratna Sari, S.H., M.H.",
        license_number="PERADI/2015/12345",
        bar_association="PERADI",
        specialties=[LawyerSpecialty.PERCERAIAN, LawyerSpecialty.WARIS],
        years_experience=15,
        location="Jakarta Selatan",
        languages=["Bahasa Indonesia", "English"],
        rating=4.8,
        reviews_count=128,
        bio_id="Advokat berpengalaman 15 tahun khusus bidang hukum keluarga, perceraian, dan waris. Alumni Universitas Indonesia.",
        bio_en="Experienced advocate specializing in family law, divorce, and inheritance for 15 years. University of Indonesia alumni.",
        consultation_types=[ConsultationType.CHAT, ConsultationType.PHONE, ConsultationType.VIDEO, ConsultationType.IN_PERSON],
        pricing={"chat": 99000, "phone": 250000, "video": 300000, "in_person": 1500000},
        available=True,
    ),
    LawyerProfile(
        id="lawyer-002",
        name="Hendra Wijaya, S.H., LL.M.",
        license_number="PERADI/2012/67890",
        bar_association="PERADI",
        specialties=[LawyerSpecialty.BISNIS, LawyerSpecialty.KEKAYAAN_INTELEKTUAL],
        years_experience=18,
        location="Jakarta Pusat",
        languages=["Bahasa Indonesia", "English", "Mandarin"],
        rating=4.9,
        reviews_count=95,
        bio_id="Spesialis hukum bisnis dan kekayaan intelektual. Telah menangani 500+ kasus pendirian perusahaan dan merek dagang.",
        bio_en="Business law and intellectual property specialist. Handled 500+ company formation and trademark cases.",
        consultation_types=[ConsultationType.CHAT, ConsultationType.PHONE, ConsultationType.VIDEO],
        pricing={"chat": 149000, "phone": 350000, "video": 400000},
        available=True,
    ),
    LawyerProfile(
        id="lawyer-003",
        name="Farah Diba, S.H., M.Kn.",
        license_number="KAI/2018/11223",
        bar_association="KAI",
        specialties=[LawyerSpecialty.KETENAGAKERJAAN, LawyerSpecialty.KONSUMEN],
        years_experience=8,
        location="Surabaya",
        languages=["Bahasa Indonesia", "English"],
        rating=4.7,
        reviews_count=67,
        bio_id="Advokat yang fokus pada hak-hak pekerja dan perlindungan konsumen. Aktif memberikan bantuan hukum pro bono.",
        bio_en="Advocate focused on workers' rights and consumer protection. Active in providing pro bono legal assistance.",
        consultation_types=[ConsultationType.CHAT, ConsultationType.PHONE, ConsultationType.IN_PERSON],
        pricing={"chat": 79000, "phone": 200000, "in_person": 1000000},
        available=True,
    ),
    LawyerProfile(
        id="lawyer-004",
        name="Agus Pratama, S.H.",
        license_number="PERADI/2020/33445",
        bar_association="PERADI",
        specialties=[LawyerSpecialty.PROPERTI, LawyerSpecialty.BISNIS],
        years_experience=6,
        location="Bandung",
        languages=["Bahasa Indonesia", "English"],
        rating=4.6,
        reviews_count=43,
        bio_id="Advokat muda yang aktif menangani kasus pertanahan dan sengketa properti di area Jawa Barat.",
        bio_en="Young advocate actively handling land and property dispute cases in West Java.",
        consultation_types=[ConsultationType.CHAT, ConsultationType.PHONE],
        pricing={"chat": 69000, "phone": 175000},
        available=True,
    ),
]


# ── Endpoints ──────────────────────────────────────────────────────────────

@router.get("/", response_model=list[LawyerProfile])
async def list_lawyers(
    specialty: Optional[LawyerSpecialty] = Query(None, description="Filter by specialty"),
    location: Optional[str] = Query(None, description="Filter by city"),
    consultation_type: Optional[ConsultationType] = Query(None, description="Filter by consultation type"),
    max_price: Optional[int] = Query(None, description="Maximum price for chat consultation (IDR)"),
    min_rating: Optional[float] = Query(None, ge=0, le=5, description="Minimum rating"),
):
    """
    Browse available partner lawyers.
    
    All lawyers are licensed Advocates registered with PERADI, KAI, or IKADIN.
    Filter by specialty, location, consultation type, and budget.
    """
    results = DEMO_LAWYERS.copy()
    
    if specialty:
        results = [l for l in results if specialty in l.specialties]
    
    if location:
        results = [l for l in results if location.lower() in l.location.lower()]
    
    if consultation_type:
        results = [l for l in results if consultation_type in l.consultation_types]
    
    if max_price is not None:
        results = [l for l in results if l.pricing.get("chat", 999999) <= max_price]
    
    if min_rating is not None:
        results = [l for l in results if l.rating >= min_rating]
    
    return results


@router.get("/{lawyer_id}", response_model=LawyerProfile)
async def get_lawyer(lawyer_id: str):
    """Get a specific lawyer's profile"""
    for lawyer in DEMO_LAWYERS:
        if lawyer.id == lawyer_id:
            return lawyer
    
    raise HTTPException(status_code=404, detail="Lawyer not found")


@router.post("/book", response_model=ConsultationResponse)
async def book_consultation(request: ConsultationRequest):
    """
    Book a consultation with a lawyer.
    
    After booking:
    1. You'll receive a Midtrans payment link
    2. Complete payment via GoPay, OVO, bank transfer, etc.
    3. Lawyer will contact you at the scheduled time
    """
    # Find the lawyer
    lawyer = None
    for l in DEMO_LAWYERS:
        if l.id == request.lawyer_id:
            lawyer = l
            break
    
    if not lawyer:
        raise HTTPException(status_code=404, detail="Lawyer not found")
    
    # Get price for consultation type
    price = lawyer.pricing.get(request.consultation_type.value, 0)
    
    # TODO: In production:
    # 1. Check lawyer availability for the requested slot
    # 2. Create booking in database
    # 3. Generate Midtrans payment URL
    # 4. Send confirmation to both parties
    
    return ConsultationResponse(
        booking_id=f"booking-{request.lawyer_id}-demo",
        lawyer_id=lawyer.id,
        lawyer_name=lawyer.name,
        consultation_type=request.consultation_type,
        scheduled_date=request.preferred_date,
        scheduled_time=request.preferred_time,
        price=price,
        payment_url=None,  # TODO: Midtrans payment URL
        status="pending_payment",
    )
