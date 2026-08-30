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
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Caveat:wght@400;600;700&family=Lato:wght@300;400&display=swap" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
  background:#1a0a00;
  font-family:'Lato',sans-serif;
  min-height:100vh;
  display:flex; flex-direction:column; align-items:center;
  padding:40px 20px 64px;
  overflow-x:hidden;
}
.bg-glow {
  position:fixed; inset:0; z-index:0; pointer-events:none;
  background:
    radial-gradient(ellipse 60% 40% at 15% 10%, rgba(192,68,90,0.16), transparent 60%),
    radial-gradient(ellipse 50% 40% at 85% 20%, rgba(212,168,67,0.12), transparent 60%),
    radial-gradient(ellipse 80% 50% at 50% 100%, rgba(43,18,0,0.6), transparent 70%);
}
.content { position:relative; z-index:1; width:100%; max-width:680px; }
.eyebrow { font-size:0.72rem; letter-spacing:0.35em; text-transform:uppercase; color:rgba(212,168,67,0.65); text-align:center; margin-bottom:0.8rem; animation:fadeUp 0.8s ease 0.1s both; }
.page-title { font-family:'Playfair Display',serif; font-size:clamp(1.8rem,5vw,2.8rem); color:#f5e6c8; text-align:center; margin-bottom:0.4rem; animation:fadeUp 0.8s ease 0.2s both; }
.page-sub { font-family:'Playfair Display',serif; font-style:italic; font-size:clamp(0.9rem,2vw,1.05rem); color:rgba(245,230,200,0.45); text-align:center; margin-bottom:2rem; animation:fadeUp 0.8s ease 0.3s both; }
.thread-line { width:100px; height:2px; background:linear-gradient(90deg,transparent,#d4a843,transparent); border-radius:2px; margin:0 auto 2rem; animation:fadeUp 0.8s ease 0.35s both; }

/* ── ENVELOPE ── */
.envelope-wrap {
  display:flex; justify-content:center; align-items:center;
  animation:fadeUp 0.8s ease 0.5s both;
  margin-bottom:1.5rem;
}
.envelope {
  position:relative; width:320px; height:200px; cursor:pointer;
  filter:drop-shadow(0 20px 40px rgba(0,0,0,0.5));
}
.env-body {
  position:absolute; inset:0;
  background:linear-gradient(160deg,#f7ead0,#e8d0a0);
  border-radius:4px 4px 12px 12px;
  border:1px solid rgba(212,168,67,0.4);
}
.env-flap {
  position:absolute; top:0; left:0; right:0;
  height:0; border-left:160px solid transparent; border-right:160px solid transparent;
  border-top:110px solid #d4a843;
  transform-origin:top center;
  transition:transform 0.6s cubic-bezier(0.4,0,0.2,1);
  filter:drop-shadow(0 4px 8px rgba(0,0,0,0.2));
  z-index:3;
}
.env-flap.open { transform:rotateX(180deg); }
.env-bottom { position:absolute; bottom:0; left:0; right:0; height:0; border-left:160px solid transparent; border-right:160px solid transparent; border-bottom:90px solid rgba(212,168,67,0.3); }
.env-left  { position:absolute; top:0; bottom:0; left:0; width:0; border-top:100px solid transparent; border-bottom:100px solid transparent; border-left:160px solid rgba(212,168,67,0.2); }
.env-right { position:absolute; top:0; bottom:0; right:0; width:0; border-top:100px solid transparent; border-bottom:100px solid transparent; border-right:160px solid rgba(212,168,67,0.2); }
.env-seal {
  position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
  width:44px; height:44px; border-radius:50%;
  background:radial-gradient(circle at 38% 35%,#e06080,#a02040);
  box-shadow:0 4px 12px rgba(160,32,64,0.5);
  display:flex; align-items:center; justify-content:center;
  font-size:1.3rem; z-index:4;
  transition:opacity 0.3s ease;
}
.env-hint {
  text-align:center; margin-top:0.8rem;
  font-family:'Caveat',cursive; font-size:1rem;
  color:rgba(245,230,200,0.5);
  animation:pulse 2s ease-in-out infinite;
}
@keyframes pulse { 0%,100%{opacity:0.5} 50%{opacity:1} }

/* letter rising from envelope */
.letter-rising {
  position:absolute; bottom:10px; left:50%; transform:translateX(-50%);
  width:280px; height:160px;
  background:linear-gradient(160deg,#fdf6e3,#f7ead0);
  border-radius:4px;
  border:1px solid rgba(212,168,67,0.3);
  z-index:2;
  transition:transform 0.7s cubic-bezier(0.4,0,0.2,1) 0.4s;
}
.letter-rising.risen { transform:translateX(-50%) translateY(-120px); }

/* ── LETTER PAPER ── */
.letter-paper {
  background:linear-gradient(160deg,#fdf6e3 0%,#f7ead0 60%,#f0ddb8 100%);
  border-radius:20px;
  padding:clamp(2rem,6vw,3.5rem) clamp(1.5rem,6vw,4rem);
  position:relative; overflow:hidden;
  opacity:0; transform:translateY(30px);
  transition:opacity 0.8s ease, transform 0.8s ease;
}
.letter-paper.visible { opacity:1; transform:none; }

/* candlelight flicker */
.letter-paper::before {
  content:'';
  position:absolute; inset:0; border-radius:20px;
  box-shadow:
    0 40px 80px rgba(0,0,0,0.55),
    0 0 0 1px rgba(212,168,67,0.2),
    inset 0 1px 0 rgba(255,255,255,0.6),
    0 0 60px rgba(212,140,40,0.15),
    0 0 120px rgba(192,68,90,0.08);
  animation:candleFlicker 3s ease-in-out infinite;
  pointer-events:none;
}
@keyframes candleFlicker {
  0%,100% { box-shadow: 0 40px 80px rgba(0,0,0,0.55), 0 0 0 1px rgba(212,168,67,0.2), inset 0 1px 0 rgba(255,255,255,0.6), 0 0 60px rgba(212,140,40,0.15), 0 0 120px rgba(192,68,90,0.08); }
  33%      { box-shadow: 0 40px 80px rgba(0,0,0,0.55), 0 0 0 1px rgba(212,168,67,0.2), inset 0 1px 0 rgba(255,255,255,0.6), 0 0 80px rgba(212,140,40,0.22), 0 0 140px rgba(192,68,90,0.12); }
  66%      { box-shadow: 0 40px 80px rgba(0,0,0,0.55), 0 0 0 1px rgba(212,168,67,0.2), inset 0 1px 0 rgba(255,255,255,0.6), 0 0 45px rgba(212,140,40,0.10), 0 0 100px rgba(192,68,90,0.06); }
}

.quote-mark { font-family:'Playfair Display',serif; font-size:7rem; color:rgba(43,18,0,0.07); line-height:1; position:absolute; top:4px; left:18px; pointer-events:none; }
.wax-seal { position:absolute; bottom:20px; right:24px; width:52px; height:52px; border-radius:50%; background:radial-gradient(circle at 38% 35%,#e06080,#a02040); box-shadow:0 4px 12px rgba(160,32,64,0.4),inset 0 1px 0 rgba(255,255,255,0.2); display:flex; align-items:center; justify-content:center; font-size:1.4rem; }

/* ── letter body ── */
.letter-body { font-family:'Caveat',cursive; font-size:clamp(1.05rem,2.6vw,1.25rem); color:#2b1200; line-height:1.75; position:relative; z-index:1; }
.letter-body p { margin-bottom:1.4rem; }
.salutation { font-size:clamp(1.2rem,3vw,1.55rem); font-weight:700; color:#7a2338; margin-bottom:1.4rem; display:block; }
.bold { font-weight:700; color:#5a1a28; }

/* gold shimmer highlight */
.highlight {
  background:linear-gradient(120deg, rgba(212,168,67,0.3) 0%, rgba(212,168,67,0.15) 50%, rgba(212,168,67,0.3) 100%);
  background-size:200% auto;
  border-radius:4px; padding:0 4px;
  font-weight:700; color:#4a1a10;
  animation:shimmer 3s linear infinite;
}
@keyframes shimmer { to { background-position:200% center; } }

.section-break { display:block; width:60px; height:1px; background:linear-gradient(90deg,transparent,rgba(122,35,56,0.3),transparent); margin:1.4rem auto; }
.list-item { display:block; padding-left:1.2rem; position:relative; margin-bottom:0.3rem; color:#3d1408; }
.list-item::before { content:'❤️'; position:absolute; left:-0.2rem; font-size:0.75rem; top:3px; }
.sign-off { margin-top:2rem; text-align:right; font-size:clamp(1.1rem,2.8vw,1.35rem); font-weight:700; color:#7a2338; display:block; }
.sign-name { font-size:clamp(1.3rem,3.2vw,1.6rem); font-weight:700; color:#5a1a28; display:block; text-align:right; margin-top:0.3rem; }

/* ── floating petals ── */
.petal {
  position:fixed; top:-20px; font-size:1rem; opacity:0;
  animation:petalFall linear infinite;
  pointer-events:none; z-index:0; user-select:none;
}
@keyframes petalFall {
  0%   { transform:translateY(0) rotate(0deg);   opacity:0; }
  10%  { opacity:0.7; }
  90%  { opacity:0.4; }
  100% { transform:translateY(110vh) rotate(360deg); opacity:0; }
}

@keyframes fadeUp { from{opacity:0;transform:translateY(18px)} to{opacity:1;transform:none} }
</style>
</head>
<body>
<div class="bg-glow"></div>

<!-- petals -->
<div id="petals"></div>

<div class="content">
  <p class="eyebrow">a letter</p>
  <h1 class="page-title">For you, Anna. 🧡</h1>
  <p class="page-sub">written from the heart — every word true</p>
  <div class="thread-line"></div>

  <!-- ENVELOPE -->
  <div class="envelope-wrap" id="envWrap">
    <div>
      <div class="envelope" id="envelope" onclick="openEnvelope()">
        <div class="env-body"></div>
        <div class="env-flap" id="envFlap"></div>
        <div class="env-bottom"></div>
        <div class="env-left"></div>
        <div class="env-right"></div>
        <div class="letter-rising" id="letterRising"></div>
        <div class="env-seal" id="envSeal">🪢</div>
      </div>
      <p class="env-hint" id="envHint">tap to open 💌</p>
    </div>
  </div>

  <!-- LETTER -->
  <div class="letter-paper" id="letterPaper">
    <div class="quote-mark">"</div>
    <div class="wax-seal">🪢</div>
    <div class="letter-body">

      <span class="salutation">Dear Rupesh Anna, ❤️</span>

      <p>First ellathukum romba thanks anna. 🥹❤️</p>
      <p>Neenga en life la sudden ah vandhinga… but ivlo close ah aaguvom nu honestly enakke theriyadhu. Konjam konjam ah neenga enakku ivlo important person aayitinga.</p>
      <p>Ellar vidavum enna nalla understand pannadhu neenga mattum dha anna. En kooda irundha friends kooda sila nerathula enna purinjikama enna vittu poitaanga… but <span class="bold">neenga mattum dha</span>, naan sollama irundha vishayangal kooda purinjikitinga. Adhu enakku romba periya vishayam. 🥹</p>
      <p>En problems ah kooda unga problems ah paathinga. Enakkaga neenga avalo kasta padanum nu avasiyame illa anna… but still, enakkaga avalo pannirukinga. Adhuku naan evlo thanks sonnalum pathaadhu.</p>

      <span class="section-break"></span>

      <p><span class="highlight">You are always my comfort and my safe person. ❤️</span></p>
      <p>Unga kitta naan ellame solluven. Enna nadandhaalum, enna feel pannalum, unga kitta sollumbodhu oru safe feeling irukkum. Naan solradha vera yaar kittayum sollamaatinga, enna judge um panna maatinga nu enakku theriyum.</p>
      <p><span class="bold">Thanks anna, en life la vandhadhuku. ❤️</span></p>

      <span class="section-break"></span>

      <p>Mostly naan perfect ah irukka maaten… 😅<br>
      Neenga solradha kooda neraya time kekka maaten. Adhuku sorry anna. En mela kovama irundhaalum, <em>"enna sonnalum kekka maata"</em> nu en mela kochikadhinga. 🥹</p>
      <p>Naan kekkaama irukradhu unga mela respect illa nu illa. Sometimes en situation apdi irukkum… But <span class="bold">unga mela enakku naraiya respect irukku anna.</span></p>

      <span class="section-break"></span>

      <p>And one thing I really love about you…</p>
      <p><span class="highlight">Naan edhachum unga kitta ketta, "Edhuku?" nu kooda kekkaama panniduvinga.</span><br>
      Adhu enakku romba pudicha vishayam. 🥹<br>
      Ennaala words la explain panna mudiyadha alavukku, I'm really grateful for that, anna.</p>
      <p>En success la eppovume neenga irukanum. ❤️</p>
      <p>Adhe maari, unga good days la mattum illa… <span class="bold">unga bad days layum kandippa naan iruppen.</span><br>
      Neenga enakku evlo support ah irundhirukingalo, adhe maari unga life la ungalukku support ah irupan.</p>

      <span class="section-break"></span>

      <p>Because you are not just my brother, Anna.</p>
      <span class="list-item">En best friend.</span>
      <span class="list-item">En guide.</span>
      <span class="list-item">En confidence.</span>
      <span class="list-item">En comfort.</span>
      <span class="list-item">En safe place.</span>
      <span class="list-item">En supportive person.</span>
      <p style="margin-top:1.2rem;"><span class="bold">You are someone I adore a lot.</span></p>

      <span class="section-break"></span>

      <p>Mostly…</p>
      <p><span class="highlight">En life la enakku kedaicha one of the greatest blessings neenga. ❤️🥹</span></p>
      <p>Namma ore blood ah illaama irukkalaam.<br>Namma rendu perukkum distance irukkalaam.</p>
      <p>But honestly anna…</p>
      <p><span class="bold">Naan ungaala eppovume en kooda porandha brother-ah dhaan paakuren. ❤️</span></p>

      <span class="section-break"></span>

      <p><span class="bold">I miss you a lot, Anna. 🥹❤️</span></p>
      <p>And thank you…</p>
      <span class="list-item">En life la vandhadhuku.</span>
      <span class="list-item">Enna understand pannadhuku.</span>
      <span class="list-item">Enna judge pannama irundhadhuku.</span>
      <span class="list-item">Enakkaga ninnadhuku.</span>
      <span class="list-item">Enakku safe place ah irundhadhuku.</span>

      <p style="margin-top:1.4rem;font-size:clamp(1.15rem,3vw,1.45rem);font-weight:700;color:#7a2338;">
        Happy Raksha Bandhan, Rupesh Anna. 🪢❤️
      </p>
      <span class="sign-off">Love you so much, Anna. ❤️🥹</span>
      <span class="sign-name">— Swarna 🧡</span>

    </div>
  </div>
</div>

<script>
window.scrollTo(0,0);
// spawn petals
const petalEmojis = ['🌸','🌺','✨','🧡','💛'];
const container = document.getElementById('petals');
for(let i=0;i<18;i++){
  const p = document.createElement('div');
  p.className = 'petal';
  p.textContent = petalEmojis[i % petalEmojis.length];
  p.style.left = Math.random()*100 + 'vw';
  p.style.animationDuration = (6 + Math.random()*8) + 's';
  p.style.animationDelay = (Math.random()*10) + 's';
  p.style.fontSize = (0.7 + Math.random()*0.8) + 'rem';
  container.appendChild(p);
}

function openEnvelope() {
  const flap = document.getElementById('envFlap');
  const seal = document.getElementById('envSeal');
  const rising = document.getElementById('letterRising');
  const hint = document.getElementById('envHint');
  const paper = document.getElementById('letterPaper');
  const envWrap = document.getElementById('envWrap');

  // already opened
  if(flap.classList.contains('open')) return;

  hint.style.opacity = '0';
  seal.style.opacity = '0';
  flap.classList.add('open');

  setTimeout(() => { rising.classList.add('risen'); }, 500);

  setTimeout(() => {
    envWrap.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    envWrap.style.opacity = '0';
    envWrap.style.transform = 'translateY(-20px)';
  }, 1200);

  setTimeout(() => {
    envWrap.style.display = 'none';
    paper.classList.add('visible');
  }, 1700);
}
</script>
</body>
</html>
""", height=1900, scrolling=True)

    if st.button("The moment I've been building to →", key="s9_next", use_container_width=True):
        go(5)
