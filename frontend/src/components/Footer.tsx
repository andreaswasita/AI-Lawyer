export default function Footer() {
  return (
    <footer className="bg-gray-900 text-gray-400 py-16 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <div className="grid md:grid-cols-4 gap-12">
          {/* Brand */}
          <div>
            <div className="flex items-center gap-2 mb-4">
              <span className="text-2xl">{"\u2696\uFE0F"}</span>
              <span className="font-bold text-xl text-white">AI Lawyer</span>
            </div>
            <p className="text-sm leading-relaxed">
              Platform layanan hukum berbasis AI untuk warga Indonesia.
              Membuat hukum lebih mudah diakses oleh semua orang.
            </p>
            <div className="flex gap-4 mt-4">
              <a href="#" className="hover:text-white transition-colors">Instagram</a>
              <a href="#" className="hover:text-white transition-colors">Twitter</a>
              <a href="#" className="hover:text-white transition-colors">LinkedIn</a>
            </div>
          </div>

          {/* Layanan */}
          <div>
            <h4 className="font-bold text-white mb-4">Layanan</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="./" className="hover:text-white transition-colors">AI Chatbot Hukum</a></li>
              <li><a href="./templates" className="hover:text-white transition-colors">Template Dokumen (23)</a></li>
              <li><a href="./knowledge" className="hover:text-white transition-colors">Basis Pengetahuan</a></li>
              <li><a href="#pricing" className="hover:text-white transition-colors">Konsultasi Advokat</a></li>
              <li><a href="./templates" className="hover:text-white transition-colors">Pendirian PT/CV</a></li>
            </ul>
          </div>

          {/* Kategori Hukum */}
          <div>
            <h4 className="font-bold text-white mb-4">Kategori Hukum</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="./templates" className="hover:text-white transition-colors">Perceraian & Keluarga</a></li>
              <li><a href="./templates" className="hover:text-white transition-colors">Bisnis & Perusahaan</a></li>
              <li><a href="./templates" className="hover:text-white transition-colors">Ketenagakerjaan</a></li>
              <li><a href="./templates" className="hover:text-white transition-colors">Properti & Tanah</a></li>
              <li><a href="./knowledge" className="hover:text-white transition-colors">Panduan Prosedur</a></li>
              <li><a href="./knowledge" className="hover:text-white transition-colors">Glosarium Hukum</a></li>
            </ul>
          </div>

          {/* Perusahaan */}
          <div>
            <h4 className="font-bold text-white mb-4">Perusahaan</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-white transition-colors">Tentang Kami</a></li>
              <li><a href="#features" className="hover:text-white transition-colors">Cara Kerja</a></li>
              <li><a href="#pricing" className="hover:text-white transition-colors">Harga</a></li>
              <li><a href="./knowledge" className="hover:text-white transition-colors">FAQ</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Syarat & Ketentuan</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Kebijakan Privasi</a></li>
              <li><a href="#" className="hover:text-white transition-colors">Hubungi Kami</a></li>
            </ul>
          </div>
        </div>

        {/* Disclaimer */}
        <div className="mt-12 pt-8 border-t border-gray-800">
          <div className="bg-gray-800 rounded-xl p-4 mb-8">
            <p className="text-xs text-gray-400 leading-relaxed">
              <strong className="text-gray-300">{"\u26A0\uFE0F"} Pemberitahuan Penting:</strong> AI Lawyer
              menyediakan informasi hukum umum dan layanan automasi dokumen. Platform ini BUKAN
              kantor hukum dan TIDAK memberikan nasihat hukum. Konten yang dihasilkan oleh AI
              bersifat informatif dan tidak menggantikan konsultasi dengan Advokat berlisensi.
              Untuk nasihat hukum yang mengikat secara hukum, silakan gunakan fitur konsultasi
              dengan Advokat mitra kami yang terdaftar di PERADI/KAI. Penggunaan platform ini
              tunduk pada{" "}
              <a href="#" className="text-blue-400 hover:underline">
                Syarat dan Ketentuan
              </a>{" "}
              serta{" "}
              <a href="#" className="text-blue-400 hover:underline">
                Kebijakan Privasi
              </a>{" "}
              kami. Data Anda dilindungi sesuai UU PDP No. 27 Tahun 2022.
            </p>
          </div>

          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <p className="text-xs">
              {"\u00A9"} 2025 AI Lawyer (Hukum AI). Semua hak dilindungi undang-undang.
            </p>
            <div className="flex items-center gap-4 text-xs">
              <span>{"\uD83D\uDD12"} SSL Encrypted</span>
              <span>{"\uD83C\uDDEE\uD83C\uDDE9"} Server Indonesia</span>
              <span>{"\uD83D\uDCCB"} UU PDP Compliant</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
