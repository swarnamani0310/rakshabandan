import streamlit as st

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    /* ── ceremony stage ── */
    .ceremony-wrap {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        padding: 2rem 0;
    }

    /* wrist + hands container */
    .wrist-stage {
        position: relative;
        width: min(420px, 88vw);
        height: 260px;
        margin: 0 auto;
    }

    /* brother's wrist / arm */
    .bro-arm {
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 160px;
        height: 90px;
        background: linear-gradient(160deg, #c8956c, #a0714a);
        border-radius: 50px 50px 30px 30px;
        box-shadow: inset 0 -6px 12px rgba(0,0,0,0.25), 0 8px 24px rgba(0,0,0,0.4);
    }
    /* wrist crease lines */
    .bro-arm::after {
        content: '';
        position: absolute;
        bottom: 22px; left: 20px; right: 20px;
        height: 1px;
        background: rgba(0,0,0,0.15);
        border-radius: 50%;
    }

    /* sister's hand (enters from top-left) */
    .sis-hand {
        position: absolute;
        top: 0; left: -20px;
        width: 130px;
        animation: handApproach 2s cubic-bezier(.22,.61,.36,1) 0.8s both;
    }
    @keyframes handApproach {
        from { transform: translate(-60px, -80px) rotate(-25deg); opacity: 0; }
        to   { transform: translate(0,0) rotate(0deg); opacity: 1; }
    }

    /* rakhi on wrist — appears after hand arrives */
    .rakhi-on-wrist {
        position: absolute;
        bottom: 52px;
        left: 50%;
        transform: translateX(-50%);
        width: 56px;
        opacity: 0;
        animation: rakhiAppear 0.8s ease 2.6s forwards;
    }
    @keyframes rakhiAppear {
        from { opacity: 0; transform: translateX(-50%) scale(0.5); }
        to   { opacity: 1; transform: translateX(-50%) scale(1); }
    }

    /* thread wrap lines */
    .thread-wrap {
        position: absolute;
        bottom: 44px;
        left: 50%;
        transform: translateX(-50%);
        width: 130px;
        height: 20px;
        opacity: 0;
        animation: threadAppear 0.6s ease 3.2s forwards;
    }
    @keyframes threadAppear {
        from { opacity: 0; }
        to   { opacity: 1; }
    }

    /* hearts burst */
    .hearts {
        position: absolute;
        top: 30px; left: 50%;
        transform: translateX(-50%);
        font-size: 1.4rem;
        opacity: 0;
        animation: heartsBurst 1s ease 3.6s forwards;
        pointer-events: none;
        white-space: nowrap;
        letter-spacing: 6px;
    }
    @keyframes heartsBurst {
        0%   { opacity: 0; transform: translateX(-50%) translateY(0) scale(0.5); }
        50%  { opacity: 1; transform: translateX(-50%) translateY(-20px) scale(1.1); }
        100% { opacity: 0.7; transform: translateX(-50%) translateY(-30px) scale(1); }
    }

    /* emotional message */
    .ceremony-msg {
        opacity: 0;
        animation: fadeIn 1.4s ease 4.2s forwards;
        text-align: center;
        max-width: 520px;
    }

    /* hand away */
    .sis-hand-away {
        animation: handApproach 2s cubic-bezier(.22,.61,.36,1) 0.8s both,
                   handAway 1s cubic-bezier(.22,.61,.36,1) 3.8s forwards !important;
    }
    @keyframes handAway {
        from { transform: translate(0,0) rotate(0deg); opacity: 1; }
        to   { transform: translate(-80px,-60px) rotate(-20deg); opacity: 0; }
    }
    </style>

    <div class="scene">
      <div class="ceremony-wrap" style="max-width:680px; width:100%; padding:0 20px;">

        <p style="font-family:'Lato',sans-serif; font-size:0.75rem; letter-spacing:0.35em;
                  text-transform:uppercase; color:rgba(212,168,67,0.65); margin-bottom:0.5rem;"
           class="fade-in">the moment</p>

        <h2 class="title fade-in" style="margin-bottom:0.5rem;">
          Your Rakhi. 🪢
        </h2>
        <p class="subtitle fade-in" style="margin-bottom:1.5rem;">
          I couldn't be there. So close your eyes for a second.<br>
          Pretend I am.
        </p>

        <!-- CEREMONY STAGE -->
        <div class="wrist-stage fade-in">

          <!-- brother's arm/wrist -->
          <div class="bro-arm"></div>

          <!-- sister's hand SVG (bangles + mehendi + rakhi) -->
          <div class="sis-hand sis-hand-away">
            <svg viewBox="0 0 130 160" fill="none" xmlns="http://www.w3.org/2000/svg">
              <!-- palm -->
              <ellipse cx="65" cy="100" rx="42" ry="55"
                       fill="#c8956c" stroke="#a0714a" stroke-width="1"/>
              <!-- fingers -->
              <rect x="30" y="30" width="16" height="55" rx="8" fill="#c8956c" stroke="#a0714a" stroke-width="1"/>
              <rect x="50" y="18" width="16" height="65" rx="8" fill="#c8956c" stroke="#a0714a" stroke-width="1"/>
              <rect x="70" y="20" width="16" height="63" rx="8" fill="#c8956c" stroke="#a0714a" stroke-width="1"/>
              <rect x="90" y="30" width="14" height="55" rx="7" fill="#c8956c" stroke="#a0714a" stroke-width="1"/>
              <!-- thumb -->
              <ellipse cx="18" cy="90" rx="10" ry="22" fill="#c8956c" stroke="#a0714a" stroke-width="1"
                       transform="rotate(-20 18 90)"/>
              <!-- bangles -->
              <ellipse cx="65" cy="148" rx="40" ry="7" fill="none" stroke="#d4a843" stroke-width="3"/>
              <ellipse cx="65" cy="140" rx="40" ry="7" fill="none" stroke="#c0445a" stroke-width="2.5"/>
              <ellipse cx="65" cy="133" rx="40" ry="7" fill="none" stroke="#e8732a" stroke-width="2"/>
              <!-- mehendi dots -->
              <circle cx="55" cy="80" r="3" fill="#7a3a10" opacity="0.6"/>
              <circle cx="65" cy="70" r="3" fill="#7a3a10" opacity="0.6"/>
              <circle cx="75" cy="80" r="3" fill="#7a3a10" opacity="0.6"/>
              <circle cx="60" cy="95" r="2.5" fill="#7a3a10" opacity="0.5"/>
              <circle cx="70" cy="95" r="2.5" fill="#7a3a10" opacity="0.5"/>
              <!-- rakhi in hand -->
              <circle cx="65" cy="55" r="14" fill="#e8732a" opacity="0.9"/>
              <circle cx="65" cy="55" r="6"  fill="#f3cd6e"/>
              <circle cx="65" cy="41" r="5"  fill="#c0445a"/>
              <circle cx="75" cy="44" r="5"  fill="#c0445a"/>
              <circle cx="79" cy="55" r="5"  fill="#c0445a"/>
              <circle cx="75" cy="66" r="5"  fill="#c0445a"/>
              <circle cx="65" cy="69" r="5"  fill="#c0445a"/>
              <circle cx="55" cy="66" r="5"  fill="#c0445a"/>
              <circle cx="51" cy="55" r="5"  fill="#c0445a"/>
              <circle cx="55" cy="44" r="5"  fill="#c0445a"/>
            </svg>
          </div>

          <!-- rakhi tied on wrist (appears after hand) -->
          <div class="rakhi-on-wrist">
            <svg viewBox="0 0 56 56" fill="none">
              <circle cx="28" cy="28" r="14" fill="#e8732a"/>
              <circle cx="28" cy="28" r="6"  fill="#f3cd6e"/>
              <circle cx="28" cy="14" r="5"  fill="#c0445a"/>
              <circle cx="38" cy="17" r="5"  fill="#c0445a"/>
              <circle cx="42" cy="28" r="5"  fill="#c0445a"/>
              <circle cx="38" cy="39" r="5"  fill="#c0445a"/>
              <circle cx="28" cy="42" r="5"  fill="#c0445a"/>
              <circle cx="18" cy="39" r="5"  fill="#c0445a"/>
              <circle cx="14" cy="28" r="5"  fill="#c0445a"/>
              <circle cx="18" cy="17" r="5"  fill="#c0445a"/>
            </svg>
          </div>

          <!-- thread wrap -->
          <div class="thread-wrap">
            <svg viewBox="0 0 130 20" fill="none">
              <path d="M 0 10 Q 32 2 65 10 Q 98 18 130 10"
                    stroke="#d4a843" stroke-width="2.5" stroke-linecap="round"/>
              <path d="M 0 14 Q 32 6 65 14 Q 98 22 130 14"
                    stroke="#c0445a" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
            </svg>
          </div>

          <!-- hearts burst -->
          <div class="hearts">🧡 ✨ 💛 ✨ 🧡</div>

        </div>
        <!-- end wrist-stage -->

        <!-- emotional message -->
        <div class="ceremony-msg">
          <div class="thread" style="margin-bottom:1.5rem;"></div>
          <p class="handwritten" style="font-size:clamp(1.2rem,3vw,1.6rem);
                                        color:rgba(245,230,200,0.95); line-height:1.8;">
            There. ❤️
          </p>
          <p class="handwritten" style="font-size:clamp(1rem,2.5vw,1.3rem);
                                        color:rgba(245,230,200,0.75); margin-top:0.8rem; line-height:1.8;">
            I know it's not the same as being there.<br>
            But for a second — pretend I was.
          </p>
          <p style="font-family:'Lato',sans-serif; font-size:0.8rem; letter-spacing:0.15em;
                    color:rgba(245,230,200,0.35); margin-top:1.5rem; text-transform:uppercase;">
            tied with love, from Chennai 🧡
          </p>
        </div>

      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Read my letter →", key="s8_next", use_container_width=True):
            go(9)
