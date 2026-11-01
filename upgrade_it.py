from pathlib import Path

p = Path("index.html")
s = p.read_text()

css = r"""
/* ===== DEVA IT CYBER ORNAMENTS ===== */
:root {
  --cyber-red: #ff2348;
  --cyber-glow: #ff234855;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  opacity: .035;
  background: repeating-linear-gradient(
    to bottom,
    transparent 0px,
    transparent 3px,
    #ff526b 4px
  );
}

#hacker-rain {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  opacity: .15;
  pointer-events: none;
}

header, main, footer {
  position: relative;
  z-index: 3;
}

.cyber-hud {
  position: fixed;
  z-index: 4;
  top: 100px;
  right: 18px;
  width: 185px;
  padding: 14px;
  border: 1px solid #ff234833;
  border-radius: 12px;
  background: #090307c9;
  backdrop-filter: blur(12px);
  font: 10px/1.8 monospace;
  color: #ff7187;
  box-shadow: 0 0 25px #ff123f0c;
  pointer-events: none;
}

.hud-title {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #ff234833;
  padding-bottom: 7px;
  margin-bottom: 7px;
  color: #ff3658;
  letter-spacing: 1px;
}

.hud-line {
  display: flex;
  justify-content: space-between;
  gap: 8px;
}

.hud-value {
  color: #ffd0d8;
}

.hud-bar {
  height: 3px;
  background: #ff234422;
  margin: 5px 0 8px;
  overflow: hidden;
}

.hud-bar span {
  display: block;
  height: 100%;
  width: 72%;
  background: #ff2348;
  box-shadow: 0 0 10px #ff2348;
  animation: hud-load 3s ease-in-out infinite alternate;
}

.cyber-terminal {
  border: 1px solid #ff234855;
  border-radius: 16px;
  background: linear-gradient(135deg, #100308ed, #1c050bed);
  overflow: hidden;
  box-shadow: 0 0 35px #ff123f12;
  margin: 35px 0 20px;
  font-family: monospace;
}

.terminal-head {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 12px 16px;
  border-bottom: 1px solid #ff234422;
  background: #ff234808;
  color: #ff7187;
  font-size: 11px;
}

.terminal-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ff2348;
  box-shadow: 0 0 8px #ff2348;
}

.terminal-body {
  padding: 20px;
  color: #cdaeb4;
  font-size: 12px;
  line-height: 2;
  overflow: hidden;
}

.terminal-prompt { color: #ff3658; }
.terminal-output { color: #ff9aaa; }
.terminal-cursor {
  display: inline-block;
  width: 7px;
  height: 14px;
  background: #ff3658;
  vertical-align: middle;
  animation: cursor-blink .8s steps(2) infinite;
}

.cyber-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin: 25px 0 10px;
}

.cyber-stat {
  padding: 18px;
  border: 1px solid #ff234422;
  border-radius: 14px;
  background: #16060b99;
  text-align: center;
}

.cyber-stat strong {
  display: block;
  font: 800 1.5rem monospace;
  color: #ff3658;
  text-shadow: 0 0 15px #ff234855;
}

.cyber-stat span {
  color: #c4a5aa;
  font-size: .72rem;
  letter-spacing: 1px;
}

.cyber-divider {
  display: flex;
  align-items: center;
  gap: 15px;
  margin: 25px 0;
  color: #ff3658;
  font: 10px monospace;
  letter-spacing: 3px;
}

.cyber-divider::before,
.cyber-divider::after {
  content: "";
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #ff234855);
}

.cyber-divider::after {
  background: linear-gradient(90deg, #ff234855, transparent);
}

.cyber-ticker {
  overflow: hidden;
  white-space: nowrap;
  border-block: 1px solid #ff234422;
  background: #120308aa;
  padding: 12px 0;
  color: #ff7187;
  font: 10px monospace;
  letter-spacing: 2px;
}

.cyber-ticker span {
  display: inline-block;
  padding-left: 100%;
  animation: ticker-scroll 28s linear infinite;
}

@keyframes hud-load {
  to { width: 96%; }
}

@keyframes cursor-blink {
  to { opacity: 0; }
}

@keyframes ticker-scroll {
  to { transform: translateX(-100%); }
}

@media (max-width: 1050px) {
  .cyber-hud { display: none; }
}

@media (max-width: 600px) {
  .cyber-stats { gap: 7px; }
  .cyber-stat { padding: 12px 5px; }
  .cyber-stat strong { font-size: 1.15rem; }
  .cyber-stat span { font-size: .6rem; letter-spacing: 0; }
  .terminal-body { padding: 14px; font-size: 10px; }
}

@media (prefers-reduced-motion: reduce) {
  .cyber-ticker span, .terminal-cursor, .hud-bar span {
    animation: none !important;
  }
}
"""

ornaments = r"""
<canvas id="hacker-rain" aria-hidden="true"></canvas>

<aside class="cyber-hud" aria-hidden="true">
  <div class="hud-title"><span>SYSTEM STATUS</span><span>● LIVE</span></div>
  <div class="hud-line"><span>CORE</span><span class="hud-value">ONLINE</span></div>
  <div class="hud-bar"><span></span></div>
  <div class="hud-line"><span>NETWORK</span><span class="hud-value">SECURE</span></div>
  <div class="hud-line"><span>SECTOR</span><span class="hud-value">DEVA-01</span></div>
  <div class="hud-line"><span>MODE</span><span class="hud-value">CREATIVE</span></div>
  <div class="hud-line"><span>STATUS</span><span class="hud-value">LEARNING</span></div>
</aside>
"""

band = r"""
<div class="container">
  <div class="cyber-stats reveal">
    <div class="cyber-stat"><strong>01</strong><span>CREATIVE MIND</span></div>
    <div class="cyber-stat"><strong>24/7</strong><span>LEARNING MODE</span></div>
    <div class="cyber-stat"><strong>∞</strong><span>IDEAS IN ORBIT</span></div>
  </div>

  <div class="cyber-terminal reveal">
    <div class="terminal-head">
      <span class="terminal-dot"></span>
      <span class="terminal-dot" style="background:#ffbd44"></span>
      <span class="terminal-dot" style="background:#50fa7b"></span>
      <span style="margin-left:8px">deva@portfolio:~</span>
    </div>
    <div class="terminal-body">
      <div><span class="terminal-prompt">deva@portfolio:~$</span> whoami</div>
      <div class="terminal-output">DEVA ARDITIA SUWITKA — CREATIVE DEVELOPER</div>
      <div><span class="terminal-prompt">deva@portfolio:~$</span> cat mission.txt</div>
      <div class="terminal-output">Belajar, bereksperimen, dan menciptakan sesuatu yang berarti.</div>
      <div><span class="terminal-prompt">deva@portfolio:~$</span> <span id="terminal-typing"></span><span class="terminal-cursor"></span></div>
    </div>
  </div>

  <div class="cyber-divider">TRANSMISSION // END OF LOG</div>
</div>

<div class="cyber-ticker" aria-hidden="true">
  <span>
    [ SYSTEM ONLINE ] &nbsp; // &nbsp; KEEP BUILDING &nbsp; // &nbsp;
    LEARN • CREATE • REPEAT &nbsp; // &nbsp; DEVA AS. &nbsp; // &nbsp;
    WELCOME TO THE CRIMSON GALAXY &nbsp; // &nbsp;
  </span>
</div>
"""

script = r"""
<script id="cyber-ornaments-script">
(() => {
  const canvas = document.getElementById("hacker-rain");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  const chars = "01アイウエオ<>/{}[]$#";
  let drops = [];
  let w, h, columns;
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;

  function resize() {
    w = canvas.width = innerWidth;
    h = canvas.height = innerHeight;
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    columns = Math.floor(w / 18);
    drops = Array.from({length: columns}, () => Math.random() * -50);
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    ctx.font = "12px monospace";
    for (let i = 0; i < drops.length; i++) {
      const char = chars[Math.floor(Math.random() * chars.length)];
      ctx.fillStyle = Math.random() > .96 ? "#ff9aaa" : "#a80d2d";
      ctx.fillText(char, i * 18, drops[i] * 18);
      if (drops[i] * 18 > h && Math.random() > .975) drops[i] = 0;
      if (!reduced) drops[i] += .25;
    }
    if (!reduced) requestAnimationFrame(draw);
  }

  resize();
  draw();
  addEventListener("resize", resize);

  const target = document.getElementById("terminal-typing");
  if (target) {
    const messages = [
      "npm run create",
      "git commit -m 'keep learning'",
      "echo 'Hello, universe!'",
      "sudo make dreams real"
    ];
    let message = 0, index = 0, deleting = false;

    function type() {
      const current = messages[message];
      target.textContent = current.slice(0, index);
      if (!deleting && index < current.length) {
        index++;
        setTimeout(type, 75);
      } else if (!deleting) {
        deleting = true;
        setTimeout(type, 1300);
      } else if (index > 0) {
        index--;
        setTimeout(type, 35);
      } else {
        deleting = false;
        message = (message + 1) % messages.length;
        setTimeout(type, 350);
      }
    }
    type();
  }
})();
</script>
"""

if "DEVA IT CYBER ORNAMENTS" not in s:
    s = s.replace("</style>", css + "\n</style>", 1)

if 'id="hacker-rain"' not in s:
    s = s.replace("<body>", "<body>\n" + ornaments, 1)

if "TRANSMISSION // END OF LOG" not in s:
    marker = '<section class="container" id="about">'
    if marker in s:
        s = s.replace(marker, band + "\n" + marker, 1)
    else:
        print("Peringatan: bagian About tidak ditemukan.")

if 'id="cyber-ornaments-script"' not in s:
    s = s.replace("</body>", script + "\n</body>", 1)

p.write_text(s)
print("Ornamen IT dan animasi berhasil ditambahkan.")
