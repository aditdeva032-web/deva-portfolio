from pathlib import Path

p = Path("index.html")
s = p.read_text()

css = r"""
/* ===== LIVING RED GALAXY ===== */
#galaxy-ornaments {
  position: fixed;
  inset: 0;
  z-index: 1;
  overflow: hidden;
  pointer-events: none;
  contain: strict;
}
.galaxy-nebula {
  position: absolute;
  width: 75vw;
  height: 75vw;
  max-width: 900px;
  max-height: 900px;
  border-radius: 50%;
  filter: blur(65px);
  opacity: .17;
  mix-blend-mode: screen;
  animation: nebula-drift 24s ease-in-out infinite alternate;
}
.galaxy-nebula.n1 {
  background: radial-gradient(circle, #ff1744 0%, #7b102d 35%, transparent 70%);
  top: -25%; left: -20%;
}
.galaxy-nebula.n2 {
  background: radial-gradient(circle, #a855f7 0%, #45105d 38%, transparent 70%);
  right: -30%; top: 20%;
  animation-delay: -8s;
}
.galaxy-nebula.n3 {
  background: radial-gradient(circle, #ff4d6d 0%, #4c0519 40%, transparent 70%);
  bottom: -35%; left: 10%;
  animation-delay: -14s;
}
@keyframes nebula-drift {
  from { transform: translate3d(-4%, -3%, 0) scale(.85) rotate(0deg); }
  to { transform: translate3d(8%, 7%, 0) scale(1.18) rotate(18deg); }
}
.galaxy-star {
  position: absolute;
  width: 2px; height: 2px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 0 6px 1px rgba(255,255,255,.8);
  animation: star-twinkle var(--twinkle, 3s) ease-in-out infinite alternate;
}
@keyframes star-twinkle {
  from { opacity: .15; transform: scale(.6); }
  to { opacity: 1; transform: scale(1.8); }
}
.galaxy-comet {
  position: absolute;
  width: 140px; height: 2px;
  opacity: 0;
  background: linear-gradient(90deg, transparent, #fff, #ff637d, transparent);
  filter: drop-shadow(0 0 5px #ff1744);
  transform: rotate(-35deg);
  animation: comet-flight 9s linear infinite;
}
.galaxy-comet::after {
  content: "";
  position: absolute;
  right: 25%; top: -2px;
  width: 5px; height: 5px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 0 12px 4px #ff4267;
}
.galaxy-comet.c1 { top: 18%; left: -20%; animation-delay: 1s; }
.galaxy-comet.c2 { top: 55%; left: -20%; animation-delay: 6s; animation-duration: 12s; }
@keyframes comet-flight {
  0%, 72% { opacity: 0; transform: translate3d(0,0,0) rotate(-35deg); }
  75% { opacity: .9; }
  90% { opacity: 0; transform: translate3d(140vw,65vh,0) rotate(-35deg); }
  100% { opacity: 0; }
}
.galaxy-planet {
  position: absolute;
  border-radius: 50%;
  transform-style: preserve-3d;
  animation: planet-float 12s ease-in-out infinite alternate;
}
.galaxy-planet.p1 {
  width: clamp(70px, 12vw, 150px);
  aspect-ratio: 1;
  right: 7%; top: 22%;
  background:
    radial-gradient(circle at 30% 25%, rgba(255,255,255,.8), transparent 8%),
    radial-gradient(circle at 35% 30%, #ffb3c1, #c9184a 28%, #4c0519 68%, #12020a);
  box-shadow: inset -18px -12px 28px rgba(0,0,0,.7), 0 0 35px #ff174433;
}
.galaxy-planet.p1::before {
  content: "";
  position: absolute;
  inset: 25% -35%;
  border: 2px solid rgba(255,140,170,.55);
  border-radius: 50%;
  transform: rotate(-22deg) scaleY(.35);
  box-shadow: 0 0 12px #ff174455;
}
.galaxy-planet.p2 {
  width: clamp(30px, 5vw, 65px);
  aspect-ratio: 1;
  left: 8%; bottom: 18%;
  background: radial-gradient(circle at 30% 25%, #e9d5ff, #8b5cf6 40%, #2e1065 75%);
  box-shadow: inset -9px -7px 15px #0009, 0 0 22px #a855f744;
  animation-delay: -5s;
}
.galaxy-orbit {
  position: absolute;
  width: 210px; height: 210px;
  right: 3%; top: 18%;
  border: 1px solid rgba(255,100,140,.12);
  border-radius: 50%;
  animation: orbit-spin 35s linear infinite;
}
.galaxy-orbit::before, .galaxy-orbit::after {
  content: "";
  position: absolute;
  border: 1px solid rgba(255,100,140,.08);
  border-radius: 50%;
  inset: 18px;
}
.galaxy-orbit::after { inset: 38px; }
@keyframes orbit-spin { to { transform: rotate(360deg); } }
@keyframes planet-float {
  from { translate: 0 -8px; }
  to { translate: 0 14px; }
}
@media (max-width: 600px) {
  .galaxy-nebula { filter: blur(45px); opacity: .13; }
  .galaxy-planet.p1 { right: 2%; top: 14%; opacity: .7; }
  .galaxy-planet.p2 { left: 2%; bottom: 10%; }
  .galaxy-orbit { width: 150px; height: 150px; right: -5%; top: 13%; }
}
@media (prefers-reduced-motion: reduce) {
  #galaxy-ornaments *, #galaxy-ornaments *::before, #galaxy-ornaments *::after {
    animation-duration: 30s !important;
  }
}
"""

markup = """
<div id="galaxy-ornaments" aria-hidden="true">
  <div class="galaxy-nebula n1"></div>
  <div class="galaxy-nebula n2"></div>
  <div class="galaxy-nebula n3"></div>
  <div class="galaxy-planet p1"></div>
  <div class="galaxy-planet p2"></div>
  <div class="galaxy-orbit"></div>
  <div class="galaxy-comet c1"></div>
  <div class="galaxy-comet c2"></div>
</div>
"""

js = """
<script>
(() => {
  const root = document.getElementById('galaxy-ornaments');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';

  // Bintang acak, dibuat sekali agar tetap ringan.
  const count = window.innerWidth < 600 ? 65 : 125;
  const frag = document.createDocumentFragment();
  for (let i = 0; i < count; i++) {
    const star = document.createElement('i');
    star.className = 'galaxy-star';
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    star.style.setProperty('--twinkle', (2 + Math.random() * 5) + 's');
    star.style.animationDelay = (-Math.random() * 6) + 's';
    if (Math.random() > .82) {
      star.style.width = '3px';
      star.style.height = '3px';
    }
    frag.appendChild(star);
  }
  root.appendChild(frag);
})();
</script>
"""

if "/* ===== LIVING RED GALAXY ===== */" not in s:
    s = s.replace("</head>", "<style>\n" + css + "\n</style>\n</head>", 1)

if 'id="galaxy-ornaments"' not in s:
    s = s.replace("<body>", "<body>\n" + markup, 1)

if "galaxy-ornaments').dataset" not in s and "const root = document.getElementById('galaxy-ornaments')" not in s:
    s = s.replace("</body>", js + "\n</body>", 1)

p.write_text(s)
print("Ornamen galaksi berhasil ditambahkan.")
