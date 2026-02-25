"use client";

import { useState } from "react";

interface FAQItem {
  q: string;
  a: string;
}

interface ProcedureItem {
  id: string;
  icon: string;
  title: string;
  title_en: string;
  steps: number;
  timeline: string;
  description: string;
}

interface LawRef {
  id: string;
  icon: string;
  title: string;
  laws: string[];
  topics: string;
}

const LAW_REFS: LawRef[] = [
  {
    id: "family",
    icon: "💔",
    title: "Hukum Keluarga",
    laws: ["UU No. 1/1974", "KHI", "UU No. 23/2004 (KDRT)"],
    topics: "Pernikahan, perceraian, hak asuh anak, waris, KDRT, perjanjian pranikah",
  },
  {
    id: "labor",
    icon: "👷",
    title: "Hukum Ketenagakerjaan",
    laws: ["UU No. 13/2003", "UU Cipta Kerja", "PP No. 35/2021"],
    topics: "PKWT/PKWTT, PHK, pesangon, BPJS, jam kerja, lembur, cuti, THR",
  },
  {
    id: "company",
    icon: "🏢",
    title: "Hukum Perusahaan",
    laws: ["UU No. 40/2007", "PP No. 8/2021", "UU Cipta Kerja"],
    topics: "Pendirian PT/CV, anggaran dasar, RUPS, NIB, OSS, KBLI",
  },
  {
    id: "criminal",
    icon: "🔒",
    title: "Hukum Pidana",
    laws: ["KUHP Baru (UU 1/2023)", "KUHAP", "UU ITE"],
    topics: "Tindak pidana, proses peradilan, hak tersangka, penahanan",
  },
  {
    id: "consumer",
    icon: "🛡️",
    title: "Perlindungan Konsumen",
    laws: ["UU No. 8/1999", "PP No. 80/2019"],
    topics: "Hak konsumen, BPSK, e-commerce, pengaduan",
  },
  {
    id: "privacy",
    icon: "🔐",
    title: "Perlindungan Data Pribadi",
    laws: ["UU PDP No. 27/2022"],
    topics: "Data pribadi, consent, hak subjek data, notifikasi pelanggaran",
  },
  {
    id: "property",
    icon: "🏠",
    title: "Hukum Properti & Tanah",
    laws: ["UUPA No. 5/1960", "PP No. 24/1997"],
    topics: "SHM, HGB, AJB, PPAT, BPN, pajak properti, balik nama",
  },
];

const PROCEDURES: ProcedureItem[] = [
  {
    id: "divorce",
    icon: "💔",
    title: "Prosedur Perceraian",
    title_en: "Divorce Procedure",
    steps: 12,
    timeline: "3-6 bulan",
    description: "Langkah lengkap cerai gugat, cerai talak, mediasi wajib, hingga akta cerai",
  },
  {
    id: "company",
    icon: "🏢",
    title: "Pendirian PT",
    title_en: "Company Formation",
    steps: 8,
    timeline: "2-4 minggu",
    description: "AHU Online, notaris, SK Kemenkumham, NPWP, OSS/NIB",
  },
  {
    id: "employment",
    icon: "⚖️",
    title: "Perselisihan Ketenagakerjaan",
    title_en: "Employment Dispute",
    steps: 4,
    timeline: "1-6 bulan",
    description: "Bipartit → Tripartit (Mediasi/Konsiliasi) → PHI → Kasasi",
  },
  {
    id: "consumer",
    icon: "🛡️",
    title: "Pengaduan Konsumen",
    title_en: "Consumer Complaint",
    steps: 6,
    timeline: "21 hari - 3 bulan",
    description: "Pengaduan langsung → BPSK (gratis) → PN → Kasasi",
  },
  {
    id: "property",
    icon: "🏠",
    title: "Transaksi Jual Beli Properti",
    title_en: "Property Transaction",
    steps: 9,
    timeline: "1-3 bulan",
    description: "Due diligence → PPJB → Pajak → AJB di PPAT → Balik Nama BPN",
  },
];

const POPULAR_FAQ: FAQItem[] = [
  {
    q: "Berapa biaya cerai di Indonesia?",
    a: "Biaya perkara di Pengadilan Agama sekitar Rp 300.000 - 1.000.000. Jika menggunakan pengacara, tambahan Rp 5.000.000 - 50.000.000 tergantung kompleksitas. Proses biasanya 3-6 bulan.",
  },
  {
    q: "Apa beda cerai gugat dan cerai talak?",
    a: "Cerai gugat diajukan oleh istri (penggugat vs tergugat), cerai talak diajukan oleh suami (pemohon vs termohon). Keduanya diajukan ke Pengadilan Agama untuk Muslim. Hak-hak pasca cerai berbeda (mut'ah, iddah hanya ada di cerai talak).",
  },
  {
    q: "Berapa biaya mendirikan PT?",
    a: "PT biasa: Rp 5.000.000 - 15.000.000 (termasuk notaris, AHU, NPWP, OSS). PT Perorangan: Rp 250.000 - 500.000 via AHU Online. Modal dasar minimum Rp 50.000.000, modal disetor minimum 25%.",
  },
  {
    q: "Apa hak pekerja yang di-PHK?",
    a: "Pesangon (max 9 bulan gaji), UPMK (max 10 bulan gaji), dan uang penggantian hak (cuti, ongkos pulang, dll). Besaran tergantung masa kerja dan alasan PHK. Diatur UU 13/2003 dan PP 35/2021.",
  },
  {
    q: "Bagaimana cara membuat laporan polisi?",
    a: "Datangi Polsek/Polres terdekat, bawa KTP dan bukti. Buat laporan pengaduan (delik aduan) atau laporan polisi (delik biasa). Proses: pelaporan → BAP → penyelidikan → penyidikan. Gratis, tidak dipungut biaya. Dasar: KUHAP Pasal 108.",
  },
  {
    q: "Apa itu UU PDP dan dampaknya?",
    a: "UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi. Mengatur pengumpulan, pemrosesan, dan penyimpanan data pribadi. Sanksi pelanggaran: denda hingga 2% pendapatan tahunan dan pidana penjara. Berlaku penuh sejak Oktober 2024.",
  },
];

const GLOSSARY_PREVIEW = [
  { term: "Gugatan", en: "Lawsuit/Petition", def: "Tuntutan hak yang mengandung sengketa" },
  { term: "Somasi", en: "Demand Letter", def: "Teguran hukum resmi atas wanprestasi" },
  { term: "PHK", en: "Termination", def: "Pemutusan Hubungan Kerja" },
  { term: "Pesangon", en: "Severance Pay", def: "Uang kompensasi karena PHK" },
  { term: "PKWT", en: "Fixed-Term Contract", def: "Perjanjian Kerja Waktu Tertentu" },
  { term: "NIB", en: "Business ID Number", def: "Nomor Induk Berusaha (via OSS)" },
  { term: "AJB", en: "Deed of Sale", def: "Akta Jual Beli di hadapan PPAT" },
  { term: "BPHTB", en: "Land Transfer Tax", def: "Bea Perolehan Hak atas Tanah/Bangunan (5%)" },
  { term: "Hadhanah", en: "Child Custody", def: "Hak asuh anak di bawah 12 tahun" },
  { term: "Gono-Gini", en: "Marital Property", def: "Harta bersama selama perkawinan" },
  { term: "Inkracht", en: "Final & Binding", def: "Putusan berkekuatan hukum tetap" },
  { term: "Praperadilan", en: "Pre-trial Hearing", def: "Pemeriksaan keabsahan tindakan penyidik/penuntut" },
];

export default function KnowledgePage() {
  const [activeTab, setActiveTab] = useState<string>("laws");
  const [openFaq, setOpenFaq] = useState<number | null>(null);

  return (
    <main className="min-h-screen bg-gray-50">
      {/* Nav */}
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
              <a href="./templates" className="text-gray-600 hover:text-blue-700 text-sm font-medium">Template Dokumen</a>
              <a href="./knowledge" className="text-blue-700 text-sm font-bold">Basis Pengetahuan</a>
            </div>
            <button className="bg-blue-700 hover:bg-blue-800 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors">
              Daftar Gratis
            </button>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="pt-28 pb-12 px-4 bg-gradient-to-br from-indigo-50 via-white to-blue-50">
        <div className="max-w-7xl mx-auto text-center">
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-gray-900 mb-4">
            📚 Basis <span className="text-blue-700">Pengetahuan Hukum</span>
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto mb-8">
            Referensi hukum Indonesia lengkap — undang-undang, prosedur, glosarium, dan FAQ.
            Didukung 200+ istilah hukum bilingual dan 30+ undang-undang.
          </p>

          {/* Stats */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-3xl mx-auto">
            {[
              { value: "7", label: "Kategori Hukum" },
              { value: "5", label: "Panduan Prosedur" },
              { value: "200+", label: "Istilah Glosarium" },
              { value: "57+", label: "FAQ Terjawab" },
            ].map((s) => (
              <div key={s.label} className="bg-white rounded-xl p-4 border border-gray-200 shadow-sm">
                <div className="text-2xl font-bold text-blue-700">{s.value}</div>
                <div className="text-xs text-gray-500 mt-1">{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Tabs */}
      <section className="sticky top-16 z-40 bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex gap-1 overflow-x-auto py-2">
            {[
              { id: "laws", label: "📖 Referensi Hukum", count: 7 },
              { id: "procedures", label: "📋 Prosedur", count: 5 },
              { id: "glossary", label: "🔤 Glosarium", count: "200+" },
              { id: "faq", label: "❓ FAQ", count: "57+" },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex-shrink-0 px-4 py-2.5 rounded-lg text-sm font-medium transition-all ${
                  activeTab === tab.id
                    ? "bg-blue-700 text-white shadow-md"
                    : "text-gray-600 hover:bg-gray-100"
                }`}
              >
                {tab.label} ({tab.count})
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* Content */}
      <section className="py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          {/* Law References */}
          {activeTab === "laws" && (
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-2">Referensi Hukum Indonesia</h2>
              <p className="text-gray-600 mb-8">
                Database hukum komprehensif mencakup 30+ undang-undang dan peraturan Indonesia yang
                sering digunakan masyarakat.
              </p>
              <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {LAW_REFS.map((law) => (
                  <div
                    key={law.id}
                    className="bg-white rounded-xl border border-gray-200 p-6 hover:shadow-lg hover:border-blue-200 transition-all"
                  >
                    <div className="text-3xl mb-3">{law.icon}</div>
                    <h3 className="text-lg font-bold text-gray-900 mb-3">{law.title}</h3>
                    <div className="space-y-1 mb-4">
                      {law.laws.map((l) => (
                        <span
                          key={l}
                          className="inline-block text-xs bg-blue-50 text-blue-700 px-2 py-1 rounded mr-1 mb-1"
                        >
                          {l}
                        </span>
                      ))}
                    </div>
                    <p className="text-sm text-gray-500">{law.topics}</p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Procedures */}
          {activeTab === "procedures" && (
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-2">Panduan Prosedur Hukum</h2>
              <p className="text-gray-600 mb-8">
                Langkah-langkah detail untuk menyelesaikan masalah hukum umum di Indonesia,
                lengkap dengan estimasi waktu dan biaya.
              </p>
              <div className="space-y-4">
                {PROCEDURES.map((proc) => (
                  <div
                    key={proc.id}
                    className="bg-white rounded-xl border border-gray-200 p-6 hover:shadow-md hover:border-blue-200 transition-all"
                  >
                    <div className="flex items-start gap-4">
                      <span className="text-3xl flex-shrink-0">{proc.icon}</span>
                      <div className="flex-1">
                        <div className="flex items-center gap-3 mb-1">
                          <h3 className="text-lg font-bold text-gray-900">{proc.title}</h3>
                          <span className="text-xs text-gray-400 italic">{proc.title_en}</span>
                        </div>
                        <p className="text-sm text-gray-600 mb-3">{proc.description}</p>
                        <div className="flex gap-4">
                          <span className="text-xs bg-blue-50 text-blue-700 px-3 py-1 rounded-full">
                            📝 {proc.steps} langkah
                          </span>
                          <span className="text-xs bg-green-50 text-green-700 px-3 py-1 rounded-full">
                            ⏱️ {proc.timeline}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Glossary */}
          {activeTab === "glossary" && (
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-2">Glosarium Hukum Bilingual</h2>
              <p className="text-gray-600 mb-8">
                200+ istilah hukum Indonesia dengan terjemahan Bahasa Inggris dan definisi singkat.
                Membantu memahami istilah-istilah hukum yang sering ditemui.
              </p>
              <div className="bg-white rounded-xl border border-gray-200 overflow-hidden">
                <table className="w-full">
                  <thead>
                    <tr className="bg-gray-50 border-b border-gray-200">
                      <th className="text-left px-6 py-3 text-sm font-bold text-gray-700">
                        Istilah (Indonesia)
                      </th>
                      <th className="text-left px-6 py-3 text-sm font-bold text-gray-700">
                        English
                      </th>
                      <th className="text-left px-6 py-3 text-sm font-bold text-gray-700 hidden md:table-cell">
                        Definisi
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    {GLOSSARY_PREVIEW.map((item, i) => (
                      <tr
                        key={item.term}
                        className={`border-b border-gray-100 ${
                          i % 2 === 0 ? "bg-white" : "bg-gray-50/50"
                        }`}
                      >
                        <td className="px-6 py-3 text-sm font-medium text-gray-900">
                          {item.term}
                        </td>
                        <td className="px-6 py-3 text-sm text-blue-700">{item.en}</td>
                        <td className="px-6 py-3 text-sm text-gray-500 hidden md:table-cell">
                          {item.def}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
                <div className="px-6 py-4 bg-gray-50 border-t border-gray-200 text-center">
                  <p className="text-sm text-gray-500">
                    Menampilkan 12 dari 200+ istilah. Glosarium lengkap tersedia di aplikasi.
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* FAQ */}
          {activeTab === "faq" && (
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-2">Pertanyaan yang Sering Diajukan</h2>
              <p className="text-gray-600 mb-8">
                Jawaban atas pertanyaan hukum paling umum dari masyarakat Indonesia.
                Didukung rujukan undang-undang yang berlaku.
              </p>
              <div className="space-y-3 max-w-3xl">
                {POPULAR_FAQ.map((faq, index) => (
                  <div
                    key={index}
                    className="bg-white rounded-xl border border-gray-200 overflow-hidden"
                  >
                    <button
                      onClick={() => setOpenFaq(openFaq === index ? null : index)}
                      className="w-full text-left px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors"
                    >
                      <span className="font-medium text-gray-900 text-sm pr-4">{faq.q}</span>
                      <span
                        className={`text-gray-400 transition-transform flex-shrink-0 ${
                          openFaq === index ? "rotate-180" : ""
                        }`}
                      >
                        ▼
                      </span>
                    </button>
                    {openFaq === index && (
                      <div className="px-6 pb-4">
                        <p className="text-sm text-gray-600 leading-relaxed bg-blue-50 rounded-lg p-4">
                          {faq.a}
                        </p>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-4 bg-blue-700">
        <div className="max-w-4xl mx-auto text-center text-white">
          <h2 className="text-3xl font-bold mb-4">Ada Pertanyaan Hukum?</h2>
          <p className="text-blue-100 mb-8">
            AI Lawyer siap menjawab pertanyaan hukum Anda 24/7. Gratis, cepat, dan akurat.
          </p>
          <div className="flex flex-col sm:flex-row justify-center gap-4">
            <a
              href="./"
              className="inline-block bg-white text-blue-700 font-semibold px-8 py-3 rounded-xl hover:bg-blue-50 transition-colors"
            >
              💬 Tanya AI Lawyer
            </a>
            <a
              href="./templates"
              className="inline-block bg-blue-600 text-white font-semibold px-8 py-3 rounded-xl border border-blue-500 hover:bg-blue-500 transition-colors"
            >
              📄 Lihat Template
            </a>
          </div>
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
