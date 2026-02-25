"use client";

import { useState } from "react";

interface Template {
  id: string;
  name_id: string;
  name_en: string;
  description_id: string;
  complexity: string;
  legal_basis: string[];
  estimated_cost?: string;
}

interface TemplateCategory {
  id: string;
  icon: string;
  name: string;
  name_en: string;
  color: string;
  templates: Template[];
}

const TEMPLATE_DATA: TemplateCategory[] = [
  {
    id: "family",
    icon: "💔",
    name: "Hukum Keluarga",
    name_en: "Family Law",
    color: "rose",
    templates: [
      {
        id: "surat-gugatan-cerai",
        name_id: "Surat Gugatan Cerai",
        name_en: "Divorce Petition (Wife Filing)",
        description_id: "Surat gugatan perceraian yang diajukan oleh istri kepada Pengadilan Agama",
        complexity: "moderate",
        legal_basis: ["UU No. 1/1974", "KHI Pasal 116"],
        estimated_cost: "Rp 300.000 - 1.000.000",
      },
      {
        id: "surat-permohonan-cerai-talak",
        name_id: "Surat Permohonan Cerai Talak",
        name_en: "Divorce Petition (Husband Filing)",
        description_id: "Surat permohonan cerai talak yang diajukan oleh suami kepada Pengadilan Agama",
        complexity: "moderate",
        legal_basis: ["UU No. 1/1974", "KHI Pasal 129-131"],
        estimated_cost: "Rp 300.000 - 1.000.000",
      },
      {
        id: "perjanjian-pranikah",
        name_id: "Perjanjian Pranikah",
        name_en: "Prenuptial Agreement",
        description_id: "Perjanjian perkawinan yang mengatur pemisahan harta dan hal-hal lain",
        complexity: "complex",
        legal_basis: ["UU No. 1/1974 Pasal 29", "Putusan MK No. 69/PUU-XIII/2015"],
        estimated_cost: "Rp 1.000.000 - 5.000.000",
      },
      {
        id: "surat-keterangan-waris",
        name_id: "Surat Keterangan Waris",
        name_en: "Inheritance Declaration",
        description_id: "Surat keterangan ahli waris untuk menetapkan siapa yang berhak atas warisan",
        complexity: "moderate",
        legal_basis: ["KUHPerdata Buku II", "KHI Buku II"],
      },
      {
        id: "surat-wasiat",
        name_id: "Surat Wasiat (Testament)",
        name_en: "Last Will and Testament",
        description_id: "Surat wasiat untuk mengatur pembagian harta setelah meninggal dunia",
        complexity: "complex",
        legal_basis: ["KUHPerdata Pasal 875-1004", "KHI Pasal 194-209"],
        estimated_cost: "Rp 1.000.000 - 5.000.000",
      },
    ],
  },
  {
    id: "business",
    icon: "🏢",
    name: "Bisnis & Perusahaan",
    name_en: "Business & Corporate",
    color: "blue",
    templates: [
      {
        id: "akta-pendirian-pt",
        name_id: "Akta Pendirian PT",
        name_en: "Company Incorporation Deed",
        description_id: "Akta pendirian Perseroan Terbatas (PT) melalui notaris",
        complexity: "complex",
        legal_basis: ["UU No. 40/2007", "PP No. 8/2021"],
        estimated_cost: "Rp 5.000.000 - 15.000.000",
      },
      {
        id: "perjanjian-kerjasama",
        name_id: "Perjanjian Kerjasama",
        name_en: "Partnership Agreement",
        description_id: "Perjanjian kerjasama bisnis antara dua pihak atau lebih",
        complexity: "moderate",
        legal_basis: ["KUHPerdata Pasal 1313, 1320, 1338"],
      },
      {
        id: "surat-kuasa",
        name_id: "Surat Kuasa",
        name_en: "Power of Attorney",
        description_id: "Surat kuasa umum atau khusus untuk bertindak atas nama pemberi kuasa",
        complexity: "simple",
        legal_basis: ["KUHPerdata Pasal 1792-1819"],
      },
      {
        id: "perjanjian-jual-beli",
        name_id: "Perjanjian Jual Beli",
        name_en: "Sale & Purchase Agreement",
        description_id: "Perjanjian jual beli barang atau jasa antara penjual dan pembeli",
        complexity: "moderate",
        legal_basis: ["KUHPerdata Pasal 1457-1540"],
      },
      {
        id: "non-disclosure-agreement",
        name_id: "NDA / Kerahasiaan",
        name_en: "Non-Disclosure Agreement",
        description_id: "Perjanjian kerahasiaan untuk melindungi informasi bisnis sensitif",
        complexity: "moderate",
        legal_basis: ["KUHPerdata Pasal 1338", "UU No. 30/2000"],
      },
    ],
  },
  {
    id: "employment",
    icon: "👷",
    name: "Ketenagakerjaan",
    name_en: "Employment",
    color: "amber",
    templates: [
      {
        id: "kontrak-kerja-pkwt",
        name_id: "Kontrak Kerja PKWT",
        name_en: "Fixed-Term Employment Contract",
        description_id: "Perjanjian Kerja Waktu Tertentu untuk karyawan kontrak",
        complexity: "moderate",
        legal_basis: ["UU No. 13/2003", "PP No. 35/2021"],
      },
      {
        id: "kontrak-kerja-pkwtt",
        name_id: "Kontrak Kerja PKWTT",
        name_en: "Permanent Employment Contract",
        description_id: "Perjanjian Kerja Waktu Tidak Tertentu untuk karyawan tetap",
        complexity: "moderate",
        legal_basis: ["UU No. 13/2003 Pasal 60-63"],
      },
      {
        id: "surat-pengunduran-diri",
        name_id: "Surat Pengunduran Diri",
        name_en: "Resignation Letter",
        description_id: "Surat pengunduran diri karyawan dengan pemberitahuan 30 hari",
        complexity: "simple",
        legal_basis: ["UU No. 13/2003 Pasal 162"],
      },
      {
        id: "surat-peringatan",
        name_id: "Surat Peringatan (SP)",
        name_en: "Warning Letter (SP1/SP2/SP3)",
        description_id: "Surat peringatan karyawan atas pelanggaran disiplin",
        complexity: "simple",
        legal_basis: ["UU No. 13/2003 Pasal 161"],
      },
      {
        id: "surat-phk",
        name_id: "Surat PHK",
        name_en: "Termination Letter",
        description_id: "Surat pemutusan hubungan kerja dengan perhitungan pesangon",
        complexity: "complex",
        legal_basis: ["UU No. 13/2003 Pasal 150-172", "PP No. 35/2021"],
      },
    ],
  },
  {
    id: "property",
    icon: "🏠",
    name: "Properti & Tanah",
    name_en: "Property & Land",
    color: "green",
    templates: [
      {
        id: "perjanjian-sewa-menyewa",
        name_id: "Perjanjian Sewa Menyewa",
        name_en: "Rental/Lease Agreement",
        description_id: "Perjanjian sewa menyewa rumah, apartemen, ruko, atau properti lainnya",
        complexity: "moderate",
        legal_basis: ["KUHPerdata Pasal 1548-1600"],
        estimated_cost: "Rp 500.000 - 2.000.000",
      },
      {
        id: "perjanjian-jual-beli-tanah",
        name_id: "Perjanjian Jual Beli Tanah (PPJB)",
        name_en: "Land Sale Agreement",
        description_id: "Perjanjian pengikatan jual beli tanah/properti",
        complexity: "complex",
        legal_basis: ["UUPA No. 5/1960", "PP No. 18/2021"],
        estimated_cost: "Rp 2.000.000 - 10.000.000",
      },
      {
        id: "surat-kuasa-jual-tanah",
        name_id: "Surat Kuasa Jual Tanah",
        name_en: "Power of Attorney - Land Sale",
        description_id: "Surat kuasa khusus untuk menjual tanah/properti",
        complexity: "moderate",
        legal_basis: ["KUHPerdata Pasal 1792", "PP 24/1997"],
      },
    ],
  },
  {
    id: "general",
    icon: "⚖️",
    name: "Umum & Pidana",
    name_en: "General & Criminal",
    color: "purple",
    templates: [
      {
        id: "surat-somasi",
        name_id: "Surat Somasi",
        name_en: "Demand/Warning Letter",
        description_id: "Surat teguran hukum (somasi) untuk menuntut pemenuhan kewajiban",
        complexity: "moderate",
        legal_basis: ["KUHPerdata Pasal 1238, 1243"],
      },
      {
        id: "surat-pernyataan",
        name_id: "Surat Pernyataan",
        name_en: "Sworn Statement/Affidavit",
        description_id: "Surat pernyataan resmi bermaterai untuk berbagai keperluan",
        complexity: "simple",
        legal_basis: ["KUHPerdata Pasal 1875"],
      },
      {
        id: "surat-pengaduan-polisi",
        name_id: "Surat Pengaduan Polisi",
        name_en: "Police Complaint Letter",
        description_id: "Surat pengaduan/laporan ke kepolisian atas tindak pidana",
        complexity: "moderate",
        legal_basis: ["KUHAP Pasal 108"],
      },
      {
        id: "surat-pengaduan-konsumen",
        name_id: "Surat Pengaduan Konsumen",
        name_en: "Consumer Complaint",
        description_id: "Surat pengaduan konsumen atas pelanggaran hak",
        complexity: "simple",
        legal_basis: ["UU No. 8/1999", "PP No. 58/2001"],
      },
      {
        id: "perjanjian-perdamaian",
        name_id: "Perjanjian Perdamaian",
        name_en: "Settlement Agreement",
        description_id: "Perjanjian damai untuk menyelesaikan sengketa di luar pengadilan",
        complexity: "moderate",
        legal_basis: ["KUHPerdata Pasal 1851-1864"],
      },
    ],
  },
];

const complexityConfig = {
  simple: { label: "Mudah", color: "bg-green-100 text-green-700", icon: "🟢" },
  moderate: { label: "Sedang", color: "bg-yellow-100 text-yellow-700", icon: "🟡" },
  complex: { label: "Kompleks", color: "bg-red-100 text-red-700", icon: "🔴" },
};

export default function TemplatesPage() {
  const [activeCategory, setActiveCategory] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState("");

  const filteredCategories =
    activeCategory === "all"
      ? TEMPLATE_DATA
      : TEMPLATE_DATA.filter((c) => c.id === activeCategory);

  const totalTemplates = TEMPLATE_DATA.reduce((sum, c) => sum + c.templates.length, 0);

  const filteredTemplates = filteredCategories
    .map((cat) => ({
      ...cat,
      templates: cat.templates.filter(
        (t) =>
          !searchQuery ||
          t.name_id.toLowerCase().includes(searchQuery.toLowerCase()) ||
          t.name_en.toLowerCase().includes(searchQuery.toLowerCase()) ||
          t.description_id.toLowerCase().includes(searchQuery.toLowerCase())
      ),
    }))
    .filter((cat) => cat.templates.length > 0);

  return (
    <main className="min-h-screen bg-gray-50">
      {/* Header */}
      <nav className="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <a href="./" className="flex items-center gap-2">
              <span className="text-2xl">⚖️</span>
              <span className="font-bold text-xl text-blue-900">AI Lawyer</span>
              <span className="text-xs bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">BETA</span>
            </a>
            <div className="hidden md:flex items-center gap-8">
              <a href="./" className="text-gray-600 hover:text-blue-700 text-sm font-medium">Beranda</a>
              <a href="./templates" className="text-blue-700 text-sm font-bold">Template Dokumen</a>
              <a href="./knowledge" className="text-gray-600 hover:text-blue-700 text-sm font-medium">Basis Pengetahuan</a>
            </div>
            <button className="bg-blue-700 hover:bg-blue-800 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors">
              Daftar Gratis
            </button>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="pt-28 pb-12 px-4 bg-gradient-to-br from-blue-50 via-white to-indigo-50">
        <div className="max-w-7xl mx-auto text-center">
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-gray-900 mb-4">
            📄 Template <span className="text-blue-700">Dokumen Hukum</span>
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto mb-8">
            {totalTemplates} template dokumen hukum Indonesia siap pakai. Isi formulir, AI
            generate dokumen Anda secara otomatis. Sesuai hukum yang berlaku.
          </p>

          {/* Search */}
          <div className="max-w-xl mx-auto mb-8">
            <div className="relative">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Cari template... contoh: perceraian, kontrak kerja, sewa"
                className="w-full border border-gray-300 rounded-xl px-5 py-3 pl-12 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent shadow-sm"
              />
              <span className="absolute left-4 top-3.5 text-gray-400">🔍</span>
            </div>
          </div>

          {/* Category Filter */}
          <div className="flex flex-wrap justify-center gap-2">
            <button
              onClick={() => setActiveCategory("all")}
              className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                activeCategory === "all"
                  ? "bg-blue-700 text-white shadow-md"
                  : "bg-white text-gray-600 border border-gray-200 hover:border-blue-300"
              }`}
            >
              Semua ({totalTemplates})
            </button>
            {TEMPLATE_DATA.map((cat) => (
              <button
                key={cat.id}
                onClick={() => setActiveCategory(cat.id)}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                  activeCategory === cat.id
                    ? "bg-blue-700 text-white shadow-md"
                    : "bg-white text-gray-600 border border-gray-200 hover:border-blue-300"
                }`}
              >
                {cat.icon} {cat.name} ({cat.templates.length})
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* Templates Grid */}
      <section className="py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          {filteredTemplates.map((category) => (
            <div key={category.id} className="mb-12">
              <h2 className="text-2xl font-bold text-gray-900 mb-2 flex items-center gap-3">
                <span className="text-3xl">{category.icon}</span>
                {category.name}
                <span className="text-sm font-normal text-gray-400">
                  ({category.name_en})
                </span>
              </h2>
              <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
                {category.templates.map((template) => {
                  const comp = complexityConfig[template.complexity as keyof typeof complexityConfig];
                  return (
                    <div
                      key={template.id}
                      className="bg-white border border-gray-200 rounded-xl p-5 hover:shadow-lg hover:border-blue-200 transition-all group cursor-pointer"
                    >
                      <div className="flex items-start justify-between mb-3">
                        <h3 className="font-bold text-gray-900 group-hover:text-blue-700 transition-colors">
                          {template.name_id}
                        </h3>
                        <span className={`text-xs px-2 py-1 rounded-full font-medium ${comp.color}`}>
                          {comp.icon} {comp.label}
                        </span>
                      </div>
                      <p className="text-xs text-gray-400 mb-2 italic">{template.name_en}</p>
                      <p className="text-sm text-gray-600 mb-4">{template.description_id}</p>

                      <div className="flex flex-wrap gap-1 mb-3">
                        {template.legal_basis.map((law) => (
                          <span
                            key={law}
                            className="text-[10px] bg-gray-100 text-gray-500 px-2 py-0.5 rounded"
                          >
                            {law}
                          </span>
                        ))}
                      </div>

                      {template.estimated_cost && (
                        <p className="text-xs text-gray-400 mb-3">
                          💰 Estimasi biaya: {template.estimated_cost}
                        </p>
                      )}

                      <button className="w-full bg-blue-50 hover:bg-blue-100 text-blue-700 text-sm font-medium py-2 rounded-lg transition-colors">
                        📝 Buat Dokumen Ini
                      </button>
                    </div>
                  );
                })}
              </div>
            </div>
          ))}

          {filteredTemplates.length === 0 && (
            <div className="text-center py-20">
              <p className="text-4xl mb-4">🔍</p>
              <p className="text-gray-500">
                Tidak ada template ditemukan untuk &quot;{searchQuery}&quot;
              </p>
              <button
                onClick={() => {
                  setSearchQuery("");
                  setActiveCategory("all");
                }}
                className="mt-4 text-blue-700 hover:underline text-sm"
              >
                Reset pencarian
              </button>
            </div>
          )}
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-4 bg-blue-700">
        <div className="max-w-4xl mx-auto text-center text-white">
          <h2 className="text-3xl font-bold mb-4">Butuh Template Lain?</h2>
          <p className="text-blue-100 mb-8">
            Tidak menemukan template yang Anda butuhkan? Tanya AI Lawyer dan kami
            akan membuatkan dokumen khusus untuk Anda.
          </p>
          <a
            href="./"
            className="inline-block bg-white text-blue-700 font-semibold px-8 py-3 rounded-xl hover:bg-blue-50 transition-colors"
          >
            💬 Tanya AI Lawyer
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-400 py-8 px-4">
        <div className="max-w-7xl mx-auto text-center text-sm">
          <p>© 2025 AI Lawyer (Hukum AI). Semua hak dilindungi undang-undang.</p>
          <p className="text-xs mt-2 text-gray-500">
            ⚠️ Informasi umum, bukan nasihat hukum. Konsultasi Advokat berlisensi untuk nasihat hukum resmi.
          </p>
        </div>
      </footer>
    </main>
  );
}
