export default function Categories() {
  const categories = [
    {
      icon: "\uD83D\uDC94",
      name: "Perceraian & Keluarga",
      description: "Gugatan cerai, talak, hak asuh anak, harta gono-gini, waris, wasiat",
      templates: 5,
      popular: true,
      href: "./templates",
    },
    {
      icon: "\uD83C\uDFE2",
      name: "Bisnis & Perusahaan",
      description: "Pendirian PT/CV, perjanjian kerjasama, NDA, surat kuasa, jual beli",
      templates: 5,
      popular: true,
      href: "./templates",
    },
    {
      icon: "\uD83D\uDC77",
      name: "Ketenagakerjaan",
      description: "Kontrak PKWT/PKWTT, PHK, pesangon, surat peringatan, resign",
      templates: 5,
      popular: true,
      href: "./templates",
    },
    {
      icon: "\uD83C\uDFE0",
      name: "Properti & Tanah",
      description: "Sewa menyewa, jual beli tanah, PPJB, surat kuasa jual",
      templates: 3,
      popular: false,
      href: "./templates",
    },
    {
      icon: "\u2696\uFE0F",
      name: "Umum & Pidana",
      description: "Somasi, surat pernyataan, pengaduan polisi, perdamaian",
      templates: 5,
      popular: false,
      href: "./templates",
    },
    {
      icon: "\uD83D\uDEE1\uFE0F",
      name: "Perlindungan Konsumen",
      description: "Pengaduan konsumen, BPSK, somasi, klaim refund",
      templates: 2,
      popular: false,
      href: "./knowledge",
    },
    {
      icon: "\uD83D\uDD12",
      name: "Data Pribadi & Privasi",
      description: "UU PDP, perlindungan data, consent, notifikasi pelanggaran",
      templates: 1,
      popular: false,
      href: "./knowledge",
    },
    {
      icon: "\uD83D\uDCDA",
      name: "Panduan Prosedur",
      description: "Step-by-step: perceraian, pendirian PT, sengketa kerja, jual beli properti",
      templates: 5,
      popular: true,
      href: "./knowledge",
    },
  ];

  return (
    <section id="categories" className="py-20 px-4 sm:px-6 lg:px-8 bg-gray-50">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Kategori <span className="text-blue-700">Hukum</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            23 template dokumen, 7 referensi hukum, 5 panduan prosedur, dan 200+ istilah glosarium.
            Pilih kategori yang sesuai kebutuhan Anda.
          </p>
        </div>

        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {categories.map((cat) => (
            <a
              key={cat.name}
              href={cat.href}
              className="bg-white rounded-2xl p-6 border border-gray-200 hover:border-blue-300 hover:shadow-md transition-all cursor-pointer group block"
            >
              <div className="flex items-start justify-between mb-4">
                <span className="text-3xl">{cat.icon}</span>
                {cat.popular && (
                  <span className="text-[10px] font-bold bg-red-50 text-red-600 px-2 py-1 rounded-full">
                    POPULER
                  </span>
                )}
              </div>
              <h3 className="text-lg font-bold text-gray-900 mb-2 group-hover:text-blue-700 transition-colors">
                {cat.name}
              </h3>
              <p className="text-sm text-gray-500 mb-4">{cat.description}</p>
              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-400">
                  {cat.templates} {cat.templates > 1 ? "item" : "item"}
                </span>
                <span className="text-blue-700 text-sm font-medium group-hover:translate-x-1 transition-transform">
                  Lihat &rarr;
                </span>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
