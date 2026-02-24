"""
Legal Document Templates Endpoint
Browse and access Indonesian legal document templates
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

router = APIRouter()


class TemplateTier(str, Enum):
    FREE = "free"
    STARTER = "starter"
    PROFESSIONAL = "professional"
    BUSINESS = "business"


class TemplateCategory(str, Enum):
    PERCERAIAN = "perceraian"
    BISNIS = "bisnis"
    KETENAGAKERJAAN = "ketenagakerjaan"
    WARIS = "waris"
    WASIAT = "wasiat"
    KONTRAK = "kontrak"
    PROPERTI = "properti"
    KONSUMEN = "konsumen"
    KEKAYAAN_INTELEKTUAL = "kekayaan_intelektual"


class TemplateField(BaseModel):
    name: str
    label: str
    field_type: str
    required: bool = True
    placeholder: Optional[str] = None
    options: Optional[list[str]] = None


class Template(BaseModel):
    id: str
    name_id: str  # Indonesian name
    name_en: str  # English name
    description_id: str
    description_en: str
    category: TemplateCategory
    tier: TemplateTier
    fields: list[TemplateField]
    estimated_time: str  # e.g., "5 minutes"
    price: int  # in IDR, 0 for free
    popular: bool = False
    legal_basis: Optional[str] = None  # e.g., "UU No. 1 Tahun 1974"


# ── Template Database (MVP - In production, stored in PostgreSQL) ──────────

TEMPLATES = [
    # ── DIVORCE TEMPLATES ──
    Template(
        id="surat-gugatan-cerai",
        name_id="Surat Gugatan Cerai",
        name_en="Divorce Petition Letter",
        description_id="Surat gugatan perceraian yang diajukan ke Pengadilan Agama (Islam) atau Pengadilan Negeri (non-Islam)",
        description_en="Divorce petition letter filed to Religious Court (Muslim) or District Court (non-Muslim)",
        category=TemplateCategory.PERCERAIAN,
        tier=TemplateTier.STARTER,
        popular=True,
        price=50000,
        estimated_time="10 menit",
        legal_basis="UU No. 1 Tahun 1974, PP No. 9 Tahun 1975",
        fields=[
            TemplateField(name="nama_penggugat", label="Nama Penggugat (Istri/Suami)", field_type="text", placeholder="Nama lengkap sesuai KTP"),
            TemplateField(name="nik_penggugat", label="NIK Penggugat", field_type="text", placeholder="16 digit NIK"),
            TemplateField(name="alamat_penggugat", label="Alamat Penggugat", field_type="textarea"),
            TemplateField(name="nama_tergugat", label="Nama Tergugat", field_type="text"),
            TemplateField(name="nik_tergugat", label="NIK Tergugat", field_type="text"),
            TemplateField(name="alamat_tergugat", label="Alamat Tergugat", field_type="textarea"),
            TemplateField(name="tanggal_nikah", label="Tanggal Pernikahan", field_type="date"),
            TemplateField(name="tempat_nikah", label="Tempat Pernikahan", field_type="text"),
            TemplateField(name="nomor_akta_nikah", label="Nomor Akta Nikah", field_type="text"),
            TemplateField(name="jumlah_anak", label="Jumlah Anak", field_type="number", placeholder="0"),
            TemplateField(name="alasan_cerai", label="Alasan Perceraian", field_type="textarea", placeholder="Jelaskan alasan perceraian"),
            TemplateField(name="tuntutan", label="Tuntutan/Permohonan", field_type="textarea", placeholder="Hak asuh anak, harta gono-gini, nafkah, dll"),
            TemplateField(name="agama", label="Agama", field_type="select", options=["Islam", "Kristen", "Katolik", "Hindu", "Buddha", "Konghucu"]),
            TemplateField(name="pengadilan", label="Pengadilan Tujuan", field_type="text", placeholder="Pengadilan Agama/Negeri [Kota]"),
        ],
    ),
    Template(
        id="surat-permohonan-cerai-talak",
        name_id="Surat Permohonan Cerai Talak",
        name_en="Talak Divorce Application",
        description_id="Permohonan cerai talak yang diajukan oleh suami ke Pengadilan Agama",
        description_en="Talak divorce application filed by husband to Religious Court",
        category=TemplateCategory.PERCERAIAN,
        tier=TemplateTier.STARTER,
        price=50000,
        estimated_time="10 menit",
        legal_basis="UU No. 1 Tahun 1974, KHI Pasal 129-148",
        fields=[
            TemplateField(name="nama_pemohon", label="Nama Pemohon (Suami)", field_type="text"),
            TemplateField(name="nama_termohon", label="Nama Termohon (Istri)", field_type="text"),
            TemplateField(name="alasan", label="Alasan Permohonan Talak", field_type="textarea"),
            TemplateField(name="tanggal_nikah", label="Tanggal Pernikahan", field_type="date"),
        ],
    ),

    # ── BUSINESS TEMPLATES ──
    Template(
        id="akta-pendirian-pt",
        name_id="Panduan Pendirian PT",
        name_en="PT Company Formation Guide",
        description_id="Panduan lengkap dan template untuk mendirikan Perseroan Terbatas (PT) di Indonesia",
        description_en="Complete guide and template for establishing a Limited Liability Company (PT) in Indonesia",
        category=TemplateCategory.BISNIS,
        tier=TemplateTier.PROFESSIONAL,
        popular=True,
        price=200000,
        estimated_time="30 menit",
        legal_basis="UU No. 40 Tahun 2007, UU No. 11 Tahun 2020",
        fields=[
            TemplateField(name="nama_perusahaan", label="Nama PT (3 pilihan)", field_type="text", placeholder="PT [Nama] [Nama Alternatif 1] [Nama Alternatif 2]"),
            TemplateField(name="bidang_usaha", label="Bidang Usaha (KBLI)", field_type="text", placeholder="Kode KBLI dan deskripsi"),
            TemplateField(name="modal_dasar", label="Modal Dasar", field_type="text", placeholder="Minimal Rp 50.000.000"),
            TemplateField(name="modal_disetor", label="Modal Disetor", field_type="text", placeholder="Minimal 25% dari modal dasar"),
            TemplateField(name="nama_direktur", label="Nama Direktur Utama", field_type="text"),
            TemplateField(name="nama_komisaris", label="Nama Komisaris", field_type="text"),
            TemplateField(name="alamat_perusahaan", label="Alamat Perusahaan", field_type="textarea"),
            TemplateField(name="pemegang_saham", label="Data Pemegang Saham", field_type="textarea", placeholder="Nama, NIK/Paspor, persentase saham masing-masing"),
        ],
    ),
    Template(
        id="perjanjian-kerjasama",
        name_id="Perjanjian Kerjasama",
        name_en="Partnership Agreement",
        description_id="Template perjanjian kerjasama antar pihak untuk berbagai keperluan bisnis",
        description_en="Partnership agreement template for various business needs",
        category=TemplateCategory.KONTRAK,
        tier=TemplateTier.FREE,
        popular=True,
        price=0,
        estimated_time="15 menit",
        legal_basis="KUH Perdata Pasal 1313-1351",
        fields=[
            TemplateField(name="nama_pihak_pertama", label="Nama Pihak Pertama", field_type="text"),
            TemplateField(name="jabatan_pihak_pertama", label="Jabatan Pihak Pertama", field_type="text"),
            TemplateField(name="alamat_pihak_pertama", label="Alamat Pihak Pertama", field_type="textarea"),
            TemplateField(name="nama_pihak_kedua", label="Nama Pihak Kedua", field_type="text"),
            TemplateField(name="jabatan_pihak_kedua", label="Jabatan Pihak Kedua", field_type="text"),
            TemplateField(name="alamat_pihak_kedua", label="Alamat Pihak Kedua", field_type="textarea"),
            TemplateField(name="ruang_lingkup", label="Ruang Lingkup Kerjasama", field_type="textarea"),
            TemplateField(name="durasi", label="Durasi Kerjasama", field_type="text", placeholder="12 bulan"),
            TemplateField(name="pembagian_keuntungan", label="Pembagian Keuntungan", field_type="text", placeholder="50:50"),
        ],
    ),

    # ── EMPLOYMENT TEMPLATES ──
    Template(
        id="kontrak-kerja-pkwt",
        name_id="Kontrak Kerja PKWT",
        name_en="Fixed-Term Employment Contract (PKWT)",
        description_id="Perjanjian Kerja Waktu Tertentu sesuai UU Ketenagakerjaan dan PP 35/2021",
        description_en="Fixed-Term Employment Contract per Indonesian Labor Law",
        category=TemplateCategory.KETENAGAKERJAAN,
        tier=TemplateTier.FREE,
        popular=True,
        price=0,
        estimated_time="10 menit",
        legal_basis="UU No. 13 Tahun 2003, PP No. 35 Tahun 2021",
        fields=[
            TemplateField(name="nama_perusahaan", label="Nama Perusahaan", field_type="text"),
            TemplateField(name="nama_karyawan", label="Nama Karyawan", field_type="text"),
            TemplateField(name="jabatan", label="Jabatan/Posisi", field_type="text"),
            TemplateField(name="gaji_pokok", label="Gaji Pokok (IDR)", field_type="number"),
            TemplateField(name="tunjangan", label="Tunjangan", field_type="textarea", placeholder="Transport, makan, kesehatan, dll"),
            TemplateField(name="tanggal_mulai", label="Tanggal Mulai Kerja", field_type="date"),
            TemplateField(name="durasi_kontrak", label="Durasi Kontrak", field_type="text", placeholder="12 bulan"),
            TemplateField(name="jam_kerja", label="Jam Kerja", field_type="text", placeholder="08:00-17:00, Senin-Jumat"),
            TemplateField(name="lokasi_kerja", label="Lokasi Kerja", field_type="text"),
        ],
    ),
    Template(
        id="surat-pengunduran-diri",
        name_id="Surat Pengunduran Diri",
        name_en="Resignation Letter",
        description_id="Template surat pengunduran diri karyawan yang profesional",
        description_en="Professional employee resignation letter template",
        category=TemplateCategory.KETENAGAKERJAAN,
        tier=TemplateTier.FREE,
        price=0,
        estimated_time="5 menit",
        legal_basis="UU No. 13 Tahun 2003 Pasal 162",
        fields=[
            TemplateField(name="nama_karyawan", label="Nama Karyawan", field_type="text"),
            TemplateField(name="jabatan", label="Jabatan", field_type="text"),
            TemplateField(name="departemen", label="Departemen", field_type="text"),
            TemplateField(name="nama_perusahaan", label="Nama Perusahaan", field_type="text"),
            TemplateField(name="tanggal_efektif", label="Tanggal Efektif Pengunduran Diri", field_type="date"),
            TemplateField(name="alasan", label="Alasan (Opsional)", field_type="textarea", required=False),
        ],
    ),

    # ── INHERITANCE TEMPLATES ──
    Template(
        id="surat-keterangan-waris",
        name_id="Surat Keterangan Waris",
        name_en="Certificate of Inheritance",
        description_id="Surat keterangan hak waris untuk pembagian harta warisan",
        description_en="Certificate of inheritance rights for estate distribution",
        category=TemplateCategory.WARIS,
        tier=TemplateTier.STARTER,
        price=75000,
        estimated_time="15 menit",
        legal_basis="KUH Perdata, KHI (untuk Islam), Hukum Adat",
        fields=[
            TemplateField(name="nama_pewaris", label="Nama Almarhum/ah (Pewaris)", field_type="text"),
            TemplateField(name="tanggal_meninggal", label="Tanggal Meninggal", field_type="date"),
            TemplateField(name="ahli_waris", label="Daftar Ahli Waris", field_type="textarea", placeholder="Nama, hubungan, dan bagian masing-masing"),
            TemplateField(name="harta_warisan", label="Daftar Harta Warisan", field_type="textarea", placeholder="Tanah, rumah, tabungan, kendaraan, dll"),
            TemplateField(name="sistem_hukum", label="Sistem Hukum Waris", field_type="select", options=["Hukum Islam (Faraid)", "Hukum Perdata (BW)", "Hukum Adat"]),
        ],
    ),

    # ── CONTRACT TEMPLATES ──
    Template(
        id="nda",
        name_id="Perjanjian Kerahasiaan (NDA)",
        name_en="Non-Disclosure Agreement (NDA)",
        description_id="Perjanjian kerahasiaan untuk melindungi informasi bisnis rahasia",
        description_en="Non-disclosure agreement to protect confidential business information",
        category=TemplateCategory.KEKAYAAN_INTELEKTUAL,
        tier=TemplateTier.FREE,
        popular=True,
        price=0,
        estimated_time="10 menit",
        fields=[
            TemplateField(name="pihak_pengungkap", label="Pihak Pengungkap (Disclosing Party)", field_type="text"),
            TemplateField(name="pihak_penerima", label="Pihak Penerima (Receiving Party)", field_type="text"),
            TemplateField(name="jenis_informasi", label="Jenis Informasi Rahasia", field_type="textarea"),
            TemplateField(name="durasi", label="Durasi Kerahasiaan", field_type="text", placeholder="2 tahun"),
            TemplateField(name="yurisdiksi", label="Yurisdiksi Hukum", field_type="text", placeholder="Jakarta, Indonesia"),
        ],
    ),
    Template(
        id="surat-somasi",
        name_id="Surat Somasi",
        name_en="Formal Warning/Demand Letter",
        description_id="Surat peringatan/teguran resmi sebelum mengambil tindakan hukum",
        description_en="Formal warning/demand letter before taking legal action",
        category=TemplateCategory.KONSUMEN,
        tier=TemplateTier.STARTER,
        price=50000,
        estimated_time="10 menit",
        legal_basis="KUH Perdata Pasal 1238",
        fields=[
            TemplateField(name="nama_pengirim", label="Nama Pengirim", field_type="text"),
            TemplateField(name="nama_penerima", label="Nama Penerima Somasi", field_type="text"),
            TemplateField(name="perihal", label="Perihal Somasi", field_type="text"),
            TemplateField(name="kronologi", label="Kronologi Masalah", field_type="textarea"),
            TemplateField(name="tuntutan", label="Tuntutan", field_type="textarea"),
            TemplateField(name="batas_waktu", label="Batas Waktu Respon", field_type="text", placeholder="7 hari kerja"),
        ],
    ),
    Template(
        id="perjanjian-sewa-menyewa",
        name_id="Perjanjian Sewa Menyewa",
        name_en="Rental/Lease Agreement",
        description_id="Perjanjian sewa menyewa untuk properti (rumah, ruko, kantor, dll)",
        description_en="Rental/lease agreement for property (house, shophouse, office, etc.)",
        category=TemplateCategory.PROPERTI,
        tier=TemplateTier.FREE,
        price=0,
        estimated_time="10 menit",
        legal_basis="KUH Perdata Pasal 1548-1600",
        fields=[
            TemplateField(name="nama_pemilik", label="Nama Pemilik (Pihak Pertama)", field_type="text"),
            TemplateField(name="nama_penyewa", label="Nama Penyewa (Pihak Kedua)", field_type="text"),
            TemplateField(name="alamat_properti", label="Alamat Properti", field_type="textarea"),
            TemplateField(name="jenis_properti", label="Jenis Properti", field_type="select", options=["Rumah", "Ruko", "Kantor", "Apartemen", "Tanah", "Gudang"]),
            TemplateField(name="harga_sewa", label="Harga Sewa per Bulan/Tahun", field_type="text"),
            TemplateField(name="durasi_sewa", label="Durasi Sewa", field_type="text", placeholder="12 bulan"),
            TemplateField(name="deposit", label="Deposit/Uang Jaminan", field_type="text"),
        ],
    ),
]


# ── Endpoints ──────────────────────────────────────────────────────────────

@router.get("/", response_model=list[Template])
async def list_templates(
    category: Optional[TemplateCategory] = Query(None, description="Filter by category"),
    tier: Optional[TemplateTier] = Query(None, description="Filter by pricing tier"),
    search: Optional[str] = Query(None, description="Search templates"),
    popular: Optional[bool] = Query(None, description="Show only popular templates"),
):
    """
    Browse available legal document templates.
    
    Templates are organized by:
    - **Category**: Divorce, Business, Employment, Inheritance, etc.
    - **Tier**: Free, Starter (Rp 50k), Professional (Rp 200k), Business
    """
    results = TEMPLATES.copy()
    
    if category:
        results = [t for t in results if t.category == category]
    
    if tier:
        results = [t for t in results if t.tier == tier]
    
    if popular is not None:
        results = [t for t in results if t.popular == popular]
    
    if search:
        search_lower = search.lower()
        results = [
            t for t in results
            if search_lower in t.name_id.lower()
            or search_lower in t.name_en.lower()
            or search_lower in t.description_id.lower()
            or search_lower in t.description_en.lower()
        ]
    
    return results


@router.get("/categories")
async def get_template_categories():
    """Get all template categories with counts"""
    categories = {}
    for template in TEMPLATES:
        cat = template.category.value
        if cat not in categories:
            categories[cat] = {
                "category": cat,
                "count": 0,
                "free_count": 0,
            }
        categories[cat]["count"] += 1
        if template.tier == TemplateTier.FREE:
            categories[cat]["free_count"] += 1
    
    return {"categories": list(categories.values())}


@router.get("/popular")
async def get_popular_templates():
    """Get the most popular templates"""
    popular = [t for t in TEMPLATES if t.popular]
    return {"templates": popular}


@router.get("/{template_id}", response_model=Template)
async def get_template(template_id: str):
    """Get a specific template by ID with all its fields"""
    for template in TEMPLATES:
        if template.id == template_id:
            return template
    
    raise HTTPException(status_code=404, detail=f"Template '{template_id}' not found")
