import streamlit as st

# ✏️ FILL IN your real memories here
MEMORIES = [
    {
        "year": "[Year]",
        "title": "[Memory 1 title]",
        "desc":  "[Describe what happened and why it mattered — add your real memory here]",
        "photo": None,   # set to "assets/photos/memory1.jpg" when ready
    },
    {
        "year": "[Year]",
        "title": "[Memory 2 title]",
        "desc":  "[Describe what happened and why it mattered]",
        "photo": None,
    },
    {
        "year": "[Year]",
        "title": "[Memory 3 title]",
        "desc":  "[Describe what happened and why it mattered]",
        "photo": None,
    },
    {
        "year": "[Year]",
        "title": "[Memory 4 title]",
        "desc":  "[Describe what happened and why it mattered]",
        "photo": None,
    },
    {
        "year": "[Year]",
        "title": "[Memory 5 title]",
        "desc":  "[Describe what happened and why it mattered]",
        "photo": None,
    },
]

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="scene" style="align-items:flex-start; padding-top:6vh;">
      <div style="max-width:680px; width:100%; margin:0 auto; padding:0 20px;">
        <p style="font-family:'Lato',sans-serif; font-size:0.75rem; letter-spacing:0.35em;
                  text-transform:uppercase; color:rgba(212,168,67,0.65); margin-bottom:1rem; text-align:center;"
           class="fade-in">chapter two</p>
        <h2 class="title fade-in" style="text-align:center; margin-bottom:0.5rem;">
          How we became <em>us</em>.
        </h2>
        <p class="subtitle fade-in" style="text-align:center; margin-bottom:3rem;">
          A few moments I never want to forget.
        </p>
    """, unsafe_allow_html=True)

    for i, m in enumerate(MEMORIES):
        delay = i * 0.15
        photo_html = ""
        if m["photo"]:
            photo_html = f'<img src="{m["photo"]}" style="width:100%;max-width:400px;border-radius:14px;margin:0.8rem 0;border:1px solid rgba(212,168,67,0.2);">'
        else:
            photo_html = """
            <div class="photo-slot" style="max-width:400px; margin:0.8rem 0; aspect-ratio:4/3;">
              <span style="font-size:1.4rem;">📷</span>
              <span>add a photo for this memory</span>
            </div>"""

        st.markdown(f"""
        <div class="tl-item" style="animation-delay:{delay}s; position:relative;">
          <div style="display:flex; flex-direction:column; align-items:center; flex-shrink:0;">
            <div class="tl-dot"></div>
            <div style="width:1px; flex:1; background:linear-gradient(180deg,rgba(212,168,67,0.4),transparent); min-height:40px;"></div>
          </div>
          <div style="flex:1;">
            <div class="tl-year">{m['year']}</div>
            <div class="tl-title">{m['title']}</div>
            {photo_html}
            <p class="tl-desc">{m['desc']}</p>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("The funny stuff →", key="s3_next", use_container_width=True):
            go(4)
