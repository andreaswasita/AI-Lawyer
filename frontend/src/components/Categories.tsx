export default function Categories() {
  const categories = [
    {
      icon: "💔",
      name: "Perceraian",
      description: "Gugatan cerai, talak, hak asuh anak, harta gono-gini",
      templates: 5,
      popular: true,
    },
    {
      icon: "🏢",
      name: "Bisnis & Perusahaan",
      description: "Pendirian PT/CV, NIB, SIUP, anggaran dasar",
      templates: 8,
      popular: true,
    },
    {
      icon: "👷",
      name: "Ketenagakerjaan",
      description: "Kontrak kerja, PHK, pesangon, hak pekerja",
      templates: 6,
      popular: true,
    },
    {
      icon: "📜",
      name: "Waris & Wasiat",
      description: "Pembagian warisan, surat wasiat, hibah",
      templates: 4,
    },
    {
      icon: "📋",
      name: "Kontrak & Perjanjian",
      description: "Kerjasama, NDA, MOU, sewa menyewa",
      templates: 10,
    },
    {
      icon: "🏠",
      name: "Properti & Tanah",
      description: "Jual beli tanah, sertifikat, sengketa properti",
      templates: 4,
    },
    {
      icon: "🛡️",
      name: "Perlindungan Konsumen",
      description: "Pengaduan, somasi, klaim garansi, refund",
      templates: 3,
    },
    {
      icon: "💡",
      name: "Kekayaan Intelektual",
      description: "Merek dagang, hak cipta, paten, lisensi",
      templates: 4,
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
            Pilih kategori masalah hukum Anda. AI kami akan memberikan 
            informasi yang relevan dan template dokumen yang sesuai.
          </p>
        </div>

        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {categories.map((cat) => (
            <div
              key={cat.name}
              className="bg-white rounded-2xl p-6 border border-gray-200 hover:border-blue-300 hover:shadow-md transition-all cursor-pointer group"
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
                  {cat.templates} template
                </span>
                <span className="text-blue-700 text-sm font-medium group-hover:translate-x-1 transition-transform">
                  Lihat →
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
