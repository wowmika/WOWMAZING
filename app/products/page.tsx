export default function ProductsPage() {
  const products = [
    {
      name: "WOWMAZING Music",
      type: "Windows Desktop",
      status: "Available",
      description:
        "Offline music player with playlists, downloads and smart library.",
      color: "from-cyan-500 to-blue-600",
      link: "/music",
    },
    {
      name: "CodeForge",
      type: "Developer Tool",
      status: "Coming Soon",
      description:
        "AI-powered toolkit for developers and software engineers.",
      color: "from-purple-500 to-pink-600",
      link: "#",
    },
    {
      name: "Quantum Lab",
      type: "Learning Platform",
      status: "Coming Soon",
      description:
        "Interactive learning platform for AI, Quantum Computing and Cybersecurity.",
      color: "from-emerald-500 to-teal-600",
      link: "#",
    },
  ];

  return (
    <main className="min-h-screen bg-[#050816] px-8 py-20 text-white">
      <div className="mx-auto max-w-7xl">
        <p className="font-semibold tracking-[0.3em] text-cyan-400">
          PRODUCTS
        </p>

        <h1 className="mt-4 text-5xl font-black">
          Everything built by WOWMAZING
        </h1>

        <p className="mt-6 max-w-2xl text-lg text-gray-400">
          Premium software, developer tools and educational products crafted by
          WOWMAZING Studios.
        </p>

        <div className="mt-16 grid gap-8 lg:grid-cols-3">
          {products.map((p) => (
            <div
              key={p.name}
              className="overflow-hidden rounded-3xl border border-white/10 bg-white/5 backdrop-blur"
            >
              <div className={`h-40 bg-gradient-to-br ${p.color}`} />

              <div className="p-6">
                <span className="rounded-full bg-cyan-500/20 px-3 py-1 text-xs text-cyan-300">
                  {p.type}
                </span>

                <h2 className="mt-4 text-2xl font-bold">{p.name}</h2>

                <p className="mt-4 text-gray-400">{p.description}</p>

                <div className="mt-6 flex items-center justify-between">
                  <span className="text-sm text-gray-500">{p.status}</span>

                  <a
                    href={p.link}
                    className="rounded-lg bg-white/10 px-4 py-2 text-sm font-semibold transition hover:bg-cyan-400 hover:text-black"
                  >
                    View →
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}