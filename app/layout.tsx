import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  metadataBase: new URL("https://www.wowmazingstudios.com"),

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
      url: "https://www.wowmazingstudios.com",
    },
  ],

  creator: "WOWMAZING Studios",

  openGraph: {
    type: "website",
    url: "https://www.wowmazingstudios.com",
    siteName: "WOWMAZING Studios",
    title: "WOWMAZING Studios",
    description:
      "WOWMAZING Studios builds premium software, Windows applications, AI tools, indie games and digital experiences.",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: "WOWMAZING Studios",
      },
    ],
  },

  twitter: {
    card: "summary_large_image",
    title: "WOWMAZING Studios",
    description:
      "WOWMAZING Studios builds premium software, Windows applications, AI tools, indie games and digital experiences.",
    images: ["/og-image.png"],
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