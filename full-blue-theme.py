from pathlib import Path

p = Path("index.html")
s = p.read_text()

css = r"""
/* ===== COMPLETE DARK BLUE GALAXY THEME ===== */
:root {
  color-scheme: dark;
  --bg: #030712 !important;
  --panel: rgba(9, 20, 43, .82) !important;
  --text: #eaf6ff !important;
  --muted: #9bb2cc !important;
  --cyan: #38bdf8 !important;
  --purple: #818cf8 !important;
  --line: rgba(96, 165, 250, .2) !important;
  --blue-electric: #3b82f6;
  --blue-cyan: #22d3ee;
  --blue-glow: rgba(56, 189, 248, .28);
}

/* Background utama dan lapisan atmosfer */
html, body {
  background-color: #030712 !important;
  color: var(--text) !important;
}
body {
  background:
    radial-gradient(ellipse at 12% 12%, rgba(30, 64, 175, .24), transparent 38%),
    radial-gradient(ellipse at 88% 42%, rgba(8, 145, 178, .18), transparent 40%),
    linear-gradient(145deg, #020617 0%, #071329 48%, #030712 100%) !important;
}
.background {
  background:
    radial-gradient(ellipse at 15% 15%, #102b59 0, transparent 48%),
    radial-gradient(ellipse at 85% 55%, #102c49 0, transparent 42%),
    radial-gradient(ellipse at 50% 100%, #11133d 0, transparent 55%),
    #030712 !important;
}
.orb { background: #38bdf8 !important; opacity: .2 !important; }
.orb.two { background: #6366f1 !important; opacity: .24 !important; }

/* Header, navigasi, logo */
header {
  background: rgba(3, 7, 18, .82) !important;
  border-bottom: 1px solid rgba(96, 165, 250, .2) !important;
  box-shadow: 0 8px 35px rgba(0, 0, 0, .18);
  backdrop-filter: blur(22px) saturate(150%) !important;
}
.logo span, .nav-links a:hover { color: #38bdf8 !important; }
.nav-links a { transition: color .25s, text-shadow .25s; }
.nav-links a:hover { text-shadow: 0 0 16px #38bdf866; }
.menu-btn {
  color: #dbeafe !important;
  border-color: #38bdf855 !important;
  background: #071329 !important;
}
.nav-links.open {
  background: rgba(3, 10, 25, .97) !important;
  border-color: #38bdf833 !important;
}

/* Tipografi dan heading */
h1, h2, h3, .section-title {
  color: #eaf6ff !important;
  text-shadow: 0 0 25px rgba(56, 189, 248, .12);
}
.eyebrow {
  color: #38bdf8 !important;
  text-shadow: 0 0 15px #38bdf833;
}
.gradient {
  background: linear-gradient(100deg, #60a5fa, #22d3ee, #a5b4fc) !important;
  background-size: 200% auto !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  color: transparent !important;
}
.hero p, .section-desc, .card p { color: #9bb2cc !important; }

/* Tombol */
.btn {
  color: #dbeafe !important;
  background: rgba(8, 20, 42, .72) !important;
  border: 1px solid rgba(96, 165, 250, .3) !important;
  box-shadow: inset 0 1px rgba(255,255,255,.035);
}
.btn:hover {
  border-color: #38bdf8aa !important;
  box-shadow: 0 0 25px rgba(56, 189, 248, .16) !important;
}
.btn.primary {
  color: #03111e !important;
  background: linear-gradient(115deg, #38bdf8, #818cf8) !important;
  border: 0 !important;
  box-shadow: 0 0 30px rgba(56, 189, 248, .24) !important;
}
.btn.primary:hover {
  box-shadow: 0 0 38px rgba(56, 189, 248, .4) !important;
}

/* Hero dan foto profil */
.profile-frame {
  border-color: rgba(56, 189, 248, .75) !important;
  background: linear-gradient(145deg, #0c2b4d, #171746) !important;
  box-shadow:
    0 0 70px rgba(56, 189, 248, .17),
    inset 0 0 40px rgba(129, 140, 248, .12) !important;
}
.profile-placeholder {
  color: #67e8f9 !important;
  text-shadow: 0 0 35px #38bdf8 !important;
}

/* Semua kartu dan panel */
.card, .cyber-stat, .cyber-terminal, .cyber-hud,
.project-card, .skill-card, .contact-card, .stat-card,
[class*="card"], [class*="panel"] {
  border-color: rgba(96, 165, 250, .2) !important;
}
.card {
  background: linear-gradient(145deg, rgba(10, 25, 51, .9), rgba(5, 13, 30, .88)) !important;
  box-shadow: 0 14px 40px rgba(0, 0, 0, .2), inset 0 1px rgba(147, 197, 253, .04);
  backdrop-filter: blur(14px);
}
.card:hover {
  border-color: rgba(56, 189, 248, .65) !important;
  box-shadow: 0 18px 45px rgba(14, 165, 233, .1) !important;
}
.project-visual {
  background:
    radial-gradient(circle at 30% 25%, rgba(56, 189, 248, .35), transparent 30%),
    linear-gradient(135deg, #102b50, #17183f) !important;
  border: 1px solid rgba(96, 165, 250, .12);
}
.tag {
  color: #7dd3fc !important;
  background: rgba(56, 189, 248, .07) !important;
  border-color: rgba(56, 189, 248, .22) !important;
}
.project-link { color: #38bdf8 !important; }

/* Terminal, statistik, ticker, HUD */
.cyber-terminal {
  background: linear-gradient(135deg, rgba(5, 18, 39, .96), rgba(9, 14, 39, .94)) !important;
  border-color: rgba(56, 189, 248, .35) !important;
  box-shadow: 0 0 35px rgba(56, 189, 248, .07) !important;
}
.terminal-head {
  color: #7dd3fc !important;
  background: rgba(56, 189, 248, .045) !important;
  border-color: rgba(56, 189, 248, .18) !important;
}
.terminal-dot { background: #38bdf8 !important; box-shadow: 0 0 8px #38bdf8 !important; }
.terminal-prompt, .cyber-stat strong { color: #38bdf8 !important; }
.terminal-output { color: #a5f3fc !important; }
.terminal-cursor { background: #22d3ee !important; }
.cyber-stat {
  background: rgba(7, 20, 43, .75) !important;
}
.cyber-stat strong { text-shadow: 0 0 15px #38bdf855 !important; }
.cyber-stat span { color: #9bb2cc !important; }
.cyber-divider { color: #38bdf8 !important; }
.cyber-divider::before, .cyber-divider::after {
  background: linear-gradient(90deg, transparent, #38bdf855) !important;
}
.cyber-divider::after {
  background: linear-gradient(90deg, #38bdf855, transparent) !important;
}
.cyber-ticker {
  color: #7dd3fc !important;
  background: rgba(5, 16, 35, .75) !important;
  border-color: rgba(56, 189, 248, .18) !important;
}
.cyber-hud {
  color: #7dd3fc !important;
  background: rgba(3, 12, 28, .88) !important;
  border-color: rgba(56, 189, 248, .3) !important;
}
.hud-title { color: #38bdf8 !important; border-color: #38bdf833 !important; }
.hud-value { color: #bae6fd !important; }
.hud-bar { background: #38bdf822 !important; }
.hud-bar span { background: #38bdf8 !important; box-shadow: 0 0 10px #38bdf8 !important; }

/* Form dan footer */
input, textarea, select {
  color: #e0f2fe !important;
  background: rgba(5, 16, 35, .88) !important;
  border-color: rgba(96, 165, 250, .25) !important;
}
input:focus, textarea:focus, select:focus {
  border-color: #38bdf8 !important;
  box-shadow: 0 0 0 3px rgba(56, 189, 248, .1) !important;
}
footer {
  color: #8fa8c5 !important;
  border-color: rgba(96, 165, 250, .18) !important;
}

/* Loader */
#cosmic-loader { background: #020617 !important; }
.loader-orbit { border-color: #38bdf855 !important; }
.loader-planet {
  background: linear-gradient(135deg, #67e8f9, #4f46e5) !important;
  box-shadow: 0 0 30px #38bdf899 !important;
}
.loader-core {
  background: radial-gradient(circle at 30% 30%, #e0f2fe, #6366f1 50%, #020617) !important;
  box-shadow: 0 0 50px #6366f199 !important;
}
.loader-title {
  background: linear-gradient(90deg, #38bdf8, #c4b5fd, #22d3ee) !important;
  background-size: 200% !important;
  color: transparent !important;
  background-clip: text !important;
}
.loader-progress {
  background: linear-gradient(90deg, #38bdf8, #818cf8) !important;
  box-shadow: 0 0 15px #38bdf8 !important;
}

/* Galaksi dan hologram IT: hapus filter hue merah lama */
#galaxy-ornaments, #it-holograms {
  filter: none !important;
}
.galaxy-nebula.n1 {
  background: radial-gradient(circle, #2563eb 0%, #1e3a8a 38%, transparent 70%) !important;
}
.galaxy-nebula.n2 {
  background: radial-gradient(circle, #06b6d4 0%, #164e63 38%, transparent 70%) !important;
}
.galaxy-nebula.n3 {
  background: radial-gradient(circle, #6366f1 0%, #312e81 40%, transparent 70%) !important;
}
.galaxy-comet {
  background: linear-gradient(90deg, transparent, #e0f2fe, #38bdf8, transparent) !important;
  filter: drop-shadow(0 0 5px #38bdf8) !important;
}
.galaxy-comet::after {
  box-shadow: 0 0 12px 4px #38bdf8 !important;
}
.galaxy-planet.p1 {
  background:
    radial-gradient(circle at 30% 25%, rgba(255,255,255,.8), transparent 8%),
    radial-gradient(circle at 35% 30%, #bae6fd, #2563eb 30%, #172554 70%, #020617) !important;
  box-shadow: inset -18px -12px 28px rgba(0,0,0,.7), 0 0 35px #38bdf833 !important;
}
.galaxy-planet.p1::before {
  border-color: rgba(125, 211, 252, .55) !important;
  box-shadow: 0 0 12px #38bdf844 !important;
}
.galaxy-planet.p2 {
  background: radial-gradient(circle at 30% 25%, #e0f2fe, #6366f1 40%, #1e1b4b 75%) !important;
  box-shadow: inset -9px -7px 15px #0009, 0 0 22px #818cf844 !important;
}
.galaxy-orbit {
  border-color: rgba(56, 189, 248, .15) !important;
}
.galaxy-orbit::before, .galaxy-orbit::after {
  border-color: rgba(129, 140, 248, .1) !important;
}

/* IT hologram SVGs */
.it-holo {
  color: #7dd3fc !important;
  filter: drop-shadow(0 0 9px #38bdf855) !important;
}
.it-holo.monitor .screen, .it-holo.phone .phone-screen {
  stroke: #38bdf8 !important;
  fill: rgba(56, 189, 248, .06) !important;
}
.it-holo .code-line { stroke: #a5f3fc !important; }
.it-holo.phone .app-dot { fill: #67e8f9 !important; }
.it-holo.cloud .cloud-shape { stroke: #38bdf8 !important; }
.it-holo.gear .gear-shape { stroke: #7dd3fc !important; }
#it-holograms::after {
  border-color: rgba(56, 189, 248, .15) !important;
  box-shadow: 0 0 45px rgba(56, 189, 248, .06), inset 0 0 45px rgba(56, 189, 248, .04) !important;
}

/* Scanlines dan code rain */
body::before {
  background: repeating-linear-gradient(
    to bottom, transparent 0, transparent 3px, #38bdf8 4px
  ) !important;
  opacity: .025 !important;
}
#hacker-rain { opacity: .09 !important; }
"""

if "COMPLETE DARK BLUE GALAXY THEME" not in s:
    s = s.replace("</head>", "<style>\n" + css + "\n</style>\n</head>", 1)

p.write_text(s)
print("Tema seluruh website berhasil diubah ke Dark Blue Galaxy.")
