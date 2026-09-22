export default function NotFound() {
  return (
    <main className="relative flex min-h-screen items-center justify-center overflow-hidden bg-[#02040b] px-6 text-white">
      {/* Futuristic background */}
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute left-[-140px] top-[-100px] h-[420px] w-[420px] rounded-full bg-cyan-400/10 blur-[140px]" />

        <div className="absolute right-[-120px] top-[20%] h-[420px] w-[420px] rounded-full bg-purple-500/10 blur-[140px]" />

        <div className="absolute bottom-[-140px] left-1/2 h-[360px] w-[360px] -translate-x-1/2 rounded-full bg-blue-500/10 blur-[130px]" />

        <div className="absolute inset-0 opacity-[0.035] [background-image:linear-gradient(rgba(255,255,255,0.7)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.7)_1px,transparent_1px)] [background-size:72px_72px]" />

        <div className="absolute inset-x-0 top-1/2 h-px bg-gradient-to-r from-transparent via-cyan-400/20 to-transparent" />
      </div>

      {/* Main panel */}
      <div className="relative w-full max-w-3xl text-center">
        {/* System label */}
        <div className="mx-auto inline-flex items-center gap-3 rounded-full border border-cyan-400/20 bg-cyan-400/5 px-4 py-2 text-[10px] font-semibold tracking-[0.3em] text-cyan-300 backdrop-blur-xl">
          <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-cyan-300 shadow-[0_0_12px_rgba(103,232,249,0.9)]" />
          SYSTEM // ROUTE NOT FOUND
        </div>

        {/* 404 */}
        <div className="relative mt-10">
          <div className="pointer-events-none absolute inset-0 flex items-center justify-center text-[150px] font-black tracking-[-0.08em] text-cyan-400/5 blur-xl sm:text-[220px]">
            404
          </div>

          <h1 className="relative bg-gradient-to-r from-cyan-300 via-sky-400 to-purple-500 bg-clip-text text-[110px] font-black leading-none tracking-[-0.08em] text-transparent sm:text-[180px]">
            404
          </h1>
        </div>

        <p className="mt-5 font-mono text-xs tracking-[0.3em] text-gray-600">
          SIGNAL LOST
        </p>

        <h2 className="mt-5 text-3xl font-black sm:text-4xl">
          This destination doesn&apos;t exist.
        </h2>

        <p className="mx-auto mt-5 max-w-xl text-base leading-7 text-gray-500 sm:text-lg">
          The page you requested could not be located. The WOWMAZING system is
          still online — you just took a wrong turn.
        </p>

        {/* Terminal */}
        <div className="mx-auto mt-10 max-w-xl rounded-3xl border border-white/10 bg-white/[0.025] p-2 text-left backdrop-blur-xl">
          <div className="rounded-2xl border border-white/10 bg-black/30 p-5 font-mono text-xs">
            <div className="flex items-center gap-2 border-b border-white/10 pb-4">
              <span className="h-2.5 w-2.5 rounded-full bg-red-400/60" />
              <span className="h-2.5 w-2.5 rounded-full bg-yellow-400/60" />
              <span className="h-2.5 w-2.5 rounded-full bg-green-400/60" />
            </div>

            <div className="mt-5 space-y-2">
              <p className="text-gray-600">
                $ locate_requested_route
              </p>

              <p className="text-red-300/80">
                ✕ route unavailable
              </p>

              <p className="text-cyan-300">
                ✓ core systems operational
              </p>

              <p className="text-gray-500">
                $ redirect_available_destinations
              </p>
            </div>
          </div>
        </div>

        {/* Actions */}
        <div className="mt-10 flex flex-wrap justify-center gap-4">
          <a
            href="/"
            className="rounded-2xl bg-gradient-to-r from-cyan-400 to-purple-500 px-7 py-4 font-bold text-black transition hover:-translate-y-1 hover:shadow-[0_0_40px_rgba(34,211,238,0.18)]"
          >
            Return Home
          </a>

          <a
            href="/products"
            className="rounded-2xl border border-white/10 bg-white/[0.03] px-7 py-4 font-semibold text-white transition hover:-translate-y-1 hover:border-cyan-400/30 hover:bg-white/[0.06]"
          >
            Explore Products
          </a>
        </div>

        {/* Footer status */}
        <div className="mt-12 flex items-center justify-center gap-3 text-[9px] tracking-[0.3em] text-gray-700">
          <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-emerald-300" />
          WOWMAZING CORE ONLINE
          <span className="text-gray-800">•</span>
          NAVIGATION READY
        </div>
      </div>
    </main>
  );
}