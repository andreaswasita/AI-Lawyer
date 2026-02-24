export default function Features() {
  const features = [
    {
      icon: "🤖",
      title: "AI Chatbot 24/7",
      description:
        "Tanya apa saja tentang hukum Indonesia. AI kami menjawab dalam Bahasa Indonesia yang mudah dipahami, kapan saja.",
      badge: "GRATIS",
    },
    {
      icon: "📄",
      title: "Generator Dokumen",
      description:
        "Buat dokumen hukum otomatis — surat gugatan, kontrak kerja, perjanjian kerjasama, dan 50+ template lainnya.",
      badge: "AI-POWERED",
    },
    {
      icon: "👨‍⚖️",
      title: "Jaringan Advokat",
      description:
        "Terhubung langsung dengan Advokat berlisensi PERADI/KAI. Konsultasi via chat mulai Rp 69.000.",
      badge: "BERLISENSI",
    },
    {
      icon: "📚",
      title: "Perpustakaan Hukum",
      description:
        "Akses database lengkap UU, PP, Perpres, dan peraturan Indonesia. Selalu ter-update dengan peraturan terbaru.",
      badge: "LENGKAP",
    },
    {
      icon: "🎯",
      title: "Smart Triage",
      description:
        "AI menilai kompleksitas kasus Anda dan merekomendasikan: self-service, template, atau konsultasi Advokat.",
      badge: "UNIK",
    },
    {
      icon: "🔒",
      title: "Privasi & Keamanan",
      description:
        "Data Anda terenkripsi dan dilindungi sesuai UU PDP No. 27/2022. Server di Indonesia.",
      badge: "AMAN",
    },
  ];

  return (
    <section id="features" className="py-20 px-4 sm:px-6 lg:px-8 bg-white">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Semua yang Anda Butuhkan dalam
            <span className="text-blue-700"> Satu Platform</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Dari pertanyaan sederhana hingga kasus kompleks, AI Lawyer siap membantu
            dengan teknologi AI terdepan dan jaringan Advokat berpengalaman.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="relative bg-white border border-gray-200 rounded-2xl p-6 hover:shadow-lg hover:border-blue-200 transition-all group"
            >
              <span className="absolute top-4 right-4 text-[10px] font-bold bg-blue-50 text-blue-700 px-2 py-1 rounded-full">
                {feature.badge}
              </span>
              <div className="text-4xl mb-4">{feature.icon}</div>
              <h3 className="text-xl font-bold text-gray-900 mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600 text-sm leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
