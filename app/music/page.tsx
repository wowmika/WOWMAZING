export default function MusicPage() {
  const features = [
    ["🎧", "Offline Playback"],
    ["📂", "Smart Library"],
    ["❤️", "Favorites"],
    ["⬇️", "Built-in Downloads"],
    ["🎵", "Playlist Support"],
    ["⚡", "Ultra Fast"],
  ];

  const screenshots = [
    "/images/music/screen1.png",
    "/images/music/screen2.png",
    "/images/music/screen3.png",
    "/images/music/screen4.png",
  ];

  return (
    <main className="relative min-h-screen overflow-hidden bg-[#030712] text-white">

      {/* Background Glow */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute left-0 top-0 h-[420px] w-[420px] rounded-full bg-cyan-500/20 blur-[140px]" />
        <div className="absolute right-0 top-32 h-[350px] w-[350px] rounded-full bg-purple-600/20 blur-[140px]" />
        <div className="absolute bottom-0 left-1/2 h-[320px] w-[320px] -translate-x-1/2 rounded-full bg-blue-500/10 blur-[120px]" />
      </div>

      {/* HERO */}
      <section className="mx-auto max-w-7xl px-6 py-24 lg:px-10">
        <div className="grid items-center gap-16 lg:grid-cols-2">

          {/* Big App Image */}
          <div className="relative flex justify-center">
            <div className="absolute h-80 w-80 rounded-full bg-cyan-400/20 blur-[90px]" />

            <img
              src="/images/music/hero.png"
              alt="WOWMAZING Music"
              className="relative w-full max-w-[520px] rounded-[30px] border border-cyan-400/20 shadow-[0_0_80px_rgba(34,211,238,.25)] transition duration-500 hover:scale-105"
            />
          </div>

          {/* Text */}
          <div>
            <span className="rounded-full border border-cyan-400/30 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-300">
              Windows Desktop Application
            </span>

            <h1 className="mt-6 text-6xl font-black leading-none">
              WOWMAZING
              <span className="block bg-gradient-to-r from-cyan-300 to-purple-400 bg-clip-text text-transparent">
                Music
              </span>
            </h1>

            <p className="mt-8 text-lg leading-8 text-gray-300">
              A premium offline music player with playlists, lightning-fast
              downloads, beautiful library management and zero distractions.
            </p>

            {/* Buttons */}
            <div className="mt-10 flex flex-wrap gap-4">
              <a
                href="/WOWMAZING.exe"
                download
                className="rounded-2xl bg-gradient-to-r from-cyan-400 to-purple-500 px-8 py-4 font-bold text-black shadow-lg transition hover:scale-105"
              >
                ⬇ Download Free
              </a>

              <a
                href="https://github.com/wowmika/WOWMAZING"
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-2xl border border-white/20 px-8 py-4 font-semibold backdrop-blur transition hover:bg-white/10"
              >
                GitHub
              </a>
            </div>

            {/* Glass Stats */}
            <div className="mt-10 grid grid-cols-3 gap-4">
              {[
                ["1.0.0", "Version"],
                ["Windows", "Platform"],
                ["100%", "Free"],
              ].map(([value, label]) => (
                <div
                  key={label}
                  className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur"
                >
                  <p className="text-xs uppercase tracking-wider text-gray-400">
                    {label}
                  </p>
                  <h3 className="mt-2 text-xl font-bold">{value}</h3>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section className="mx-auto max-w-7xl px-6 py-20 lg:px-10">
        <div className="mb-12 text-center">
          <p className="font-semibold tracking-[0.35em] text-cyan-400">
            FEATURES
          </p>
          <h2 className="mt-4 text-5xl font-black">
            Everything you need
          </h2>
          <p className="mt-4 text-gray-400">
            Built for modern music lovers.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {features.map(([icon, title]) => (
            <div
              key={title}
              className="group rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur transition duration-300 hover:-translate-y-2 hover:border-cyan-400/50 hover:bg-white/10"
            >
              <div className="text-5xl">{icon}</div>

              <h3 className="mt-5 text-2xl font-bold">
                {title}
              </h3>

              <p className="mt-3 leading-7 text-gray-400">
                Experience smooth performance with an elegant desktop interface.
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* SCREENSHOTS */}
      <section className="mx-auto max-w-7xl px-6 py-20 lg:px-10">
        <div className="mb-12 text-center">
          <p className="font-semibold tracking-[0.35em] text-cyan-400">
            SCREENSHOTS
          </p>
          <h2 className="mt-4 text-5xl font-black">
            Designed to feel premium
          </h2>
          <p className="mt-4 text-gray-400">
            Every screen is crafted for clarity and speed.
          </p>
        </div>

        <div className="grid gap-8 md:grid-cols-2">
          {screenshots.map((img, i) => (
            <div
              key={i}
              className="group overflow-hidden rounded-3xl border border-white/10 bg-white/5 backdrop-blur"
            >
              <img
                src={img}
                alt={`WOWMAZING Screenshot ${i + 1}`}
                className="w-full transition duration-500 group-hover:scale-105"
              />

              <div className="border-t border-white/10 p-5">
                <p className="font-semibold">
                  Screen {i + 1}
                </p>
                <p className="text-sm text-gray-400">
                  Modern desktop experience
                </p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* DOWNLOAD CTA */}
      <section className="mx-auto max-w-5xl px-6 py-24">
        <div className="rounded-[36px] border border-cyan-400/20 bg-gradient-to-r from-cyan-500/10 to-purple-500/10 p-10 text-center backdrop-blur">
          <h2 className="text-4xl font-black">
            Ready to listen offline?
          </h2>

          <p className="mx-auto mt-4 max-w-2xl text-gray-300">
            Download WOWMAZING Music for Windows and enjoy a fast,
            distraction-free music experience completely free.
          </p>

          <a
            href="/WOWMAZING.exe"
            download
            className="mt-8 inline-block rounded-2xl bg-gradient-to-r from-cyan-400 to-purple-500 px-10 py-5 text-lg font-bold text-black transition hover:scale-105"
          >
            Download WOWMAZING v1.0
          </a>

          <div className="mt-6 flex justify-center gap-6 text-sm text-gray-400">
            <span>Windows 10/11</span>
            <span>•</span>
            <span>50 MB</span>
            <span>•</span>
            <span>Free Forever</span>
          </div>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="border-t border-white/10 py-10 text-center">
        <h3 className="text-2xl font-black">
          WOWMAZING Studios
        </h3>

        <p className="mt-3 text-gray-400">
          Premium software crafted in India.
        </p>

        <p className="mt-6 text-sm text-gray-500">
          © 2026 WOWMAZING Studios. All rights reserved.
        </p>
      </footer>
    </main>
  );
}