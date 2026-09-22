"use client";

import { useEffect, useState } from "react";

const links = [
  { label: "Home", href: "/" },
  { label: "Ecosystem", href: "#ecosystem" },
  { label: "Products", href: "/products" },
  { label: "Music", href: "/music" },
  { label: "Releases", href: "/releases" },
];

const commands = [
  {
    label: "Open Home",
    description: "Return to the WOWMAZING homepage",
    href: "/",
    shortcut: "H",
  },
  {
    label: "Open Ecosystem",
    description: "Explore the studio ecosystem",
    href: "#ecosystem",
    shortcut: "E",
  },
  {
    label: "Open Products",
    description: "View all WOWMAZING products",
    href: "/products",
    shortcut: "P",
  },
  {
    label: "Open WOWMAZING Music",
    description: "Launch the music product page",
    href: "/music",
    shortcut: "M",
  },
];

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [commandOpen, setCommandOpen] = useState(false);
  const [query, setQuery] = useState("");

  useEffect(() => {
    const handleKeyboard = (event: KeyboardEvent) => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        setCommandOpen((open) => !open);
      }

      if (event.key === "Escape") {
        setCommandOpen(false);
        setMenuOpen(false);
      }
    };

    window.addEventListener("keydown", handleKeyboard);

    return () => {
      window.removeEventListener("keydown", handleKeyboard);
    };
  }, []);

  useEffect(() => {
    if (!commandOpen) {
      setQuery("");
    }
  }, [commandOpen]);

  const filteredCommands = commands.filter((command) =>
    `${command.label} ${command.description}`
      .toLowerCase()
      .includes(query.toLowerCase())
  );

  const goTo = (href: string) => {
    setCommandOpen(false);
    setMenuOpen(false);

    if (href.startsWith("#")) {
      const element = document.querySelector(href);

      if (element) {
        element.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    } else {
      window.location.href = href;
    }
  };

  return (
    <>
      {/* ========================================================= */}
      {/* NAVBAR                                                     */}
      {/* ========================================================= */}

      <header className="sticky top-0 z-[100] px-4 pt-4 sm:px-6">
        <div className="mx-auto max-w-7xl">
          <div className="navbar-shell relative overflow-hidden rounded-2xl border border-white/10 bg-[#050814]/70 px-4 py-3 shadow-2xl backdrop-blur-2xl sm:px-5">
            
            {/* Animated top light */}
            <div className="navbar-line pointer-events-none absolute inset-x-0 top-0 h-px" />

            <div className="flex items-center justify-between">
              {/* Brand */}
              <a
                href="/"
                className="group flex items-center gap-3"
                onClick={() => setMenuOpen(false)}
              >
                <div className="relative flex h-10 w-10 items-center justify-center overflow-hidden rounded-xl border border-cyan-400/20 bg-cyan-400/5">
                  <div className="absolute inset-0 bg-cyan-400/10 blur-xl transition duration-300 group-hover:bg-cyan-400/20" />

                  <span className="relative text-lg font-black text-cyan-300">
                    W
                  </span>
                </div>

                <div className="hidden sm:block">
                  <div className="text-sm font-black tracking-[0.16em] text-white">
                    WOWMAZING
                  </div>

                  <div className="text-[9px] tracking-[0.35em] text-cyan-400">
                    STUDIOS
                  </div>
                </div>
              </a>

              {/* Desktop Navigation */}
              <nav className="hidden items-center gap-1 md:flex">
                {links.map((link) => (
                  <a
                    key={link.label}
                    href={link.href}
                    className="nav-link rounded-xl px-4 py-2 text-sm text-gray-400 transition duration-300 hover:bg-white/5 hover:text-white"
                  >
                    {link.label}
                  </a>
                ))}
              </nav>

              {/* Right actions */}
              <div className="flex items-center gap-2">
                {/* System status */}
                <div className="hidden items-center gap-2 rounded-xl border border-emerald-400/10 bg-emerald-400/[0.04] px-3 py-2 lg:flex">
                  <span className="status-dot-small" />
                  <span className="text-[10px] font-semibold tracking-[0.15em] text-emerald-300">
                    ONLINE
                  </span>
                </div>

                {/* Command button */}
                <button
                  type="button"
                  onClick={() => setCommandOpen(true)}
                  className="hidden items-center gap-2 rounded-xl border border-white/10 bg-white/[0.03] px-3 py-2 text-gray-500 transition hover:border-cyan-400/20 hover:text-gray-300 sm:flex"
                  aria-label="Open command palette"
                >
                  <span className="text-xs">⌘</span>
                  <span className="text-xs">K</span>
                </button>

                {/* GitHub */}
                <a
                  href="https://github.com/wowmika/WOWMAZING"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hidden rounded-xl border border-white/10 bg-white/[0.03] px-4 py-2 text-sm font-semibold text-white transition hover:border-cyan-400/30 hover:bg-cyan-400/5 md:block"
                >
                  GitHub
                </a>

                {/* Mobile menu */}
                <button
                  type="button"
                  onClick={() => setMenuOpen((open) => !open)}
                  className="flex h-10 w-10 items-center justify-center rounded-xl border border-white/10 bg-white/[0.03] md:hidden"
                  aria-label="Toggle navigation"
                >
                  <div className="space-y-1.5">
                    <span
                      className={`block h-px w-5 bg-white transition ${
                        menuOpen ? "translate-y-2 rotate-45" : ""
                      }`}
                    />
                    <span
                      className={`block h-px w-5 bg-white transition ${
                        menuOpen ? "opacity-0" : ""
                      }`}
                    />
                    <span
                      className={`block h-px w-5 bg-white transition ${
                        menuOpen ? "-translate-y-2 -rotate-45" : ""
                      }`}
                    />
                  </div>
                </button>
              </div>
            </div>

            {/* Mobile navigation */}
            <div
              className={`overflow-hidden transition-all duration-300 md:hidden ${
                menuOpen ? "max-h-96 pt-4" : "max-h-0"
              }`}
            >
              <div className="border-t border-white/10 pt-3">
                <div className="grid gap-1">
                  {links.map((link) => (
                    <a
                      key={link.label}
                      href={link.href}
                      onClick={() => setMenuOpen(false)}
                      className="rounded-xl px-4 py-3 text-sm text-gray-400 transition hover:bg-white/5 hover:text-white"
                    >
                      {link.label}
                    </a>
                  ))}
                </div>

                <div className="mt-3 grid grid-cols-2 gap-2">
                  <button
                    type="button"
                    onClick={() => setCommandOpen(true)}
                    className="rounded-xl border border-white/10 bg-white/[0.03] px-4 py-3 text-sm text-gray-400"
                  >
                    Command
                  </button>

                  <a
                    href="https://github.com/wowmika/WOWMAZING"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="rounded-xl border border-white/10 bg-white/[0.03] px-4 py-3 text-center text-sm font-semibold"
                  >
                    GitHub
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* ========================================================= */}
      {/* COMMAND PALETTE                                           */}
      {/* ========================================================= */}

      {commandOpen && (
        <div
          className="fixed inset-0 z-[200] flex items-start justify-center bg-black/60 px-4 pt-[12vh] backdrop-blur-md"
          onMouseDown={() => setCommandOpen(false)}
        >
          <div
            className="command-window w-full max-w-2xl overflow-hidden rounded-3xl border border-white/10 bg-[#080c18]/95 shadow-[0_30px_100px_rgba(0,0,0,0.65)]"
            onMouseDown={(event) => event.stopPropagation()}
          >
            {/* Search */}
            <div className="border-b border-white/10 p-4">
              <div className="flex items-center gap-3">
                <span className="text-cyan-400">⌕</span>

                <input
                  autoFocus
                  value={query}
                  onChange={(event) => setQuery(event.target.value)}
                  placeholder="Search commands..."
                  className="w-full bg-transparent text-sm text-white outline-none placeholder:text-gray-600"
                />

                <kbd className="hidden rounded-lg border border-white/10 bg-white/5 px-2 py-1 text-[10px] text-gray-500 sm:block">
                  ESC
                </kbd>
              </div>
            </div>

            {/* Commands */}
            <div className="max-h-[55vh] overflow-y-auto p-2">
              {filteredCommands.length > 0 ? (
                filteredCommands.map((command) => (
                  <button
                    key={command.label}
                    type="button"
                    onClick={() => goTo(command.href)}
                    className="group flex w-full items-center justify-between rounded-2xl px-4 py-4 text-left transition hover:bg-white/[0.05]"
                  >
                    <div>
                      <div className="text-sm font-semibold text-white">
                        {command.label}
                      </div>

                      <div className="mt-1 text-xs text-gray-500">
                        {command.description}
                      </div>
                    </div>

                    <span className="rounded-lg border border-white/10 bg-white/[0.03] px-2 py-1 text-[10px] text-gray-500 group-hover:border-cyan-400/20 group-hover:text-cyan-300">
                      {command.shortcut}
                    </span>
                  </button>
                ))
              ) : (
                <div className="px-4 py-10 text-center text-sm text-gray-600">
                  No commands found.
                </div>
              )}
            </div>

            {/* Footer */}
            <div className="border-t border-white/10 px-4 py-3">
              <div className="flex items-center justify-between text-[10px] tracking-[0.15em] text-gray-600">
                <span>WOWMAZING COMMAND CENTER</span>
                <span>CTRL + K</span>
              </div>
            </div>
          </div>
        </div>
      )}

      <style jsx global>{`
        .navbar-shell {
          box-shadow:
            0 10px 50px rgba(0, 0, 0, 0.28),
            inset 0 1px 0 rgba(255, 255, 255, 0.025);
        }

        .navbar-line {
          background: linear-gradient(
            90deg,
            transparent,
            rgba(34, 211, 238, 0.8),
            rgba(168, 85, 247, 0.8),
            transparent
          );
          animation: navbarLine 5s linear infinite;
        }

        .status-dot-small {
          width: 6px;
          height: 6px;
          border-radius: 9999px;
          background: #6ee7b7;
          box-shadow:
            0 0 8px rgba(110, 231, 183, 0.8),
            0 0 18px rgba(110, 231, 183, 0.25);
          animation: statusPulse 1.8s ease-in-out infinite;
        }

        .command-window {
          animation: commandIn 0.18s ease-out;
        }

        @keyframes navbarLine {
          0% {
            transform: translateX(-100%);
          }

          50% {
            transform: translateX(100%);
          }

          100% {
            transform: translateX(100%);
          }
        }

        @keyframes statusPulse {
          0%,
          100% {
            opacity: 1;
            transform: scale(1);
          }

          50% {
            opacity: 0.55;
            transform: scale(1.35);
          }
        }

        @keyframes commandIn {
          from {
            opacity: 0;
            transform: translateY(-12px) scale(0.98);
          }

          to {
            opacity: 1;
            transform: translateY(0) scale(1);
          }
        }
      `}</style>
    </>
  );
}