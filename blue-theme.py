from pathlib import Path

p = Path("index.html")
s = p.read_text()

css = r"""
/* ===== DEVA BLUE NEBULA THEME ===== */
:root {
  --blue-main: #6366f1;
  --blue-bright: #38bdf8;
  --blue-cyan: #22d3ee;
  --blue-glow: rgba(56,189,248,.35);
  --blue-panel: rgba(12,20,43,.78);
  --blue-border: rgba(96,165,250,.24);
}

html { scroll-behavior: smooth; }
body {
  background:
    radial-gradient(ellipse at 12% 18%, rgba(91,33,182,.25), transparent 38%),
    radial-gradient(ellipse at 88% 35%, rgba(8,145,178,.19), transparent 40%),
    linear-gradient(135deg, #030712 0%, #080d20 48%, #030712 100%) !important;
  color: #e5f3ff;
}
body::before {
  background: linear-gradient(120deg, transparent, rgba(56,189,248,.035), transparent) !important;
}
a { color: var(--blue-bright); }
a:hover { color: #a5f3fc; }

h1, h2, h3, .section-title {
  color: #dbeafe;
  text-shadow: 0 0 24px rgba(59,130,246,.2);
}
button, .btn, .button, [class*="btn"] {
  border-color: rgba(96,165,250,.35);
}
.btn-primary, .primary-btn, button[type="submit"] {
  background: linear-gradient(110deg, #4f46e5, #0891b2) !important;
  color: #fff !important;
  box-shadow: 0 0 24px rgba(56,189,248,.18);
}
.btn-primary:hover, .primary-btn:hover {
  box-shadow: 0 0 32px rgba(56,189,248,.4);
  transform: translateY(-2px);
}
.card, .project-card, .skill-card, .contact-card, .stat-card,
[class*="card"], [class*="panel"] {
  border-color: var(--blue-border);
}
.project-card, .skill-card, .stat-card, .contact-card {
  background: linear-gradient(145deg, rgba(15,23,42,.88), rgba(8,15,32,.78));
  box-shadow: 0 12px 40px rgba(0,0,0,.22), inset 0 1px rgba(147,197,253,.05);
  backdrop-filter: blur(14px);
}
.project-card:hover, .skill-card:hover {
  border-color: rgba(56,189,248,.55);
  box-shadow: 0 0 30px rgba(56,189,248,.12);
}
header, nav, .navbar {
  background: rgba(3,7,18,.72);
  border-color: rgba(96,165,250,.12);
  backdrop-filter: blur(18px);
}
input, textarea, select {
  background: rgba(7,15,33,.8) !important;
  border-color: rgba(96,165,250,.25) !important;
  color: #e0f2fe !important;
}
input:focus, textarea:focus, select:focus {
  border-color: #38bdf8 !important;
  box-shadow: 0 0 0 3px rgba(56,189,248,.1) !important;
}

/* Ubah ornamen galaksi dan hologram merah menjadi biru */
#galaxy-ornaments {
  filter: hue-rotate(185deg) saturate(1.25);
}
#it-holograms {
  filter: hue-rotate(185deg) saturate(1.25);
}

/* Tampilan ilustrasi IT lebih fokus seperti referensi */
.it-holo.monitor {
  left: auto;
  right: 17%;
  top: 34%;
  width: clamp(105px, 15vw, 180px);
  opacity: .78;
  filter: drop-shadow(0 0 15px rgba(56,189,248,.35));
}
.it-holo.phone {
  right: 11%;
  top: 56%;
  opacity: .75;
}
.it-holo.cloud {
  right: 6%;
  top: 31%;
  opacity: .72;
}
.it-holo.gear {
  right: 9%;
  top: 46%;
  opacity: .65;
}
#it-holograms::after {
  content: "";
  position: absolute;
  right: 7%;
  top: 28%;
  width: 260px;
  height: 260px;
  border: 1px solid rgba(56,189,248,.12);
  border-radius: 50%;
  box-shadow: 0 0 45px rgba(56,189,248,.05), inset 0 0 45px rgba(56,189,248,.04);
  animation: blue-orbit 24s linear infinite;
}
@keyframes blue-orbit { to { transform: rotate(360deg); } }

@media (max-width: 700px) {
  .it-holo.monitor {
    right: 4%;
    top: 28%;
    width: 90px;
    opacity: .35;
  }
  .it-holo.phone { right: 3%; top: 50%; opacity: .35; }
  .it-holo.cloud { right: 2%; top: 24%; opacity: .3; }
  .it-holo.gear { right: 13%; top: 42%; opacity: .3; }
  #it-holograms::after {
    width: 150px; height: 150px;
    right: -4%; top: 24%;
  }
}
"""

if "DEVA BLUE NEBULA THEME" not in s:
    s = s.replace("</head>", "<style>\n" + css + "\n</style>\n</head>", 1)

p.write_text(s)
print("Tema dark blue berhasil diterapkan.")
