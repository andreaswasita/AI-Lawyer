"use client";

interface HeroProps {
  onStartChat: () => void;
}

export default function Hero({ onStartChat }: HeroProps) {
  return (
    <section className="relative pt-32 pb-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-blue-50 via-white to-red-50">
      <div className="max-w-7xl mx-auto">
        <div className="text-center max-w-4xl mx-auto">
          {/* Indonesian Flag Badge */}
          <div className="inline-flex items-center gap-2 bg-white border border-gray-200 rounded-full px-4 py-2 mb-8 shadow-sm">
            <span className="text-lg">🇮🇩</span>
            <span className="text-sm font-medium text-gray-700">
              Dibuat untuk Warga Indonesia
            </span>
          </div>

          {/* Main Headline */}
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-6">
            Bantuan Hukum
            <span className="text-blue-700"> AI </span>
            untuk
            <br />
            <span className="text-blue-700">Semua Orang</span>
          </h1>

          {/* Subheadline */}
          <p className="text-lg sm:text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
            Konsultasi hukum 24/7 dengan AI, template dokumen otomatis, dan 
            jaringan Advokat berlisensi. Mulai <strong>GRATIS</strong> — 
            hemat hingga 80% biaya hukum tradisional.
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
            <button
              onClick={onStartChat}
              className="w-full sm:w-auto bg-blue-700 hover:bg-blue-800 text-white font-semibold px-8 py-4 rounded-xl text-lg shadow-lg shadow-blue-700/25 transition-all hover:shadow-xl hover:shadow-blue-700/30 hover:-translate-y-0.5"
            >
              💬 Tanya AI Lawyer Gratis
            </button>
            <a
              href="#categories"
              className="w-full sm:w-auto bg-white hover:bg-gray-50 text-gray-700 font-semibold px-8 py-4 rounded-xl text-lg border border-gray-200 transition-all hover:border-gray-300"
            >
              📄 Lihat Template Dokumen
            </a>
          </div>

          {/* Trust Indicators */}
          <div className="flex flex-wrap items-center justify-center gap-8 text-sm text-gray-500">
            <div className="flex items-center gap-2">
              <span className="text-green-500">✓</span>
              <span>Gratis untuk Mulai</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-green-500">✓</span>
              <span>Bahasa Indonesia</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-green-500">✓</span>
              <span>Advokat Berlisensi PERADI/KAI</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-green-500">✓</span>
              <span>Data Terenkripsi</span>
            </div>
          </div>
        </div>

        {/* Stats */}
        <div className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-8 max-w-3xl mx-auto">
          {[
            { value: "24/7", label: "AI Tersedia" },
            { value: "50+", label: "Template Dokumen" },
            { value: "Rp 0", label: "Mulai Gratis" },
            { value: "80%", label: "Lebih Hemat" },
          ].map((stat) => (
            <div key={stat.label} className="text-center">
              <div className="text-2xl sm:text-3xl font-bold text-blue-700">
                {stat.value}
              </div>
              <div className="text-sm text-gray-500 mt-1">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Disclaimer */}
      <div className="mt-12 text-center">
        <p className="text-xs text-gray-400 max-w-2xl mx-auto">
          ⚠️ AI Lawyer menyediakan informasi hukum umum dan automasi dokumen. 
          Platform ini BUKAN kantor hukum dan TIDAK memberikan nasihat hukum. 
          Untuk nasihat hukum resmi, gunakan fitur konsultasi dengan Advokat berlisensi kami.
        </p>
      </div>
    </section>
  );
}
