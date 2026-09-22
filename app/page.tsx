"use client";

import { useEffect } from "react";
import Navbar from "./components/Navbar";

const products = [
  {
    number: "01",
    icon: "◈",
    title: "WOWMAZING Music",
    category: "DESKTOP APPLICATION",
    description:
      "A fast offline music experience with playlists, downloads and a smart local library.",
    href: "/music",
    accent: "cyan",
  },
  {
    number: "02",
    icon: "✦",
    title: "WOWMAZING AI",
    category: "INTELLIGENCE",
    description:
      "Next-generation AI utilities designed to make everyday work faster and smarter.",
    href: "#",
    accent: "purple",
  },
  {
    number: "03",
    icon: "⌁",
    title: "WOWMAZING Games",
    category: "INTERACTIVE",
    description:
      "Original indie experiences built around atmosphere, exploration and unforgettable worlds.",
    href: "#",
    accent: "pink",
  },
];

const capabilities = [
  {
    icon: "01",
    title: "DESIGN",
    description:
      "Interfaces engineered with a strong visual system, motion and clarity.",
  },
  {
    icon: "02",
    title: "ENGINEERING",
    description:
      "Modern software architecture focused on speed, reliability and scalability.",
  },
  {
    icon: "03",
    title: "EXPERIENCE",
    description:
      "Products designed to feel polished from the first click to the thousandth.",
  },
  {
    icon: "04",
    title: "VISION",
    description:
      "A growing ecosystem spanning apps, games, developer tools and learning.",
  },
];

const particles = Array.from({ length: 36 }, (_, i) => ({
  id: i,
  left: `${(i * 29) % 100}%`,
  top: `${(i * 47) % 100}%`,
  delay: `${(i % 9) * 0.7}s`,
  duration: `${5 + (i % 6)}s`,
}));

export default function HomePage() {
  useEffect(() => {
    const updatePointer = (event: PointerEvent) => {
      const x = `${event.clientX}px`;
      const y = `${event.clientY}px`;

      document.documentElement.style.setProperty("--mouse-x", x);
      document.documentElement.style.setProperty("--mouse-y", y);
    };

    window.addEventListener("pointermove", updatePointer);

    return () => {
      window.removeEventListener("pointermove", updatePointer);
    };
  }, []);

  return (
    <main className="relative min-h-screen overflow-hidden bg-[#02040b] text-white selection:bg-cyan-400 selection:text-black">
      {/* ========================================================= */}
      {/* GLOBAL FUTURISTIC BACKGROUND                              */}
      {/* ========================================================= */}

      <div className="pointer-events-none fixed inset-0 -z-20 overflow-hidden">
        {/* Base radial lighting */}
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_0%,rgba(34,211,238,0.10),transparent_30%),radial-gradient(circle_at_90%_15%,rgba(168,85,247,0.12),transparent_28%),radial-gradient(circle_at_50%_100%,rgba(59,130,246,0.08),transparent_30%)]" />

        {/* Aurora blobs */}
        <div className="aurora aurora-cyan absolute -left-32 top-10 h-[420px] w-[420px] rounded-full" />
        <div className="aurora aurora-purple absolute right-[-100px] top-[15%] h-[500px] w-[500px] rounded-full" />
        <div className="aurora aurora-blue absolute bottom-[-140px] left-[35%] h-[420px] w-[420px] rounded-full" />

        {/* Perspective grid */}
        <div className="absolute inset-x-[-20%] bottom-[-30%] h-[75%] [transform:perspective(900px)_rotateX(65deg)]">
          <div className="grid-plane h-full w-full" />
        </div>

        {/* Fine technical grid */}
        <div className="absolute inset-0 opacity-[0.035] [background-image:linear-gradient(rgba(255,255,255,0.5)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.5)_1px,transparent_1px)] [background-size:72px_72px]" />

        {/* Vignette */}
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_30%,rgba(2,4,11,0.55)_100%)]" />

        {/* Mouse spotlight */}
        <div className="mouse-spotlight absolute left-[var(--mouse-x)] top-[var(--mouse-y)] h-[520px] w-[520px] -translate-x-1/2 -translate-y-1/2 rounded-full" />
      </div>

      {/* ========================================================= */}
      {/* NAVBAR                                                     */}
      {/* ========================================================= */}

      <div className="relative z-50">
        <Navbar />
      </div>

      {/* ========================================================= */}
      {/* FLOATING PARTICLES                                         */}
      {/* ========================================================= */}

      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        {particles.map((particle) => (
          <span
            key={particle.id}
            className="particle"
            style={{
              left: particle.left,
              top: particle.top,
              animationDelay: particle.delay,
              animationDuration: particle.duration,
            }}
          />
        ))}
      </div>

      {/* ========================================================= */}
      {/* HERO                                                        */}
      {/* ========================================================= */}

      <section className="relative z-10 mx-auto max-w-7xl px-6 pb-24 pt-20 lg:px-10 lg:pt-28">
        <div className="grid items-center gap-16 lg:grid-cols-[1.15fr_0.85fr]">
          {/* Left side */}
          <div>
            <div className="inline-flex items-center gap-3 rounded-full border border-cyan-400/20 bg-cyan-400/5 px-4 py-2 text-xs font-semibold tracking-[0.25em] text-cyan-300 backdrop-blur-xl">
              <span className="status-dot" />
              FUTURE SOFTWARE STUDIO
            </div>

            <div className="mt-7 flex items-center gap-4 text-xs uppercase tracking-[0.3em] text-gray-500">
              <span>Apps</span>
              <span className="text-cyan-400">/</span>
              <span>Games</span>
              <span className="text-cyan-400">/</span>
              <span>AI</span>
              <span className="text-cyan-400">/</span>
              <span>Tools</span>
            </div>

            <h1 className="mt-6 max-w-6xl text-6xl font-black leading-[0.9] tracking-[-0.05em] sm:text-7xl lg:text-[92px]">
              <span className="block">BUILD</span>

              <span className="relative mt-2 block bg-gradient-to-r from-cyan-300 via-sky-400 to-purple-500 bg-clip-text text-transparent">
                TOMORROW.
              </span>

              <span className="mt-2 block text-white/90">TODAY.</span>
            </h1>

            <p className="mt-8 max-w-2xl text-lg leading-8 text-gray-400 sm:text-xl">
              WOWMAZING Studios creates premium software, immersive games,
              intelligent tools and next-generation digital experiences.
            </p>

            <div className="mt-10 flex flex-wrap gap-4">
              <a
                href="#ecosystem"
                className="group relative overflow-hidden rounded-2xl bg-gradient-to-r from-cyan-400 via-sky-400 to-purple-500 px-7 py-4 font-bold text-black shadow-[0_0_40px_rgba(34,211,238,0.15)] transition duration-300 hover:-translate-y-1 hover:shadow-[0_0_60px_rgba(34,211,238,0.25)]"
              >
                <span className="relative z-10">Explore Ecosystem</span>

                <span className="absolute inset-0 -translate-x-full bg-white/30 transition duration-500 group-hover:translate-x-full" />
              </a>

              <a
                href="https://github.com/wowmika/WOWMAZING"
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-2xl border border-white/10 bg-white/[0.03] px-7 py-4 font-semibold text-white backdrop-blur-xl transition duration-300 hover:-translate-y-1 hover:border-cyan-400/30 hover:bg-white/[0.06]"
              >
                View on GitHub
              </a>
            </div>

            {/* Micro stats */}
            <div className="mt-12 grid max-w-xl grid-cols-3 gap-3">
              {[
                ["04", "CATEGORIES"],
                ["01", "LIVE PRODUCT"],
                ["∞", "POSSIBILITIES"],
              ].map(([value, label]) => (
                <div
                  key={label}
                  className="glass-panel rounded-2xl p-4"
                >
                  <div className="text-2xl font-black text-white">{value}</div>
                  <div className="mt-1 text-[10px] tracking-[0.22em] text-gray-500">
                    {label}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Right side: futuristic system panel */}
          <div className="relative">
            <div className="absolute -inset-8 rounded-[40px] bg-cyan-400/5 blur-3xl" />

            <div className="relative rounded-[32px] border border-white/10 bg-white/[0.025] p-4 shadow-2xl backdrop-blur-2xl">
              <div className="rounded-[26px] border border-white/10 bg-[#060a14]/90 p-6">
                {/* Window controls */}
                <div className="flex items-center justify-between border-b border-white/10 pb-4">
                  <div className="flex items-center gap-2">
                    <span className="h-2.5 w-2.5 rounded-full bg-white/20" />
                    <span className="h-2.5 w-2.5 rounded-full bg-white/20" />
                    <span className="h-2.5 w-2.5 rounded-full bg-white/20" />
                  </div>

                  <div className="text-[10px] font-semibold tracking-[0.3em] text-gray-600">
                    WOWMAZING // SYSTEM
                  </div>
                </div>

                {/* System title */}
                <div className="mt-8">
                  <div className="font-mono text-xs text-cyan-400">
                    SYSTEM STATUS
                  </div>

                  <div className="mt-2 flex items-center justify-between">
                    <h2 className="text-3xl font-black tracking-tight">
                      ONLINE
                    </h2>

                    <div className="rounded-full border border-emerald-400/20 bg-emerald-400/5 px-3 py-1 text-[10px] font-semibold tracking-[0.2em] text-emerald-300">
                      NOMINAL
                    </div>
                  </div>
                </div>

                {/* Animated waveform */}
                <div className="mt-8 flex h-28 items-end gap-1.5 overflow-hidden rounded-2xl border border-white/10 bg-black/30 p-4">
                  {Array.from({ length: 42 }).map((_, i) => (
                    <span
                      key={i}
                      className="wave-bar"
                      style={{
                        animationDelay: `${i * 0.04}s`,
                        height: `${20 + ((i * 17) % 75)}%`,
                      }}
                    />
                  ))}
                </div>

                {/* Terminal-style text */}
                <div className="mt-6 space-y-3 rounded-2xl border border-white/10 bg-black/30 p-5 font-mono text-xs">
                  <div className="text-gray-600">
                    $ initialize wowmazing_core
                  </div>

                  <div className="text-cyan-300">
                    ✓ product engine loaded
                  </div>

                  <div className="text-purple-300">
                    ✓ creative systems online
                  </div>

                  <div className="text-emerald-300">
                    ✓ ecosystem ready
                  </div>

                  <div className="flex items-center text-gray-400">
                    <span>$</span>
                    <span className="ml-2 typing-cursor">
                      creating the future
                    </span>
                  </div>
                </div>

                {/* Status cards */}
                <div className="mt-5 grid grid-cols-2 gap-3">
                  <div className="rounded-2xl border border-white/10 bg-white/[0.03] p-4">
                    <div className="text-[10px] uppercase tracking-[0.2em] text-gray-600">
                      Core
                    </div>
                    <div className="mt-2 text-sm font-bold">OPERATIONAL</div>
                  </div>

                  <div className="rounded-2xl border border-white/10 bg-white/[0.03] p-4">
                    <div className="text-[10px] uppercase tracking-[0.2em] text-gray-600">
                      Future
                    </div>
                    <div className="mt-2 text-sm font-bold text-cyan-300">
                      EXPANDING
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Scroll indicator */}
        <div className="mt-20 flex items-center gap-4 text-[10px] uppercase tracking-[0.35em] text-gray-600">
          <div className="h-px w-16 bg-white/10" />
          Scroll to explore
          <span className="animate-pulse text-cyan-400">↓</span>
        </div>
      </section>

      {/* ========================================================= */}
      {/* ECOSYSTEM                                                  */}
      {/* ========================================================= */}

      <section
        id="ecosystem"
        className="relative z-10 mx-auto max-w-7xl px-6 py-24 lg:px-10"
      >
        <div className="flex flex-col justify-between gap-8 md:flex-row md:items-end">
          <div>
            <div className="text-xs font-semibold tracking-[0.35em] text-cyan-400">
              THE ECOSYSTEM
            </div>

            <h2 className="mt-4 max-w-3xl text-5xl font-black tracking-tight sm:text-6xl">
              One studio.
              <br />
              <span className="text-white/45">Many frontiers.</span>
            </h2>
          </div>

          <p className="max-w-sm text-sm leading-7 text-gray-500">
            Software products built to live at the intersection of technology,
            creativity and human experience.
          </p>
        </div>

        <div className="mt-14 grid gap-6 lg:grid-cols-3">
          {products.map((product) => (
            <a
              key={product.number}
              href={product.href}
              className="group futuristic-card relative overflow-hidden rounded-[30px] border border-white/10 bg-white/[0.035] p-7 backdrop-blur-xl"
            >
              {/* Glow */}
              <div
                className={`absolute -right-16 -top-16 h-40 w-40 rounded-full blur-3xl transition duration-500 group-hover:scale-150 ${
                  product.accent === "cyan"
                    ? "bg-cyan-400/10"
                    : product.accent === "purple"
                      ? "bg-purple-400/10"
                      : "bg-pink-400/10"
                }`}
              />

              <div className="relative">
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs tracking-[0.25em] text-gray-600">
                    {product.number}
                  </span>

                  <span className="text-2xl text-gray-500 transition duration-300 group-hover:text-cyan-300">
                    {product.icon}
                  </span>
                </div>

                <div className="mt-16">
                  <p className="text-[10px] font-semibold tracking-[0.3em] text-cyan-400">
                    {product.category}
                  </p>

                  <h3 className="mt-3 text-3xl font-black">
                    {product.title}
                  </h3>

                  <p className="mt-4 text-sm leading-7 text-gray-500">
                    {product.description}
                  </p>
                </div>

                <div className="mt-10 flex items-center justify-between border-t border-white/10 pt-5">
                  <span className="text-sm font-semibold text-white/80">
                    {product.href === "#" ? "Coming soon" : "Open product"}
                  </span>

                  <span className="text-cyan-300 transition duration-300 group-hover:translate-x-2">
                    →
                  </span>
                </div>
              </div>
            </a>
          ))}
        </div>
      </section>

      {/* ========================================================= */}
      {/* CAPABILITIES                                               */}
      {/* ========================================================= */}

      <section className="relative z-10 mx-auto max-w-7xl px-6 py-24 lg:px-10">
        <div className="rounded-[40px] border border-white/10 bg-gradient-to-br from-white/[0.06] to-white/[0.015] p-8 backdrop-blur-xl sm:p-12">
          <div className="grid gap-14 lg:grid-cols-[0.8fr_1.2fr]">
            <div>
              <p className="text-xs font-semibold tracking-[0.35em] text-cyan-400">
                HOW WE BUILD
              </p>

              <h2 className="mt-4 text-5xl font-black tracking-tight">
                Technology is the medium.
                <br />
                <span className="text-white/40">Experience is the goal.</span>
              </h2>

              <p className="mt-7 max-w-lg text-sm leading-7 text-gray-500">
                WOWMAZING Studios is building a long-term ecosystem of
                products rather than isolated projects.
              </p>
            </div>

            <div className="grid gap-4 sm:grid-cols-2">
              {capabilities.map((item) => (
                <div
                  key={item.icon}
                  className="group rounded-3xl border border-white/10 bg-black/20 p-6 transition duration-300 hover:-translate-y-1 hover:border-cyan-400/20 hover:bg-white/[0.04]"
                >
                  <div className="font-mono text-xs text-cyan-400">
                    / {item.icon}
                  </div>

                  <h3 className="mt-8 text-lg font-black tracking-[0.12em]">
                    {item.title}
                  </h3>

                  <p className="mt-3 text-sm leading-7 text-gray-500">
                    {item.description}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ========================================================= */}
      {/* FEATURED PRODUCT CTA                                       */}
      {/* ========================================================= */}

      <section className="relative z-10 mx-auto max-w-7xl px-6 py-24 lg:px-10">
        <div className="relative overflow-hidden rounded-[40px] border border-cyan-400/20 bg-gradient-to-r from-cyan-400/10 via-sky-400/5 to-purple-500/10 p-8 sm:p-12">
          <div className="absolute -right-20 -top-20 h-64 w-64 rounded-full bg-cyan-400/10 blur-3xl" />
          <div className="absolute -bottom-20 -left-20 h-64 w-64 rounded-full bg-purple-500/10 blur-3xl" />

          <div className="relative flex flex-col justify-between gap-10 lg:flex-row lg:items-end">
            <div>
              <p className="text-xs font-semibold tracking-[0.35em] text-cyan-300">
                FLAGSHIP PRODUCT
              </p>

              <h2 className="mt-4 max-w-3xl text-5xl font-black tracking-tight sm:text-6xl">
                Meet{" "}
                <span className="bg-gradient-to-r from-cyan-300 to-purple-400 bg-clip-text text-transparent">
                  WOWMAZING Music.
                </span>
              </h2>

              <p className="mt-6 max-w-2xl text-lg leading-8 text-gray-300">
                A premium Windows music experience designed around local
                playback, playlists, downloads and simplicity.
              </p>
            </div>

            <a
              href="/music"
              className="inline-flex shrink-0 items-center justify-center rounded-2xl bg-white px-7 py-4 font-bold text-black transition hover:-translate-y-1 hover:bg-cyan-300"
            >
              Explore Music →
            </a>
          </div>
        </div>
      </section>

      {/* ========================================================= */}
      {/* FINAL CTA                                                   */}
      {/* ========================================================= */}

      <section className="relative z-10 mx-auto max-w-5xl px-6 py-28 text-center">
        <p className="text-xs font-semibold tracking-[0.4em] text-cyan-400">
          THE NEXT CHAPTER
        </p>

        <h2 className="mt-5 text-5xl font-black tracking-tight sm:text-7xl">
          Something bigger
          <br />
          is{" "}
          <span className="bg-gradient-to-r from-cyan-300 via-sky-400 to-purple-500 bg-clip-text text-transparent">
            loading.
          </span>
        </h2>

        <p className="mx-auto mt-7 max-w-2xl text-lg leading-8 text-gray-500">
          WOWMAZING Studios is just getting started. Apps, games, intelligent
          tools and learning experiences are on the way.
        </p>

        <div className="mt-10 flex justify-center">
          <a
            href="/products"
            className="rounded-2xl border border-white/10 bg-white/[0.03] px-8 py-4 font-semibold backdrop-blur-xl transition hover:border-cyan-400/30 hover:bg-white/[0.06]"
          >
            View the ecosystem
          </a>
        </div>
      </section>

      {/* ========================================================= */}
      {/* FOOTER                                                      */}
      {/* ========================================================= */}

      <footer className="relative z-10 border-t border-white/10">
        <div className="mx-auto flex max-w-7xl flex-col gap-8 px-6 py-10 md:flex-row md:items-center md:justify-between lg:px-10">
          <div>
            <div className="text-xl font-black tracking-[0.15em]">
              WOWMAZING
            </div>

            <div className="mt-1 text-xs tracking-[0.35em] text-cyan-400">
              STUDIOS
            </div>
          </div>

          <div className="flex flex-wrap gap-6 text-sm text-gray-500">
            <a className="transition hover:text-cyan-300" href="/">
              Home
            </a>

            <a className="transition hover:text-cyan-300" href="/products">
              Products
            </a>

            <a className="transition hover:text-cyan-300" href="/music">
              Music
            </a>

            <a
              className="transition hover:text-cyan-300"
              href="https://github.com/wowmika/WOWMAZING"
              target="_blank"
              rel="noopener noreferrer"
            >
              GitHub
            </a>
          </div>

          <div className="text-xs text-gray-600">
            © 2026 WOWMAZING Studios
          </div>
        </div>
      </footer>

      {/* ========================================================= */}
      {/* ADVANCED ANIMATIONS                                        */}
      {/* ========================================================= */}

      <style jsx global>{`
        :root {
          --mouse-x: 50vw;
          --mouse-y: 50vh;
        }

        html {
          scroll-behavior: smooth;
        }

        body {
          background: #02040b;
        }

        .glass-panel {
          border: 1px solid rgba(255, 255, 255, 0.08);
          background: rgba(255, 255, 255, 0.025);
          backdrop-filter: blur(18px);
          -webkit-backdrop-filter: blur(18px);
        }

        .aurora {
          filter: blur(100px);
          opacity: 0.45;
          animation: auroraFloat 12s ease-in-out infinite alternate;
        }

        .aurora-cyan {
          background: radial-gradient(
            circle,
            rgba(34, 211, 238, 0.25),
            transparent 70%
          );
        }

        .aurora-purple {
          background: radial-gradient(
            circle,
            rgba(168, 85, 247, 0.22),
            transparent 70%
          );
          animation-delay: -4s;
        }

        .aurora-blue {
          background: radial-gradient(
            circle,
            rgba(59, 130, 246, 0.18),
            transparent 70%
          );
          animation-delay: -7s;
        }

        .grid-plane {
          background-image:
            linear-gradient(
              rgba(34, 211, 238, 0.18) 1px,
              transparent 1px
            ),
            linear-gradient(
              90deg,
              rgba(34, 211, 238, 0.18) 1px,
              transparent 1px
            );
          background-size: 70px 70px;
          mask-image: linear-gradient(
            to bottom,
            transparent 0%,
            black 18%,
            black 75%,
            transparent 100%
          );
          animation: gridMove 10s linear infinite;
        }

        .mouse-spotlight {
          background: radial-gradient(
            circle,
            rgba(34, 211, 238, 0.08),
            rgba(34, 211, 238, 0.025) 35%,
            transparent 70%
          );
        }

        .particle {
          position: absolute;
          display: block;
          width: 2px;
          height: 2px;
          border-radius: 9999px;
          background: rgba(103, 232, 249, 0.65);
          box-shadow: 0 0 10px rgba(34, 211, 238, 0.45);
          animation: particleFloat linear infinite;
        }

        .status-dot {
          width: 7px;
          height: 7px;
          border-radius: 9999px;
          background: #67e8f9;
          box-shadow:
            0 0 12px rgba(103, 232, 249, 0.9),
            0 0 24px rgba(103, 232, 249, 0.35);
          animation: pulseDot 1.8s ease-in-out infinite;
        }

        .wave-bar {
          flex: 1;
          min-width: 3px;
          border-radius: 999px;
          background: linear-gradient(
            to top,
            rgba(34, 211, 238, 0.2),
            rgba(34, 211, 238, 0.95)
          );
          animation: waveform 1.4s ease-in-out infinite alternate;
          transform-origin: bottom;
        }

        .typing-cursor {
          position: relative;
        }

        .typing-cursor::after {
          content: "";
          display: inline-block;
          width: 6px;
          height: 14px;
          margin-left: 5px;
          background: #67e8f9;
          vertical-align: -2px;
          animation: cursorBlink 0.9s steps(2) infinite;
        }

        .futuristic-card {
          transform-style: preserve-3d;
          transition:
            transform 0.4s ease,
            border-color 0.4s ease,
            box-shadow 0.4s ease;
        }

        .futuristic-card:hover {
          transform: translateY(-10px) rotateX(2deg) rotateY(-2deg);
          box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.35),
            0 0 40px rgba(34, 211, 238, 0.05);
        }

        @keyframes auroraFloat {
          0% {
            transform: translate3d(0, 0, 0) scale(1);
          }
          50% {
            transform: translate3d(35px, -20px, 0) scale(1.08);
          }
          100% {
            transform: translate3d(-20px, 25px, 0) scale(0.95);
          }
        }

        @keyframes gridMove {
          from {
            background-position: 0 0;
          }
          to {
            background-position: 0 70px;
          }
        }

        @keyframes particleFloat {
          0% {
            transform: translate3d(0, 20px, 0);
            opacity: 0;
          }
          20% {
            opacity: 0.8;
          }
          80% {
            opacity: 0.55;
          }
          100% {
            transform: translate3d(0, -120px, 0);
            opacity: 0;
          }
        }

        @keyframes pulseDot {
          0%,
          100% {
            transform: scale(1);
            opacity: 1;
          }
          50% {
            transform: scale(1.35);
            opacity: 0.65;
          }
        }

        @keyframes waveform {
          from {
            transform: scaleY(0.45);
            opacity: 0.5;
          }
          to {
            transform: scaleY(1);
            opacity: 1;
          }
        }

        @keyframes cursorBlink {
          0%,
          45% {
            opacity: 1;
          }
          46%,
          100% {
            opacity: 0;
          }
        }

        @media (prefers-reduced-motion: reduce) {
          *,
          *::before,
          *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            scroll-behavior: auto !important;
            transition-duration: 0.01ms !important;
          }
        }
      `}</style>
    </main>
  );
}