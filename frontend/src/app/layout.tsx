import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "AI Lawyer - Hukum AI | Layanan Hukum Terjangkau untuk Indonesia",
  description:
    "Platform layanan hukum berbasis AI untuk warga Indonesia. Konsultasi hukum, template dokumen, dan jaringan Advokat berlisensi. Mulai dari GRATIS.",
  keywords: [
    "AI Lawyer",
    "Hukum AI",
    "konsultasi hukum online",
    "template dokumen hukum",
    "advokat online",
    "perceraian Indonesia",
    "pendirian PT",
    "hukum Indonesia",
    "legal tech Indonesia",
  ],
  openGraph: {
    title: "AI Lawyer - Hukum AI",
    description: "Layanan Hukum Terjangkau untuk Seluruh Indonesia 🇮🇩⚖️",
    locale: "id_ID",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="id">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
