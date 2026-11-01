from pathlib import Path

p = Path("index.html")
s = p.read_text()

style = r"""
/* ===== FLOATING IT HOLOGRAMS ===== */
#it-holograms {
  position: fixed;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  overflow: hidden;
}
.it-holo {
  position: absolute;
  color: #ff526f;
  opacity: .58;
  filter: drop-shadow(0 0 9px #ff174455);
  animation: it-hover 7s ease-in-out infinite;
}
.it-holo svg { width: 100%; height: 100%; display: block; }
.it-holo.monitor { width: 115px; left: 2.5%; top: 37%; animation-delay: -2s; }
.it-holo.phone { width: 54px; right: 5%; top: 62%; animation-delay: -4s; }
.it-holo.cloud { width: 90px; right: 3%; top: 39%; animation-delay: -1s; }
.it-holo.gear { width: 48px; right: 13%; top: 48%; animation: it-hover 8s ease-in-out infinite, gear-spin 22s linear infinite; }
.it-holo.monitor .screen {
  fill: rgba(255,23,68,.06);
  stroke: #ff526f;
  stroke-width: 1.5;
}
.it-holo .code-line {
  stroke: #ff9aaa;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-dasharray: 30;
  animation: code-draw 3s ease-in-out infinite alternate;
}
.it-holo .code-line:nth-child(2) { animation-delay: -.8s; }
.it-holo .code-line:nth-child(3) { animation-delay: -1.5s; }
.it-holo .code-line:nth-child(4) { animation-delay: -2s; }
.it-holo.phone .phone-screen {
  fill: rgba(255,23,68,.07);
  stroke: #ff526f;
  stroke-width: 1.5;
}
.it-holo.phone .app-dot { fill: #ff9aaa; animation: holo-pulse 2s ease-in-out infinite alternate; }
.it-holo.cloud .cloud-shape {
  fill: rgba(255,23,68,.05);
  stroke: #ff526f;
  stroke-width: 1.5;
}
.it-holo.gear .gear-shape { fill: none; stroke: #ff526f; stroke-width: 2; }
@keyframes it-hover {
  0%,100% { transform: translateY(0) rotate(-2deg); }
  50% { transform: translateY(-17px) rotate(2deg); }
}
@keyframes gear-spin { to { rotate: 360deg; } }
@keyframes code-draw { from { stroke-dashoffset: 30; opacity: .25; } to { stroke-dashoffset: 0; opacity: 1; } }
@keyframes holo-pulse { from { opacity: .25; } to { opacity: 1; } }
@media (max-width: 700px) {
  .it-holo.monitor { width: 75px; left: 1%; top: 42%; opacity: .35; }
  .it-holo.phone { width: 38px; right: 2%; top: 68%; opacity: .4; }
  .it-holo.cloud { width: 58px; right: 1%; top: 42%; opacity: .35; }
  .it-holo.gear { width: 30px; right: 12%; top: 51%; opacity: .3; }
}
@media (prefers-reduced-motion: reduce) {
  .it-holo, .it-holo * { animation-duration: 30s !important; }
}
"""

markup = r"""
<div id="it-holograms" aria-hidden="true">
  <div class="it-holo monitor">
    <svg viewBox="0 0 120 90" fill="none">
      <rect class="screen" x="5" y="4" width="110" height="65" rx="5"/>
      <path d="M45 70v8m30-8v8M35 80h50" stroke="currentColor" stroke-width="2"/>
      <path class="code-line" d="M14 17h26M14 25h42M14 33h18M14 41h35M14 49h22"/>
      <path d="M65 18l-7 8 7 8m10-16 7 8-7 8m13-16-7 16" stroke="#ff526f" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="it-holo phone">
    <svg viewBox="0 0 60 100" fill="none">
      <rect class="phone-screen" x="5" y="2" width="50" height="96" rx="8"/>
      <rect x="22" y="7" width="16" height="2" rx="1" fill="currentColor"/>
      <circle cx="30" cy="91" r="3" stroke="currentColor"/>
      <rect x="11" y="16" width="38" height="65" rx="3" fill="#ff1744" fill-opacity=".05"/>
      <circle class="app-dot" cx="20" cy="27" r="5"/>
      <path d="M29 25h14M29 29h10M15 42h30M15 48h24M15 58h30M15 64h20" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      <rect x="15" y="71" width="10" height="6" rx="2" fill="#ff526f" fill-opacity=".5"/>
      <rect x="28" y="71" width="10" height="6" rx="2" fill="#ff526f" fill-opacity=".3"/>
    </svg>
  </div>
  <div class="it-holo cloud">
    <svg viewBox="0 0 100 70" fill="none">
      <path class="cloud-shape" d="M24 55h52a16 16 0 0 0 0-32 25 25 0 0 0-47-4A18 18 0 0 0 24 55Z"/>
      <path d="M50 28v25m-9-9 9 9 9-9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
  <div class="it-holo gear">
    <svg viewBox="0 0 50 50" fill="none">
      <path class="gear-shape" d="M21 3h8l2 6 5 2 5-3 6 6-3 5 2 5 6 2v8l-6 2-2 5-5-3-6 2-2 6h-8l-2-6-5-2-5 3-6-6 3-5-2-5-6-2v-8l6-2 2-5-3-5 6-6 5 3 5-2 2-6Z" transform="translate(2 2) scale(.88)"/>
      <circle class="gear-shape" cx="25" cy="25" r="9"/>
      <circle cx="25" cy="25" r="3" fill="currentColor"/>
    </svg>
  </div>
</div>
"""

if "FLOATING IT HOLOGRAMS" not in s:
    s = s.replace("</head>", "<style>\n" + style + "\n</style>\n</head>", 1)

if 'id="it-holograms"' not in s:
    s = s.replace("<body>", "<body>\n" + markup, 1)

p.write_text(s)
print("Elemen monitor, ponsel, cloud, dan gear berhasil ditambahkan.")
