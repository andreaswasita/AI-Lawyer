"use client";

import { useState } from "react";
import Hero from "@/components/Hero";
import ChatWidget from "@/components/ChatWidget";
import Features from "@/components/Features";
import Categories from "@/components/Categories";
import Pricing from "@/components/Pricing";
import Footer from "@/components/Footer";

export default function Home() {
  const [isChatOpen, setIsChatOpen] = useState(false);

  return (
    <main className="min-h-screen">
      {/* Navigation */}
      <nav className="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center gap-2">
              <span className="text-2xl"></span>
              <span className="font-bold text-xl text-blue-900">
                AI Lawyer
              </span>
              <span className="text-xs bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">
                BETA
              </span>
            </div>
            <div className="hidden md:flex items-center gap-8">
              <a href="#features" className="text-gray-600 hover:text-blue-700 text-sm font-medium">
                Fitur
              </a>
              <a href="#categories" className="text-gray-600 hover:text-blue-700 text-sm font-medium">
                Kategori Hukum
              </a>
              <a href="./templates" className="text-gray-600 hover:text-blue-700 text-sm font-medium">
                Template Dokumen
              </a>
              <a href="./knowledge" className="text-gray-600 hover:text-blue-700 text-sm font-medium">
                Basis Pengetahuan
              </a>
              <a href="#pricing" className="text-gray-600 hover:text-blue-700 text-sm font-medium">
                Harga
              </a>
            </div>
            <div className="flex items-center gap-3">
              <button className="text-sm text-gray-600 hover:text-blue-700 font-medium">
                Masuk
              </button>
              <button className="bg-blue-700 hover:bg-blue-800 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors">
                Daftar Gratis
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <Hero onStartChat={() => setIsChatOpen(true)} />

      {/* Features */}
      <Features />

      {/* Legal Categories */}
      <Categories />

      {/* Pricing */}
      <Pricing />

      {/* Footer */}
      <Footer />

      {/* Floating Chat Widget */}
      <ChatWidget isOpen={isChatOpen} onToggle={() => setIsChatOpen(!isChatOpen)} />
    </main>
  );
}
