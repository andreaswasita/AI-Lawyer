export default function Pricing() {
  const plans = [
    {
      name: "Gratis",
      price: "Rp 0",
      period: "selamanya",
      description: "Mulai kenali hak hukum Anda",
      features: [
        "5 pertanyaan AI per hari",
        "3 template dokumen dasar",
        "Akses perpustakaan hukum",
        "Panduan hukum populer",
      ],
      cta: "Mulai Gratis",
      popular: false,
      color: "gray",
    },
    {
      name: "Pemula",
      price: "Rp 99.000",
      period: "/bulan",
      description: "Untuk kebutuhan hukum personal",
      features: [
        "Unlimited pertanyaan AI",
        "20 template dokumen",
        "1x konsultasi Advokat/bulan",
        "Download dokumen (.docx)",
        "Prioritas response AI",
        "Riwayat percakapan",
      ],
      cta: "Pilih Pemula",
      popular: false,
      color: "blue",
    },
    {
      name: "Profesional",
      price: "Rp 299.000",
      period: "/bulan",
      description: "Untuk profesional & freelancer",
      features: [
        "Semua fitur Pemula",
        "50+ template premium",
        "3x konsultasi Advokat/bulan",
        "AI review dokumen",
        "Template kustom",
        "Notifikasi peraturan baru",
        "Prioritas Advokat",
      ],
      cta: "Pilih Profesional",
      popular: true,
      color: "blue",
    },
    {
      name: "Bisnis",
      price: "Rp 999.000",
      period: "/bulan",
      description: "Untuk UMKM & startup",
      features: [
        "Semua fitur Profesional",
        "Akses tim (5 pengguna)",
        "Unlimited konsultasi Advokat",
        "API akses",
        "Bulk dokumen generation",
        "Account manager dedikasi",
        "SLA 24 jam",
        "Compliance dashboard",
      ],
      cta: "Pilih Bisnis",
      popular: false,
      color: "gray",
    },
  ];

  return (
    <section id="pricing" className="py-20 px-4 sm:px-6 lg:px-8 bg-white">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
            Harga <span className="text-blue-700">Transparan</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Tidak ada biaya tersembunyi. Mulai gratis, upgrade kapan saja.
            Hemat hingga 80% dibanding layanan hukum tradisional.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {plans.map((plan) => (
            <div
              key={plan.name}
              className={`relative rounded-2xl p-6 border-2 transition-all ${
                plan.popular
                  ? "border-blue-700 shadow-xl shadow-blue-700/10 scale-105"
                  : "border-gray-200 hover:border-blue-200"
              }`}
            >
              {plan.popular && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                  <span className="bg-blue-700 text-white text-xs font-bold px-4 py-1 rounded-full">
                    PALING POPULER
                  </span>
                </div>
              )}

              <div className="mb-6">
                <h3 className="text-xl font-bold text-gray-900">{plan.name}</h3>
                <p className="text-sm text-gray-500 mt-1">{plan.description}</p>
              </div>

              <div className="mb-6">
                <span className="text-3xl font-bold text-gray-900">
                  {plan.price}
                </span>
                <span className="text-gray-500 text-sm">{plan.period}</span>
              </div>

              <ul className="space-y-3 mb-8">
                {plan.features.map((feature) => (
                  <li
                    key={feature}
                    className="flex items-start gap-2 text-sm text-gray-600"
                  >
                    <span className="text-green-500 mt-0.5">✓</span>
                    <span>{feature}</span>
                  </li>
                ))}
              </ul>

              <button
                className={`w-full py-3 rounded-xl font-semibold text-sm transition-all ${
                  plan.popular
                    ? "bg-blue-700 hover:bg-blue-800 text-white shadow-lg shadow-blue-700/25"
                    : "bg-gray-100 hover:bg-gray-200 text-gray-900"
                }`}
              >
                {plan.cta}
              </button>
            </div>
          ))}
        </div>

        {/* Comparison with competitors */}
        <div className="mt-16 text-center">
          <div className="inline-block bg-blue-50 rounded-2xl p-6 max-w-2xl">
            <h3 className="font-bold text-lg text-blue-900 mb-2">
              💰 Bandingkan dengan Kompetitor
            </h3>
            <div className="grid grid-cols-3 gap-4 text-sm">
              <div>
                <div className="font-bold text-gray-900">Justika</div>
                <div className="text-gray-500">Rp 30.000/30 menit</div>
                <div className="text-xs text-gray-400">Per sesi</div>
              </div>
              <div>
                <div className="font-bold text-gray-900">Advokat Tradisional</div>
                <div className="text-gray-500">Rp 500.000-5.000.000</div>
                <div className="text-xs text-gray-400">Per konsultasi</div>
              </div>
              <div className="bg-blue-700 text-white rounded-xl p-3 -mt-1">
                <div className="font-bold">AI Lawyer</div>
                <div>Rp 0 - 99.000/bulan</div>
                <div className="text-xs text-blue-200">Unlimited AI + template</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
