"use client";

import { useState, useRef, useEffect } from "react";

interface ChatWidgetProps {
  isOpen: boolean;
  onToggle: () => void;
}

interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: Date;
  triage?: {
    category: string;
    complexity: string;
    recommendation: string;
  };
}

const SAMPLE_QUESTIONS = [
  "Bagaimana cara mengurus perceraian?",
  "Cara mendirikan PT di Indonesia?",
  "Hak pekerja saat di-PHK?",
  "Berapa biaya cerai?",
  "Template perjanjian sewa",
];

const KNOWLEDGE_RESPONSES: Record<string, { answer: string; triage: { category: string; complexity: string; recommendation: string } }> = {
  cerai: {
    answer:
      "Untuk mengurus perceraian di Indonesia:\n\n" +
      "1. Cerai Gugat (diajukan istri) atau Cerai Talak (diajukan suami)\n" +
      "2. Diajukan ke Pengadilan Agama (Muslim) atau Pengadilan Negeri (non-Muslim)\n" +
      "3. Mediasi wajib (PERMA 1/2016, max 30 hari)\n" +
      "4. Jika mediasi gagal, lanjut pemeriksaan & putusan\n\n" +
      "Biaya: Rp 300.000-1.000.000 (perkara) + Rp 5-50 juta (pengacara)\n" +
      "Waktu: 3-6 bulan\n\n" +
      "Dasar hukum: UU No. 1/1974, PP No. 9/1975, KHI Pasal 116\n\n" +
      "Kami punya 5 template perceraian siap pakai. Ketik 'template cerai' untuk melihat.",
    triage: { category: "Hukum Keluarga", complexity: "moderate", recommendation: "Template + Konsultasi" },
  },
  pt: {
    answer:
      "Prosedur mendirikan PT:\n\n" +
      "1. Pesan nama PT via AHU Online (Rp 200.000)\n" +
      "2. Buat Akta Pendirian di Notaris (Rp 2-10 juta)\n" +
      "3. Pengesahan SK Kemenkumham via AHU (Rp 1.580.000)\n" +
      "4. Daftar NPWP Perusahaan\n" +
      "5. Daftar OSS untuk NIB & perizinan\n\n" +
      "Modal dasar min Rp 50 juta, disetor min 25%\n" +
      "Total biaya: Rp 5-15 juta | Waktu: 2-4 minggu\n\n" +
      "PT Perorangan lebih murah: Rp 250-500 ribu via AHU Online\n\n" +
      "Dasar hukum: UU No. 40/2007, PP No. 8/2021",
    triage: { category: "Hukum Perusahaan", complexity: "complex", recommendation: "Template + Notaris" },
  },
  phk: {
    answer:
      "Hak pekerja yang di-PHK:\n\n" +
      "1. Pesangon: max 9 bulan gaji (tergantung masa kerja)\n" +
      "2. UPMK: max 10 bulan gaji\n" +
      "3. Uang Penggantian Hak: cuti, ongkos pulang, dll\n\n" +
      "Contoh masa kerja 5 tahun:\n" +
      "- Pesangon: 6 bulan gaji\n" +
      "- UPMK: 2 bulan gaji\n\n" +
      "PHK harus melalui perundingan bipartit dulu!\n" +
      "Jika gagal: mediasi Disnaker, lalu PHI.\n\n" +
      "Dasar hukum: UU No. 13/2003, PP No. 35/2021\n\n" +
      "Kami punya template Surat PHK dan kalkulator pesangon.",
    triage: { category: "Ketenagakerjaan", complexity: "complex", recommendation: "Konsultasi Advokat" },
  },
  sewa: {
    answer:
      "Template Perjanjian Sewa Menyewa tersedia!\n\n" +
      "Mencakup 12 pasal:\n" +
      "1. Objek Sewa (deskripsi, alamat, sertifikat)\n" +
      "2. Jangka Waktu\n" +
      "3. Harga & Pembayaran\n" +
      "4. Deposit/Uang Jaminan\n" +
      "5. Hak & Kewajiban\n" +
      "6. Larangan Penyewa\n" +
      "7. Pemeliharaan\n" +
      "8. Force Majeure\n" +
      "9. Penyelesaian Sengketa\n\n" +
      "Dasar hukum: KUHPerdata Pasal 1548-1600\n" +
      "Biaya: Rp 500.000-2.000.000 (jika lewat notaris)\n\n" +
      "Klik 'Lihat Template' di halaman Template Dokumen untuk mulai.",
    triage: { category: "Hukum Properti", complexity: "moderate", recommendation: "Template Self-Service" },
  },
};

function getSmartResponse(message: string): { answer: string; triage?: { category: string; complexity: string; recommendation: string } } {
  const lower = message.toLowerCase();

  if (lower.includes("cerai") || lower.includes("talak") || lower.includes("gugat") || lower.includes("perceraian")) {
    return KNOWLEDGE_RESPONSES.cerai;
  }
  if (lower.includes("pt") || lower.includes("perusahaan") || lower.includes("pendirian") || lower.includes("cv")) {
    return KNOWLEDGE_RESPONSES.pt;
  }
  if (lower.includes("phk") || lower.includes("pesangon") || lower.includes("dipecat") || lower.includes("pekerja")) {
    return KNOWLEDGE_RESPONSES.phk;
  }
  if (lower.includes("sewa") || lower.includes("kontrak") || lower.includes("perjanjian")) {
    return KNOWLEDGE_RESPONSES.sewa;
  }

  return {
    answer:
      `Terima kasih atas pertanyaan Anda tentang: "${message}"\n\n` +
      "Saya memiliki pengetahuan tentang:\n" +
      "\u2022 Hukum Keluarga (perceraian, waris, KDRT)\n" +
      "\u2022 Hukum Ketenagakerjaan (PHK, kontrak, pesangon)\n" +
      "\u2022 Hukum Perusahaan (pendirian PT, NIB, OSS)\n" +
      "\u2022 Hukum Properti (jual beli tanah, sewa)\n" +
      "\u2022 Hukum Pidana & Konsumen\n" +
      "\u2022 Perlindungan Data Pribadi (UU PDP)\n\n" +
      "23 template dokumen siap pakai di halaman Template Dokumen.\n" +
      "200+ istilah hukum di Basis Pengetahuan.\n\n" +
      "Silakan tanya lebih spesifik!",
  };
}

export default function ChatWidget({ isOpen, onToggle }: ChatWidgetProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "assistant",
      content:
        "Halo! \uD83D\uDC4B Saya AI Lawyer, asisten hukum AI Anda.\n\n" +
        "Saya bisa membantu Anda dengan:\n" +
        "\u2022 \uD83D\uDCAC Menjawab pertanyaan hukum Indonesia\n" +
        "\u2022 \uD83D\uDCC4 23 template dokumen hukum siap pakai\n" +
        "\u2022 \uD83D\uDCDA Referensi 30+ undang-undang\n" +
        "\u2022 \uD83D\uDC68\u200D\u2696\uFE0F Menghubungkan dengan Advokat\n\n" +
        "Silakan tanyakan apa saja tentang hukum Indonesia!",
      timestamp: new Date(),
    },
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async (text?: string) => {
    const messageText = text || input.trim();
    if (!messageText || isLoading) return;

    const userMessage: Message = {
      id: `user-${Date.now()}`,
      role: "user",
      content: messageText,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1"}/chat/`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            message: messageText,
            language: "id",
          }),
        }
      );

      if (response.ok) {
        const data = await response.json();
        const aiMessage: Message = {
          id: `ai-${Date.now()}`,
          role: "assistant",
          content: data.message,
          timestamp: new Date(),
          triage: data.triage,
        };
        setMessages((prev) => [...prev, aiMessage]);
      } else {
        throw new Error("API error");
      }
    } catch {
      // Smart demo response based on knowledge base
      const smartResp = getSmartResponse(messageText);
      const aiMessage: Message = {
        id: `ai-${Date.now()}`,
        role: "assistant",
        content: smartResp.answer,
        timestamp: new Date(),
        triage: smartResp.triage,
      };
      setMessages((prev) => [...prev, aiMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) {
    return (
      <button
        onClick={onToggle}
        className="fixed bottom-6 right-6 z-50 bg-blue-700 hover:bg-blue-800 text-white w-16 h-16 rounded-full shadow-lg shadow-blue-700/30 flex items-center justify-center text-2xl transition-all hover:scale-110"
        aria-label="Open AI Legal Chat"
      >
        {"\u2696\uFE0F"}
      </button>
    );
  }

  return (
    <div className="fixed bottom-6 right-6 z-50 w-[400px] h-[600px] bg-white rounded-2xl shadow-2xl border border-gray-200 flex flex-col overflow-hidden">
      {/* Header */}
      <div className="bg-blue-700 text-white p-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <span className="text-2xl">{"\u2696\uFE0F"}</span>
          <div>
            <h3 className="font-bold text-sm">AI Lawyer</h3>
            <p className="text-xs text-blue-200">Asisten Hukum AI Indonesia</p>
          </div>
        </div>
        <button
          onClick={onToggle}
          className="text-white/70 hover:text-white text-xl"
          aria-label="Close chat"
        >
          {"\u2715"}
        </button>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`chat-bubble flex ${
              msg.role === "user" ? "justify-end" : "justify-start"
            }`}
          >
            <div
              className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm ${
                msg.role === "user"
                  ? "bg-blue-700 text-white rounded-br-sm"
                  : "bg-gray-100 text-gray-800 rounded-bl-sm"
              }`}
            >
              <div className="whitespace-pre-wrap">{msg.content}</div>
              {msg.triage && (
                <div className="mt-2 pt-2 border-t border-gray-200/50 text-xs">
                  <span
                    className={`inline-block px-2 py-0.5 rounded-full ${
                      msg.triage.complexity === "simple"
                        ? "bg-green-100 text-green-700"
                        : msg.triage.complexity === "moderate"
                        ? "bg-yellow-100 text-yellow-700"
                        : "bg-red-100 text-red-700"
                    }`}
                  >
                    {msg.triage.category} {"\u2022"} {msg.triage.complexity}
                  </span>
                  <p className="mt-1 text-gray-500">
                    {"\u27A1\uFE0F"} {msg.triage.recommendation}
                  </p>
                </div>
              )}
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-100 rounded-2xl rounded-bl-sm px-4 py-3">
              <div className="flex gap-1">
                <div className="typing-dot w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                <div className="typing-dot w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: "0.1s" }}></div>
                <div className="typing-dot w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: "0.2s" }}></div>
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* Quick Questions */}
      {messages.length <= 1 && (
        <div className="px-4 pb-2">
          <p className="text-xs text-gray-400 mb-2">Pertanyaan populer:</p>
          <div className="flex flex-wrap gap-1">
            {SAMPLE_QUESTIONS.map((q) => (
              <button
                key={q}
                onClick={() => sendMessage(q)}
                className="text-xs bg-blue-50 text-blue-700 px-3 py-1.5 rounded-full hover:bg-blue-100 transition-colors"
              >
                {q}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Input */}
      <div className="p-4 border-t border-gray-200">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder="Ketik pertanyaan hukum Anda..."
            className="flex-1 border border-gray-200 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={isLoading}
          />
          <button
            onClick={() => sendMessage()}
            disabled={isLoading || !input.trim()}
            className="bg-blue-700 hover:bg-blue-800 disabled:bg-gray-300 text-white px-4 py-2.5 rounded-xl text-sm font-medium transition-colors"
          >
            Kirim
          </button>
        </div>
        <p className="text-[10px] text-gray-400 mt-2 text-center">
          {"\u26A0\uFE0F"} Informasi umum, bukan nasihat hukum
        </p>
      </div>
    </div>
  );
}
