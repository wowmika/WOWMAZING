import Navbar from "./components/Navbar";

export default function Home() {
  const products = [
    {
      icon: "📱",
      title: "Apps",
      desc: "Premium desktop and mobile applications.",
    },
    {
      icon: "🎮",
      title: "Games",
      desc: "Original indie PC and Android games.",
    },
    {
      icon: "🛠",
      title: "Developer Tools",
      desc: "AI tools and productivity software.",
    },
    {
      icon: "🎓",
      title: "Learning",
      desc: "Courses, projects and study materials.",
    },
  ];

  const games = [
    {
      title: "Project Eclipse",
      genre: "Sci-Fi RPG",
      color: "from-cyan-500 to-blue-700",
    },
    {
      title: "Shadow Drift",
      genre: "Action Adventure",
      color: "from-purple-600 to-pink-600",
    },
  ];

  return (
    <main className="relative min-h-screen overflow-hidden bg-[#050816] text-white">
      <Navbar />

      {/* Background Glow */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute left-20 top-32 h-72 w-72 rounded-full bg-cyan-500/20 blur-3xl" />
        <div className="absolute right-20 top-60 h-80 w-80 rounded-full bg-purple-600/20 blur-3xl" />
        <div className="absolute bottom-20 left-1/2 h-96 w-96 -translate-x-1/2 rounded-full bg-indigo-500/10 blur-3xl" />
      </div>

      {/* Hero */}
      <section className="mx-auto max-w-7xl px-8 py-24">
        <p className="text-cyan-400 font-semibold tracking-[0.3em]">
          WOWMAZING STUDIOS
        </p>

        <h1 className="mt-6 text-6xl font-black leading-tight md:text-7xl">
          Build Amazing.
          <br />
          <span className="bg-gradient-to-r from-cyan-300 to-purple-400 bg-clip-text text-transparent">
            Ship Fearlessly.
          </span>
        </h1>

        <p className="mt-8 max-w-2xl text-lg text-gray-400">
          We build premium apps, indie games, developer tools and world-class
          learning experiences for the next generation.
        </p>

        <div className="mt-10 flex flex-wrap gap-4">
          <a
  href="/products"
  className="rounded-xl bg-gradient-to-r from-purple-500 to-cyan-400 px-6 py-3 font-bold text-black transition hover:scale-105"
>
  Explore Products
</a>

          <button className="rounded-xl border border-white/20 px-6 py-3 font-semibold transition hover:bg-white/10">
            Learn More
          </button>
        </div>
      </section>

      {/* Products */}
      <section id="products" className="mx-auto max-w-7xl px-8 pb-24">
        <div className="mb-12">
          <p className="text-cyan-400 font-semibold tracking-[0.3em]">
            OUR ECOSYSTEM
          </p>

          <h2 className="mt-3 text-4xl font-black">
            Everything we create.
          </h2>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {products.map((item) => (
            <div
              key={item.title}
              className="group rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur transition duration-300 hover:-translate-y-2 hover:border-cyan-400"
            >
              <div className="text-5xl">{item.icon}</div>

              <h3 className="mt-5 text-xl font-bold">{item.title}</h3>

              <p className="mt-3 text-sm text-gray-400">{item.desc}</p>

              <button className="mt-6 text-cyan-400 transition group-hover:translate-x-1">
                Explore →
              </button>
            </div>
          ))}
        </div>
      </section>

      {/* Games */}
      <section id="games" className="mx-auto max-w-7xl px-8 pb-28">
        <div className="mb-12">
          <p className="text-cyan-400 font-semibold tracking-[0.3em]">
            COMING SOON
          </p>

          <h2 className="mt-3 text-4xl font-black">
            Games in development
          </h2>

          <p className="mt-4 max-w-2xl text-gray-400">
            Premium cinematic indie experiences built by WOWMAZING Studios.
          </p>
        </div>

        <div className="grid gap-8 lg:grid-cols-2">
          {games.map((game) => (
            <div
              key={game.title}
              className="group overflow-hidden rounded-3xl border border-white/10 bg-white/5 transition duration-300 hover:scale-[1.02]"
            >
              <div
                className={`flex h-64 items-center justify-center bg-gradient-to-br ${game.color}`}
              >
                <h3 className="text-4xl font-black text-white/90">
                  {game.title}
                </h3>
              </div>

              <div className="p-6">
                <p className="text-cyan-300">{game.genre}</p>

                <h3 className="mt-2 text-2xl font-bold">{game.title}</h3>

                <p className="mt-3 text-gray-400">
                  A next-generation indie title currently under development.
                </p>

                <button className="mt-6 rounded-lg border border-cyan-400 px-4 py-2 text-cyan-300 transition hover:bg-cyan-400 hover:text-black">
                  Wishlist
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>
      <section className="mx-auto max-w-7xl px-8 pb-28">
  <div className="mb-12">
    <p className="text-cyan-400 font-semibold tracking-widest">
      FEATURED PRODUCTS
    </p>

    <h2 className="mt-3 text-4xl font-black">
      Built by WOWMAZING
    </h2>
  </div>

  <div className="grid gap-8 lg:grid-cols-3">
    {[
      {
        title: "WOWMAZING Music",
        tag: "Desktop App",
        desc: "Offline music player with playlists, downloads and smart library.",
      },
      {
        title: "CodeForge",
        tag: "Developer Tool",
        desc: "A productivity toolkit for developers. Coming soon.",
      },
      {
        title: "Quantum Lab",
        tag: "Learning Platform",
        desc: "Interactive courses for AI, Quantum Computing and Cybersecurity.",
      },
    ].map((item) => (
      <div
        key={item.title}
        className="rounded-3xl border border-white/10 bg-gradient-to-b from-white/10 to-white/5 p-7 hover:border-cyan-400 transition"
      >
        <span className="rounded-full bg-cyan-500/20 px-3 py-1 text-xs text-cyan-300">
          {item.tag}
        </span>

        <h3 className="mt-5 text-2xl font-bold">{item.title}</h3>

        <p className="mt-4 text-gray-400">{item.desc}</p>

        <button className="mt-8 w-full rounded-xl bg-white/10 py-3 font-semibold hover:bg-cyan-400 hover:text-black transition">
          View Product
        </button>
      </div>
    ))}
  </div>
</section>
{/* About */}
<section id="about" className="mx-auto max-w-7xl px-8 pb-28">
  <div className="grid items-center gap-14 lg:grid-cols-2">

    {/* Left */}
    <div>
      <p className="text-cyan-400 font-semibold tracking-[0.3em]">
        ABOUT US
      </p>

      <h2 className="mt-4 text-5xl font-black leading-tight">
        One studio.
        <br />
        Endless possibilities.
      </h2>

      <p className="mt-8 text-lg leading-8 text-gray-400">
        WOWMAZING Studios is an independent software company creating beautiful
        applications, immersive games, powerful developer tools and premium
        educational experiences.
      </p>

      <p className="mt-5 text-gray-500 leading-7">
        Our mission is simple: build products that people genuinely love using.
      </p>
    </div>

    {/* Right */}
    <div className="grid grid-cols-2 gap-5">
      {[
        ["01", "Desktop Apps"],
        ["02", "Indie Games"],
        ["03", "Developer Tools"],
        ["04", "Learning Platform"],
      ].map(([num, text]) => (
        <div
          key={num}
          className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur"
        >
          <p className="text-3xl font-black text-cyan-300">{num}</p>
          <p className="mt-3 font-semibold">{text}</p>
        </div>
      ))}
    </div>
  </div>
</section>
{/* Statistics */}
<section className="mx-auto max-w-7xl px-8 pb-28">
  <div className="rounded-[32px] border border-white/10 bg-gradient-to-r from-cyan-500/10 to-purple-500/10 p-10 backdrop-blur">
    <div className="mb-10 text-center">
      <p className="text-cyan-400 font-semibold tracking-[0.3em]">
        OUR VISION
      </p>

      <h2 className="mt-4 text-4xl font-black">
        Building products for millions.
      </h2>

      <p className="mt-4 text-gray-400">
        Every great company starts with one product. This is our beginning.
      </p>
    </div>

    <div className="grid gap-8 text-center md:grid-cols-4">
      {[
        ["1", "Desktop App"],
        ["4", "Product Categories"],
        ["2026", "Founded"],
        ["∞", "Big Dreams"],
      ].map(([number, label]) => (
        <div key={label}>
          <h3 className="text-5xl font-black bg-gradient-to-r from-cyan-300 to-purple-400 bg-clip-text text-transparent">
            {number}
          </h3>

          <p className="mt-3 text-gray-400">{label}</p>
        </div>
      ))}
    </div>
  </div>
</section>

      {/* Footer */}
           
      <footer
  id="contact"
  className="border-t border-white/10 bg-[#040612]"
>
        <div className="mx-auto max-w-7xl px-8 py-16">
          <div className="grid gap-12 md:grid-cols-4">
            {/* Brand */}
            <div className="md:col-span-2">
              <h2 className="text-3xl font-black tracking-wide">
                WOWMAZING
              </h2>

              <p className="text-cyan-400 tracking-[0.25em] text-sm">
                STUDIOS
              </p>

              <p className="mt-5 max-w-md leading-7 text-gray-400">
                Building premium software, indie games, developer tools and
                next-generation learning experiences for creators worldwide.
              </p>

              <div className="mt-6 flex gap-3">
                <span className="rounded-full border border-cyan-500/30 bg-cyan-500/10 px-3 py-1 text-xs text-cyan-300">
                  Windows
                </span>
                <span className="rounded-full border border-purple-500/30 bg-purple-500/10 px-3 py-1 text-xs text-purple-300">
                  AI
                </span>
                <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-gray-300">
                  Indie Games
                </span>
              </div>
            </div>

            {/* Products */}
            <div>
              <h3 className="mb-4 font-bold text-white">Products</h3>

              <ul className="space-y-3 text-gray-400">
                <li className="hover:text-cyan-300 cursor-pointer transition">
                  WOWMAZING Music
                </li>
                <li className="hover:text-cyan-300 cursor-pointer transition">
                  CodeForge
                </li>
                <li className="hover:text-cyan-300 cursor-pointer transition">
                  Quantum Lab
                </li>
                <li className="hover:text-cyan-300 cursor-pointer transition">
                  Future Games
                </li>
              </ul>
            </div>

            {/* Company */}
            <div>
              <h3 className="mb-4 font-bold text-white">Company</h3>

              <ul className="space-y-3 text-gray-400">
                <li className="hover:text-cyan-300 cursor-pointer transition">
                  About
                </li>
                <li className="hover:text-cyan-300 cursor-pointer transition">
                  Careers
                </li>
                <li className="hover:text-cyan-300 cursor-pointer transition">
                  Blog
                </li>
                <li className="hover:text-cyan-300 cursor-pointer transition">
                  Contact
                </li>
              </ul>
            </div>
          </div>

          <div className="my-10 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent" />

          <div className="flex flex-col items-center justify-between gap-4 text-sm text-gray-500 md:flex-row">
            <p>© 2026 WOWMAZING Studios. All rights reserved.</p>

            <div className="flex gap-6">
              <a href="#" className="hover:text-cyan-300 transition">
                GitHub
              </a>
              <a href="#" className="hover:text-cyan-300 transition">
                X
              </a>
              <a href="#" className="hover:text-cyan-300 transition">
                YouTube
              </a>
            </div>
          </div>
        </div>
      </footer>

            
    </main>
  );
}