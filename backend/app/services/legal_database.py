"""
Legal Database Service
In-memory Indonesian legal reference store with keyword search.
In production this would be backed by PostgreSQL + Qdrant vector search.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LegalReference:
    """A single Indonesian legal reference entry."""
    id: str
    law_name: str
    short_name: str
    category: str
    description: str
    keywords: list[str] = field(default_factory=list)
    url: Optional[str] = None
    articles: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# In-memory legal reference store
# ---------------------------------------------------------------------------

_LEGAL_REFERENCES: list[LegalReference] = [
    LegalReference(
        id="uu-1-1974",
        law_name="Undang-Undang Nomor 1 Tahun 1974 tentang Perkawinan",
        short_name="UU No. 1 Tahun 1974",
        category="perceraian",
        description="Mengatur tentang perkawinan, syarat sah perkawinan, hak dan kewajiban suami istri, serta perceraian.",
        keywords=["perkawinan", "nikah", "cerai", "divorce", "kawin", "istri", "suami"],
        url="https://peraturan.bpk.go.id/Details/47406/uu-no-1-tahun-1974",
        articles=["Pasal 38-41 (Putusnya Perkawinan)", "Pasal 19 (Alasan Perceraian)"],
    ),
    LegalReference(
        id="khi",
        law_name="Kompilasi Hukum Islam (KHI)",
        short_name="KHI",
        category="perceraian",
        description="Mengatur hukum perkawinan, kewarisan, dan perwakafan bagi umat Islam di Indonesia.",
        keywords=["islam", "talak", "khuluk", "waris", "hibah", "wakaf", "cerai"],
        articles=["Pasal 113-148 (Perceraian)", "Pasal 171-193 (Kewarisan)"],
    ),
    LegalReference(
        id="uu-40-2007",
        law_name="Undang-Undang Nomor 40 Tahun 2007 tentang Perseroan Terbatas",
        short_name="UU No. 40 Tahun 2007",
        category="bisnis",
        description="Mengatur pendirian, tata kelola, dan pembubaran Perseroan Terbatas (PT).",
        keywords=["pt", "perseroan", "perusahaan", "company", "saham", "direktur", "komisaris"],
        url="https://peraturan.bpk.go.id/Details/39965/uu-no-40-tahun-2007",
        articles=["Pasal 7-14 (Pendirian PT)", "Pasal 79-91 (RUPS)"],
    ),
    LegalReference(
        id="uu-11-2020",
        law_name="Undang-Undang Nomor 11 Tahun 2020 tentang Cipta Kerja",
        short_name="UU No. 11 Tahun 2020",
        category="bisnis",
        description="Omnibus law yang menyederhanakan perizinan berusaha melalui sistem OSS RBA.",
        keywords=["usaha", "izin", "oss", "nib", "bisnis", "perizinan", "cipta kerja"],
        articles=["Perizinan Berusaha Berbasis Risiko"],
    ),
    LegalReference(
        id="uu-13-2003",
        law_name="Undang-Undang Nomor 13 Tahun 2003 tentang Ketenagakerjaan",
        short_name="UU No. 13 Tahun 2003",
        category="ketenagakerjaan",
        description="Undang-undang pokok ketenagakerjaan Indonesia mengatur hak dan kewajiban pekerja dan pengusaha.",
        keywords=["kerja", "karyawan", "phk", "pesangon", "upah", "gaji", "lembur", "cuti", "employment"],
        url="https://peraturan.bpk.go.id/Details/43013/uu-no-13-tahun-2003",
        articles=["Pasal 59 (PKWT)", "Pasal 156 (Pesangon)", "Pasal 162 (Pengunduran Diri)"],
    ),
    LegalReference(
        id="pp-35-2021",
        law_name="Peraturan Pemerintah Nomor 35 Tahun 2021",
        short_name="PP No. 35 Tahun 2021",
        category="ketenagakerjaan",
        description="Mengatur PKWT, alih daya, waktu kerja, PHK, uang pesangon, dan kompensasi.",
        keywords=["pkwt", "kontrak", "alih daya", "phk", "pesangon", "kompensasi"],
        articles=["Pasal 1-59 (PKWT dan Alih Daya)", "Pasal 40-59 (PHK)"],
    ),
    LegalReference(
        id="kuh-perdata",
        law_name="Kitab Undang-Undang Hukum Perdata (KUH Perdata / BW)",
        short_name="KUH Perdata",
        category="kontrak",
        description="Hukum perdata umum Indonesia mengatur perjanjian, waris, dan hak kebendaan.",
        keywords=["perjanjian", "kontrak", "agreement", "contract", "waris", "harta", "sewa"],
        articles=["Buku III Pasal 1313-1351 (Perjanjian)", "Pasal 1238 (Somasi)", "Pasal 1548-1600 (Sewa)"],
    ),
    LegalReference(
        id="uu-8-1999",
        law_name="Undang-Undang Nomor 8 Tahun 1999 tentang Perlindungan Konsumen",
        short_name="UU No. 8 Tahun 1999",
        category="konsumen",
        description="Mengatur hak konsumen, kewajiban pelaku usaha, dan penyelesaian sengketa konsumen.",
        keywords=["konsumen", "consumer", "jaminan", "garansi", "refund", "produk cacat", "bpsk"],
        url="https://peraturan.bpk.go.id",
        articles=["Pasal 4-7 (Hak dan Kewajiban)", "Pasal 45-48 (Penyelesaian Sengketa)"],
    ),
    LegalReference(
        id="uu-5-1960",
        law_name="Undang-Undang Nomor 5 Tahun 1960 tentang Pokok-Pokok Agraria (UUPA)",
        short_name="UU No. 5 Tahun 1960 (UUPA)",
        category="properti",
        description="Mengatur hak atas tanah di Indonesia, termasuk HM, HGU, HGB, dan hak pakai.",
        keywords=["tanah", "properti", "shm", "hgb", "hgu", "sertifikat", "land", "property"],
        url="https://peraturan.bpk.go.id",
        articles=["Pasal 16 (Jenis Hak Atas Tanah)", "Pasal 20 (Hak Milik)"],
    ),
    LegalReference(
        id="uu-28-2014",
        law_name="Undang-Undang Nomor 28 Tahun 2014 tentang Hak Cipta",
        short_name="UU No. 28 Tahun 2014",
        category="kekayaan_intelektual",
        description="Mengatur perlindungan hak cipta atas karya intelektual.",
        keywords=["hak cipta", "copyright", "karya", "kreasi", "plagiat"],
        url="https://peraturan.bpk.go.id",
        articles=["Pasal 40 (Ciptaan yang Dilindungi)", "Pasal 58-67 (Masa Berlaku)"],
    ),
    LegalReference(
        id="uu-20-2016",
        law_name="Undang-Undang Nomor 20 Tahun 2016 tentang Merek dan Indikasi Geografis",
        short_name="UU No. 20 Tahun 2016",
        category="kekayaan_intelektual",
        description="Mengatur pendaftaran dan perlindungan merek dagang di Indonesia.",
        keywords=["merek", "trademark", "logo", "brand", "pendaftaran merek"],
        articles=["Pasal 20 (Merek yang Tidak Dapat Didaftar)", "Pasal 35 (Jangka Waktu Merek)"],
    ),
]


class LegalDatabase:
    """
    Simple in-memory legal reference database with keyword search.
    In production this is replaced by a PostgreSQL + Qdrant implementation.
    """

    def __init__(self) -> None:
        self._refs: dict[str, LegalReference] = {r.id: r for r in _LEGAL_REFERENCES}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_by_id(self, ref_id: str) -> Optional[LegalReference]:
        """Return a specific legal reference by its ID."""
        return self._refs.get(ref_id)

    def get_by_category(self, category: str) -> list[LegalReference]:
        """Return all legal references for a given category."""
        return [r for r in self._refs.values() if r.category == category]

    def search(self, query: str, limit: int = 5) -> list[LegalReference]:
        """
        Keyword-based search over all legal references.
        Returns up to *limit* results ordered by relevance score.
        """
        query_lower = query.lower()
        scored: list[tuple[int, LegalReference]] = []

        for ref in self._refs.values():
            score = 0
            # Score keyword matches
            score += sum(2 for kw in ref.keywords if kw in query_lower)
            # Score matches in law name / description
            if query_lower in ref.law_name.lower():
                score += 3
            if query_lower in ref.description.lower():
                score += 1
            if query_lower in ref.category.lower():
                score += 2
            if score > 0:
                scored.append((score, ref))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [ref for _, ref in scored[:limit]]

    def list_all(self) -> list[LegalReference]:
        """Return all legal references."""
        return list(self._refs.values())

    def list_categories(self) -> list[str]:
        """Return distinct categories."""
        return sorted({r.category for r in self._refs.values()})


# Singleton instance
legal_db = LegalDatabase()
