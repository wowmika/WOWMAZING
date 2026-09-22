export default function MusicPage() {
  const features = [
    ["🎧", "Offline Playback"],
    ["📂", "Smart Music Library"],
    ["❤️", "Favorite Songs"],
    ["⬇️", "Built-in Downloads"],
    ["🎵", "Playlist Support"],
    ["⚡", "Fast & Lightweight"],
  ];

  return (
    <main className="min-h-screen bg-[#050816] text-white">
      {/* Hero */}
      <section className="mx-auto max-w-6xl px-8 py-20">
        <div className="grid items-center gap-14 lg:grid-cols-2">
          {/* App Artwork */}
          <div className="flex justify-center">
            <img
              src="/images/music/hero.png"
              alt="WOWMAZING Music"
              className="w-full max-w-sm rounded-[36px] border border-cyan-400/30 shadow-2xl"
            />
          </div>

          {/* Details */}
          <div>
            <span className="rounded-full bg-cyan-500/20 px-4 py-1 text-sm text-cyan-300">
              Windows Desktop App
            </span>

            <h1 className="mt-6 text-5xl font-black">
              WOWMAZING Music
            </h1>

            <p className="mt-6 text-lg leading-8 text-gray-400">
              A beautiful offline music player built for speed, playlists,
              downloads and a distraction-free listening experience.
            </p>

            {/* Buttons */}
            <div className="mt-8 flex flex-wrap gap-4">
              <a
                href="/WOWMAZING.exe"
                download
                className="rounded-xl bg-gradient-to-r from-cyan-400 to-purple-500 px-8 py-4 font-bold text-black transition hover:scale-105"
              >
                Download v1.0
              </a>

              <a
                href="https://github.com/wowmika/WOWMAZING"
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-xl border border-white/20 px-8 py-4 font-semibold transition hover:bg-white/10"
              >
                GitHub
              </a>
            </div>

            {/* Stats */}
            <div className="mt-8 grid grid-cols-3 gap-4">
              <div className="rounded-xl bg-white/5 p-4">
                <p className="text-sm text-gray-400">Version</p>
                <h3 className="mt-1 text-xl font-bold">1.0.0</h3>
              </div>

              <div className="rounded-xl bg-white/5 p-4">
                <p className="text-sm text-gray-400">Platform</p>
                <h3 className="mt-1 text-xl font-bold">Windows</h3>
              </div>

              <div className="rounded-xl bg-white/5 p-4">
                <p className="text-sm text-gray-400">Price</p>
                <h3 className="mt-1 text-xl font-bold">Free</h3>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="mx-auto max-w-6xl px-8 pb-20">
        <div className="mb-10">
          <p className="font-semibold tracking-[0.3em] text-cyan-400">
            FEATURES
          </p>

          <h2 className="mt-3 text-4xl font-black">
            Everything you need
          </h2>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {features.map(([icon, title]) => (
            <div
              key={title}
              className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur transition hover:border-cyan-400"
            >
              <div className="text-5xl">{icon}</div>

              <h3 className="mt-4 text-xl font-bold">{title}</h3>

              <p className="mt-2 text-gray-400">
                Designed for a premium offline music experience.
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* Screenshots */}
      <section className="mx-auto max-w-6xl px-8 pb-20">
        <div className="mb-10">
          <p className="font-semibold tracking-[0.3em] text-cyan-400">
            SCREENSHOTS
          </p>

          <h2 className="mt-3 text-4xl font-black">
            Beautiful modern interface
          </h2>
        </div>

        <div className="grid gap-6 md:grid-cols-2">
          <img
            src="/images/music/screen1.png"
            alt="Library Screen"
            className="rounded-2xl border border-white/10"
          />

          <img
            src="/images/music/screen2.png"
            alt="Player Screen"
            className="rounded-2xl border border-white/10"
          />
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/10 bg-black/20">
        <div className="mx-auto max-w-6xl px-8 py-10 text-center">
          <h3 className="text-2xl font-black">WOWMAZING Music</h3>

          <p className="mt-3 text-gray-400">
            Premium offline music player by WOWMAZING Studios.
          </p>

          <p className="mt-6 text-sm text-gray-500">
            © 2026 WOWMAZING Studios. All rights reserved.
          </p>
        </div>
      </footer>
    </main>
  );
}