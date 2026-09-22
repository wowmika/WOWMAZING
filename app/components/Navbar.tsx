"use client";

import { useState } from "react";

export default function Navbar() {
  const [open, setOpen] = useState(false);

  const links = [
    { name: "Products", href: "#products" },
    { name: "Games", href: "#games" },
    { name: "About", href: "#about" },
    { name: "Contact", href: "#contact" },
  ];

  return (
    <nav className="sticky top-0 z-50 border-b border-white/10 bg-black/40 backdrop-blur-xl">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6 lg:px-8">
        {/* Logo */}
        <a href="#" className="group">
          <h1 className="text-2xl font-black tracking-wide transition group-hover:text-cyan-300">
            WOWMAZING
          </h1>
          <p className="text-xs tracking-[0.25em] text-cyan-400">
            STUDIOS
          </p>
        </a>

        {/* Desktop Menu */}
        <div className="hidden items-center gap-8 md:flex">
          {links.map((link) => (
            <a
              key={link.name}
              href={link.href}
              className="text-sm font-medium text-gray-300 transition hover:text-cyan-300"
            >
              {link.name}
            </a>
          ))}

          <button className="rounded-xl bg-gradient-to-r from-cyan-400 to-purple-500 px-5 py-2 font-semibold text-black transition hover:scale-105">
            Download
          </button>
        </div>

        {/* Mobile Button */}
        <button
          onClick={() => setOpen(!open)}
          className="rounded-lg border border-white/10 p-2 md:hidden"
        >
          {open ? "✕" : "☰"}
        </button>
      </div>

      {/* Mobile Menu */}
      {open && (
        <div className="border-t border-white/10 bg-black/90 md:hidden">
          <div className="mx-auto flex max-w-7xl flex-col px-6 py-5">
            {links.map((link) => (
              <a
                key={link.name}
                href={link.href}
                onClick={() => setOpen(false)}
                className="py-3 text-gray-300 transition hover:text-cyan-300"
              >
                {link.name}
              </a>
            ))}

            <button className="mt-4 rounded-xl bg-gradient-to-r from-cyan-400 to-purple-500 py-3 font-semibold text-black">
              Download WOWMAZING
            </button>
          </div>
        </div>
      )}
    </nav>
  );
}