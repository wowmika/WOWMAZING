export default function ReleasesPage() {
  return (
    <main className="relative min-h-screen overflow-hidden bg-[#02040b] text-white">
      {/* ========================================================= */}
      {/* FUTURISTIC BACKGROUND                                      */}
      {/* ========================================================= */}

      <div className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
        <div className="absolute left-[-120px] top-[-100px] h-[420px] w-[420px] rounded-full bg-cyan-400/10 blur-[140px]" />

        <div className="absolute right-[-120px] top-[20%] h-[420px] w-[420px] rounded-full bg-purple-500/10 blur-[140px]" />

        <div className="absolute bottom-[-140px] left-[35%] h-[400px] w-[400px] rounded-full bg-blue-500/10 blur-[140px]" />

        <div className="absolute inset-0 opacity-[0.035] [background-image:linear-gradient(rgba(255,255,255,0.7)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.7)_1px,transparent_1px)] [background-size:72px_72px]" />
      </div>

      {/* ========================================================= */}
      {/* HEADER                                                      */}
      {/* ========================================================= */}

      <section className="mx-auto max-w-7xl px-6 pb-16 pt-24 lg:px-10">
        <div className="max-w-4xl">
          <div className="inline-flex items-center gap-3 rounded-full border border-cyan-400/20 bg-cyan-400/5 px-4 py-2 text-xs font-semibold tracking-[0.3em] text-cyan-300">
            RELEASE CENTER
          </div>

          <h1 className="mt-7 text-6xl font-black tracking-[-0.04em] sm:text-7xl">
            Software.
            <br />
            <span className="bg-gradient-to-r from-cyan-300 via-sky-400 to-purple-500 bg-clip-text text-transparent">
              Shipped.
            </span>
          </h1>

          <p className="mt-7 max-w-2xl text-lg leading-8 text-gray-400">
            Follow every WOWMAZING release, update and product milestone from
            one futuristic command center.
          </p>
        </div>
      </section>

      {/* ========================================================= */}
      {/* LATEST RELEASE                                             */}
      {/* ========================================================= */}

      <section className="mx-auto max-w-7xl px-6 pb-20 lg:px-10">
        <div className="relative overflow-hidden rounded-[36px] border border-cyan-400/20 bg-gradient-to-br from-cyan-400/[0.08] via-white/[0.03] to-purple-500/[0.08] p-8 backdrop-blur-2xl sm:p-10">
          <div className="absolute -right-24 -top-24 h-72 w-72 rounded-full bg-cyan-400/10 blur-[100px]" />

          <div className="relative">
            <div className="flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between">
              <div className="flex flex-wrap items-center gap-3">
                <span className="rounded-full bg-emerald-400/10 px-3 py-1 text-xs font-semibold tracking-[0.18em] text-emerald-300">
                  LATEST RELEASE
                </span>

                <span className="rounded-full border border-white/10 bg-white/[0.03] px-3 py-1 text-xs text-gray-400">
                  v1.0.0
                </span>
              </div>

              <span className="font-mono text-xs text-gray-600">
                WOWMAZING MUSIC
              </span>
            </div>

            <div className="mt-10 grid gap-12 lg:grid-cols-[1fr_0.8fr]">
              {/* Product information */}
              <div>
                <div className="text-5xl">🎵</div>

                <p className="mt-6 text-xs font-semibold tracking-[0.3em] text-cyan-400">
                  WINDOWS DESKTOP APPLICATION
                </p>

                <h2 className="mt-4 text-4xl font-black sm:text-5xl">
                  WOWMAZING Music
                </h2>

                <p className="mt-5 max-w-2xl text-lg leading-8 text-gray-400">
                  A premium offline music player built around local playback,
                  playlists, downloads and a distraction-free interface.
                </p>

                <div className="mt-8 flex flex-wrap gap-3">
                  <span className="rounded-full border border-white/10 bg-white/[0.03] px-4 py-2 text-xs text-gray-400">
                    Windows 10 / 11
                  </span>

                  <span className="rounded-full border border-white/10 bg-white/[0.03] px-4 py-2 text-xs text-gray-400">
                    50 MB
                  </span>

                  <span className="rounded-full border border-white/10 bg-white/[0.03] px-4 py-2 text-xs text-gray-400">
                    Free
                  </span>
                </div>

                <div className="mt-10 flex flex-wrap gap-4">
                  <a
                    href="/WOWMAZING.exe"
                    download
                    className="rounded-2xl bg-gradient-to-r from-cyan-400 to-purple-500 px-7 py-4 font-bold text-black transition hover:-translate-y-1 hover:shadow-[0_0_45px_rgba(34,211,238,0.22)]"
                  >
                    Download v1.0.0
                  </a>

                  <a
                    href="https://github.com/wowmika/WOWMAZING"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="rounded-2xl border border-white/10 bg-white/[0.03] px-7 py-4 font-semibold transition hover:border-cyan-400/30 hover:bg-white/[0.06]"
                  >
                    View Source
                  </a>
                </div>
              </div>

              {/* Release stats */}
              <div className="grid content-start gap-4 sm:grid-cols-2">
                <div className="rounded-3xl border border-white/10 bg-black/20 p-6">
                  <p className="text-[10px] tracking-[0.25em] text-gray-600">
                    VERSION
                  </p>

                  <p className="mt-3 text-3xl font-black">
                    1.0.0
                  </p>
                </div>

                <div className="rounded-3xl border border-white/10 bg-black/20 p-6">
                  <p className="text-[10px] tracking-[0.25em] text-gray-600">
                    PLATFORM
                  </p>

                  <p className="mt-3 text-3xl font-black">
                    Windows
                  </p>
                </div>

                <div className="rounded-3xl border border-white/10 bg-black/20 p-6">
                  <p className="text-[10px] tracking-[0.25em] text-gray-600">
                    FILE SIZE
                  </p>

                  <p className="mt-3 text-3xl font-black">
                    50 MB
                  </p>
                </div>

                <div className="rounded-3xl border border-white/10 bg-black/20 p-6">
                  <p className="text-[10px] tracking-[0.25em] text-gray-600">
                    STATUS
                  </p>

                  <p className="mt-3 text-3xl font-black text-emerald-300">
                    LIVE
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ========================================================= */}
      {/* CHANGELOG                                                   */}
      {/* ========================================================= */}

      <section className="mx-auto max-w-7xl px-6 pb-20 lg:px-10">
        <div className="grid gap-8 lg:grid-cols-[0.75fr_1.25fr]">
          <div>
            <p className="text-xs font-semibold tracking-[0.3em] text-cyan-400">
              CHANGELOG
            </p>

            <h2 className="mt-4 text-4xl font-black">
              What&apos;s new
            </h2>

            <p className="mt-4 leading-7 text-gray-500">
              The first public release of the WOWMAZING Music ecosystem.
            </p>
          </div>

          <div className="rounded-3xl border border-white/10 bg-white/[0.025] p-7 backdrop-blur-xl">
            <div className="flex items-center justify-between border-b border-white/10 pb-5">
              <div>
                <h3 className="text-xl font-bold">
                  WOWMAZING Music
                </h3>

                <p className="mt-1 text-xs text-gray-600">
                  Version 1.0.0
                </p>
              </div>

              <span className="rounded-full bg-cyan-400/10 px-3 py-1 text-xs text-cyan-300">
                INITIAL
              </span>
            </div>

            <div className="mt-6 space-y-4">
              {[
                "Offline music playback",
                "Smart local music library",
                "Playlist support",
                "Favorite songs",
                "Built-in downloads",
                "Modern dark desktop interface",
                "Windows desktop distribution",
              ].map((item) => (
                <div
                  key={item}
                  className="flex items-center gap-3 text-sm text-gray-400"
                >
                  <span className="text-emerald-300">✓</span>
                  {item}
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ========================================================= */}
      {/* ROADMAP                                                     */}
      {/* ========================================================= */}

      <section className="mx-auto max-w-7xl px-6 pb-24 lg:px-10">
        <div className="rounded-[36px] border border-white/10 bg-white/[0.02] p-8 backdrop-blur-xl sm:p-10">
          <div className="flex flex-col justify-between gap-6 md:flex-row md:items-end">
            <div>
              <p className="text-xs font-semibold tracking-[0.3em] text-purple-400">
                NEXT
              </p>

              <h2 className="mt-4 text-4xl font-black">
                What&apos;s coming
              </h2>
            </div>

            <p className="max-w-md text-sm leading-7 text-gray-500">
              The ecosystem is just getting started. More software,
              intelligence and interactive experiences are in development.
            </p>
          </div>

          <div className="mt-10 grid gap-4 md:grid-cols-3">
            {[
              ["02", "WOWMAZING AI", "AI productivity tools", "PLANNED"],
              ["03", "CodeForge", "Developer utilities", "IN DEVELOPMENT"],
              ["04", "Future Games", "Original indie experiences", "EXPLORING"],
            ].map(([num, title, desc, status]) => (
              <div
                key={num}
                className="rounded-3xl border border-white/10 bg-black/20 p-6 transition hover:border-purple-400/20 hover:bg-white/[0.03]"
              >
                <div className="flex items-center justify-between">
                  <span className="font-mono text-xs text-gray-600">
                    {num}
                  </span>

                  <span className="text-[9px] tracking-[0.2em] text-gray-600">
                    {status}
                  </span>
                </div>

                <h3 className="mt-10 text-xl font-black">
                  {title}
                </h3>

                <p className="mt-2 text-sm text-gray-500">
                  {desc}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ========================================================= */}
      {/* FOOTER                                                      */}
      {/* ========================================================= */}

      <footer className="border-t border-white/10">
        <div className="mx-auto flex max-w-7xl flex-col gap-5 px-6 py-10 text-sm text-gray-600 md:flex-row md:items-center md:justify-between lg:px-10">
          <div>
            <p className="font-black tracking-[0.16em] text-white">
              WOWMAZING
            </p>

            <p className="mt-1 text-[10px] tracking-[0.3em] text-cyan-400">
              STUDIOS
            </p>
          </div>

          <div className="flex flex-wrap gap-5">
            <a
              href="/"
              className="transition hover:text-cyan-300"
            >
              Home
            </a>

            <a
              href="/products"
              className="transition hover:text-cyan-300"
            >
              Products
            </a>

            <a
              href="/music"
              className="transition hover:text-cyan-300"
            >
              Music
            </a>

            <a
              href="https://github.com/wowmika/WOWMAZING"
              target="_blank"
              rel="noopener noreferrer"
              className="transition hover:text-cyan-300"
            >
              GitHub
            </a>
          </div>

          <p>© 2026 WOWMAZING Studios</p>
        </div>
      </footer>
    </main>
  );
}