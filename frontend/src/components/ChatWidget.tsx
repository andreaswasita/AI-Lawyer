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
  "Cara membuat surat wasiat?",
  "Template perjanjian kerjasama",
];

export default function ChatWidget({ isOpen, onToggle }: ChatWidgetProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "assistant",
      content:
        "Halo! 👋 Saya AI Lawyer, asisten hukum AI Anda.\n\n" +
        "Saya bisa membantu Anda dengan:\n" +
        "• 💬 Menjawab pertanyaan hukum\n" +
        "• 📄 Membuat dokumen hukum\n" +
        "• 👨‍⚖️ Menghubungkan dengan Advokat\n\n" +
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
      // Fallback demo response
      const aiMessage: Message = {
        id: `ai-${Date.now()}`,
        role: "assistant",
        content:
          `Terima kasih atas pertanyaan Anda: "${messageText}"\n\n` +
          "🤖 *Mode Demo* — Backend API belum terhubung.\n\n" +
          "Setelah API aktif, saya akan memberikan:\n" +
          "• Jawaban berdasarkan hukum Indonesia\n" +
          "• Rujukan undang-undang yang relevan\n" +
          "• Template dokumen yang sesuai\n" +
          "• Rekomendasi langkah selanjutnya\n\n" +
          "⚠️ Informasi umum, bukan nasihat hukum.",
        timestamp: new Date(),
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
        ⚖️
      </button>
    );
  }

  return (
    <div className="fixed bottom-6 right-6 z-50 w-[400px] h-[600px] bg-white rounded-2xl shadow-2xl border border-gray-200 flex flex-col overflow-hidden">
      {/* Header */}
      <div className="bg-blue-700 text-white p-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <span className="text-2xl">⚖️</span>
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
          ✕
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
                    {msg.triage.category} • {msg.triage.complexity}
                  </span>
                </div>
              )}
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-100 rounded-2xl rounded-bl-sm px-4 py-3">
              <div className="flex gap-1">
                <div className="typing-dot w-2 h-2 bg-gray-400 rounded-full"></div>
                <div className="typing-dot w-2 h-2 bg-gray-400 rounded-full"></div>
                <div className="typing-dot w-2 h-2 bg-gray-400 rounded-full"></div>
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
          ⚠️ Informasi umum, bukan nasihat hukum
        </p>
      </div>
    </div>
  );
}
