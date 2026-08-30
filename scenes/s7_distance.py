import streamlit as st
import streamlit.components.v1 as components

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)

    components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Caveat:wght@400;600&family=Lato:wght@300;400&display=swap" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
  background: #1a0a00;
  font-family: 'Lato', sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 48px 20px 60px;
}
.bg-glow {
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 60% 40% at 15% 10%, rgba(192,68,90,0.18), transparent 60%),
    radial-gradient(ellipse 50% 40% at 85% 20%, rgba(212,168,67,0.14), transparent 60%),
    radial-gradient(ellipse 80% 50% at 50% 100%, rgba(43,18,0,0.65), transparent 70%);
}
.content { position: relative; z-index: 1; width: 100%; max-width: 700px; display: flex; flex-direction: column; align-items: center; }
.eyebrow { font-size: 0.72rem; letter-spacing: 0.35em; text-transform: uppercase; color: rgba(212,168,67,0.65); text-align: center; margin-bottom: 0.8rem; animation: fadeUp 0.8s ease 0.1s both; }
.page-title { font-family: 'Playfair Display', serif; font-size: clamp(1.8rem,5vw,2.8rem); color: #f5e6c8; text-align: center; margin-bottom: 0.4rem; animation: fadeUp 0.8s ease 0.2s both; }
.page-sub { font-family: 'Playfair Display', serif; font-style: italic; font-size: clamp(0.9rem,2vw,1.1rem); color: rgba(245,230,200,0.55); text-align: center; margin-bottom: 2rem; line-height: 1.7; animation: fadeUp 0.8s ease 0.3s both; }
.thread-line { width: 100px; height: 2px; background: linear-gradient(90deg, transparent, #d4a843, transparent); border-radius: 2px; margin: 0 auto 2rem; animation: fadeUp 0.8s ease 0.35s both; }
.map-wrap { width: 100%; max-width: 620px; animation: fadeUp 1s ease 0.5s both; }
.card {
  background: rgba(245,230,200,0.05);
  border: 1px solid rgba(245,230,200,0.12);
  border-radius: 20px;
  padding: 2rem 2.5rem;
  backdrop-filter: blur(10px);
  max-width: 600px;
  width: 100%;
  text-align: center;
  margin-top: 1.5rem;
  animation: fadeUp 1s ease 0.8s both;
}
.card-text { font-family: 'Caveat', cursive; font-size: clamp(1.1rem,2.5vw,1.35rem); color: rgba(245,230,200,0.9); line-height: 1.95; }
.foot-note { font-size: 0.8rem; color: rgba(245,230,200,0.35); text-align: center; margin-top: 1.5rem; letter-spacing: 0.06em; animation: fadeUp 1s ease 1s both; }
@keyframes fadeUp { from { opacity:0; transform:translateY(18px); } to { opacity:1; transform:none; } }

/* city pulse */
.city-pulse { animation: cityPulse 2s ease-in-out infinite; }
@keyframes cityPulse { 0%,100% { r: 8; opacity: 1; } 50% { r: 11; opacity: 0.8; } }
</style>
</head>
<body>
<div class="bg-glow"></div>
<div class="content">

  <p class="eyebrow">the distance</p>
  <h1 class="page-title">130 kilometres apart.</h1>
  <p class="page-sub">
    That's the distance between us today.<br>
    And the only reason I couldn't be there.
  </p>
  <div class="thread-line"></div>

  <!-- MAP -->
  <div class="map-wrap">
    <svg viewBox="0 0 620 360" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%; filter:drop-shadow(0 0 40px rgba(212,168,67,0.06));">
      <defs>
        <radialGradient id="mapGlow1" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="rgba(192,68,90,0.18)"/>
          <stop offset="100%" stop-color="transparent"/>
        </radialGradient>
        <radialGradient id="mapGlow2" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="rgba(212,168,67,0.18)"/>
          <stop offset="100%" stop-color="transparent"/>
        </radialGradient>
        <filter id="glow1">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>

      <!-- stylised map background -->
      <ellipse cx="310" cy="180" rx="260" ry="160" fill="rgba(212,168,67,0.03)" stroke="rgba(212,168,67,0.1)" stroke-width="1"/>
      <ellipse cx="310" cy="180" rx="200" ry="120" fill="rgba(212,168,67,0.02)" stroke="rgba(212,168,67,0.06)" stroke-width="0.5"/>

      <!-- heart flight path -->
      <path id="flightPath"
        d="M 170 255
           C 170 195, 108 132, 170 88
           C 212 56, 274 88, 310 130
           C 346 88, 408 56, 450 88
           C 512 132, 450 195, 450 255
           C 410 305, 348 325, 310 342
           C 272 325, 210 305, 170 255 Z"
        stroke="rgba(212,168,67,0.22)" stroke-width="1.5" stroke-dasharray="7 5" fill="none"/>

      <!-- glow behind Chennai -->
      <circle cx="170" cy="255" r="28" fill="url(#mapGlow1)"/>
      <!-- Chennai dot -->
      <circle cx="170" cy="255" r="10" fill="#c0445a" filter="url(#glow1)"/>
      <circle cx="170" cy="255" r="5" fill="#f5e6c8"/>
      <!-- Chennai label -->
      <text x="170" y="282" font-family="Lato,sans-serif" font-size="12" fill="rgba(245,230,200,0.85)" text-anchor="middle" letter-spacing="2">CHENNAI</text>

      <!-- glow behind Vellore -->
      <circle cx="450" cy="255" r="28" fill="url(#mapGlow2)"/>
      <!-- Vellore dot -->
      <circle cx="450" cy="255" r="10" fill="#d4a843" filter="url(#glow1)"/>
      <circle cx="450" cy="255" r="5" fill="#f5e6c8"/>
      <!-- Vellore label -->
      <text x="450" y="282" font-family="Lato,sans-serif" font-size="12" fill="rgba(245,230,200,0.85)" text-anchor="middle" letter-spacing="2">VELLORE</text>

      <!-- distance label in middle -->
      <text x="310" y="175" font-family="Playfair Display,serif" font-size="13" fill="rgba(212,168,67,0.55)" text-anchor="middle" font-style="italic">~ 130 km</text>

      <!-- animated plane: straight path Chennai -> Vellore only -->
      <path id="planePath"
        d="M 170 255 C 220 180, 350 160, 450 255"
        fill="none" stroke="none"/>
      <g id="plane">
        <text font-size="18" text-anchor="middle" dominant-baseline="middle">✈️</text>
      </g>
      <animateMotion xlink:href="#plane" dur="4s" repeatCount="indefinite" rotate="auto">
        <mpath xlink:href="#planePath"/>
      </animateMotion>

    </svg>
  </div>

  <!-- card -->
  <div class="card">
    <p class="card-text">
      Ungala romba miss panrom Anna. 🥺🤍<br><br>
      Sikarama Chennai ku vaanga. 🧡
    </p>
  </div>

  <p class="foot-note">130 km &nbsp;·&nbsp; ~2.5 hours by road &nbsp;·&nbsp; one bond that makes it feel like nothing</p>

</div>
</body>
</html>
""", height=780, scrolling=False)

    if st.button("Read my letter →", key="s7_next", use_container_width=True):
        go(4)
