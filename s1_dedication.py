import streamlit as st

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="scene">
      <div style="text-align:center; max-width:680px; padding:0 20px;">

        <p style="font-family:'Lato',sans-serif; font-size:0.75rem; letter-spacing:0.35em;
                  text-transform:uppercase; color:rgba(212,168,67,0.65); margin-bottom:2rem;"
           class="fade-in">
          dedicated to
        </p>

        <!-- PHOTO PLACEHOLDER -->
        <div style="width:180px; height:180px; border-radius:50%; margin:0 auto 2rem;
                    border:2px solid rgba(212,168,67,0.35);
                    box-shadow:0 0 40px rgba(212,168,67,0.15);
                    overflow:hidden; background:rgba(212,168,67,0.06);
                    display:flex; align-items:center; justify-content:center;
                    flex-direction:column; gap:6px;"
             class="fade-in">
          <span style="font-size:2rem;">📷</span>
          <span style="font-size:0.7rem; letter-spacing:0.12em; text-transform:uppercase;
                       color:rgba(212,168,67,0.4);">his photo</span>
        </div>

        <h1 class="title fade-in" style="font-size:clamp(2.2rem,7vw,4rem); margin-bottom:0.4rem;">
          Rupesh Kumar
        </h1>
        <p style="font-family:'Caveat',cursive; font-size:1.4rem; color:rgba(245,230,200,0.6);
                  margin-bottom:2rem;" class="fade-in">
          my Rupesh Anna 🧡
        </p>

        <div class="thread fade-in"></div>

        <p class="subtitle fade-in" style="margin-top:1.5rem;">
          Not born into my family.<br>
          Not written in any bloodline.<br>
          But somehow, the most brother-like person<br>
          I have ever known.
        </p>

        <p style="font-family:'Lato',sans-serif; font-size:0.8rem; letter-spacing:0.15em;
                  color:rgba(245,230,200,0.3); margin-top:2.5rem; text-transform:uppercase;"
           class="fade-in">
          Raksha Bandhan &middot; a bond chosen, not inherited
        </p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Our scrapbook →", key="s1_next", use_container_width=True):
            go(2)
