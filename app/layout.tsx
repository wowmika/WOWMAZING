import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://wowmazingstudios.com"),

  title: {
    default: "WOWMAZING Studios",
    template: "%s | WOWMAZING Studios",
  },

  description:
    "WOWMAZING Studios builds premium software, Windows applications, AI tools, indie games and digital experiences.",

  keywords: [
    "WOWMAZING",
    "WOWMAZING Studios",
    "Windows applications",
    "desktop software",
    "AI tools",
    "indie games",
    "developer tools",
  ],

  authors: [
    {
      name: "WOWMAZING Studios",
      url: "https://wowmazingstudios.com",
    },
  ],

  creator: "WOWMAZING Studios",

  openGraph: {
    type: "website",
    url: "https://wowmazingstudios.com",
    siteName: "WOWMAZING Studios",
    title: "WOWMAZING Studios",
    description:
      "Premium software, Windows applications, AI tools, indie games and digital experiences.",
  },

  twitter: {
    card: "summary_large_image",
    title: "WOWMAZING Studios",
    description:
      "Premium software, Windows applications, AI tools, indie games and digital experiences.",
  },

  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}