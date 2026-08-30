import streamlit as st

# ✏️ FILL IN your real inside jokes and funny moments
JOKES = [
    "[Inside joke 1 — something only you two understand]",
    "[Inside joke 2 — a phrase only you two use]",
    "[Funny moment — something that still makes you laugh]",
    "[A habit of his that's so typically him]",
    "[Something he always says / does]",
    "[A nickname or running joke between you two]",
]

FUNNY_STORY = "[Write a short funny story or moment here — the more specific, the better. Something that captures his personality perfectly.]"

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="scene">
      <div style="text-align:center; max-width:700px; padding:0 20px; width:100%;">

        <p style="font-family:'Lato',sans-serif; font-size:0.75rem; letter-spacing:0.35em;
                  text-transform:uppercase; color:rgba(212,168,67,0.65); margin-bottom:1rem;"
           class="fade-in">chapter three</p>

        <h2 class="title fade-in">The funny stuff. 😂</h2>
        <p class="subtitle fade-in" style="margin-bottom:2.5rem;">
          Because not everything has to be emotional.<br>
          (But also, this section will probably make you cringe.)
        </p>
    """, unsafe_allow_html=True)

    # chips row
    chips_html = '<div style="display:flex; flex-wrap:wrap; gap:12px; justify-content:center; margin-bottom:2rem;" class="fade-in">'
    for j in JOKES:
        chips_html += f"""
        <div style="padding:12px 20px; border-radius:14px;
                    background:rgba(245,230,200,0.06); border:1px solid rgba(245,230,200,0.12);
                    font-family:'Caveat',cursive; font-size:1.05rem; color:rgba(245,230,200,0.85);
                    cursor:default;">
          {j}
        </div>"""
    chips_html += "</div>"
    st.markdown(chips_html, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card fade-in" style="text-align:left;">
      <p style="font-family:'Lato',sans-serif; font-size:0.7rem; letter-spacing:0.2em;
                text-transform:uppercase; color:rgba(212,168,67,0.6); margin-bottom:0.8rem;">
        a story only we'd find funny
      </p>
      <p class="handwritten" style="font-size:1.15rem; color:rgba(245,230,200,0.88);">
        {FUNNY_STORY}
      </p>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Our scrapbook →", key="s4_next", use_container_width=True):
            go(5)
