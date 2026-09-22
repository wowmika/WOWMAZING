export default function Loading() {
  return (
    <main className="fixed inset-0 z-[9999] flex min-h-screen items-center justify-center overflow-hidden bg-[#02040b] text-white">
      <div className="absolute inset-0">
        <div className="absolute left-1/2 top-1/2 h-[420px] w-[420px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan-400/10 blur-[120px]" />

        <div className="absolute left-[15%] top-[15%] h-40 w-40 rounded-full bg-purple-500/10 blur-[80px]" />

        <div className="absolute bottom-[15%] right-[15%] h-44 w-44 rounded-full bg-blue-500/10 blur-[90px]" />

        <div className="absolute inset-0 opacity-[0.03] [background-image:linear-gradient(rgba(255,255,255,0.8)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.8)_1px,transparent_1px)] [background-size:72px_72px]" />
      </div>

      <div className="relative w-full max-w-md px-6 text-center">
        <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-3xl border border-cyan-400/20 bg-cyan-400/5 shadow-[0_0_50px_rgba(34,211,238,0.12)]">
          <span className="text-3xl font-black text-cyan-300">
            W
          </span>
        </div>

        <p className="mt-6 text-[10px] font-semibold tracking-[0.45em] text-cyan-400">
          WOWMAZING STUDIOS
        </p>

        <h1 className="mt-4 text-3xl font-black tracking-tight">
          Initializing...
        </h1>

        <p className="mt-3 text-sm text-gray-600">
          Preparing the next experience
        </p>

        <div className="mt-10">
          <div className="h-1 overflow-hidden rounded-full bg-white/5">
            <div className="h-full w-1/2 animate-pulse rounded-full bg-gradient-to-r from-cyan-400 via-sky-400 to-purple-500" />
          </div>

          <div className="mt-3 flex justify-between font-mono text-[9px] tracking-[0.2em] text-gray-700">
            <span>SYSTEM</span>
            <span>LOADING</span>
          </div>
        </div>

        <div className="mt-8 flex items-center justify-center gap-2 text-[10px] tracking-[0.2em] text-gray-600">
          <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-cyan-300 shadow-[0_0_12px_rgba(103,232,249,0.8)]" />
          CORE SYSTEMS ONLINE
        </div>
      </div>
    </main>
  );
}