import streamlit as st

# ✏️ FILL IN: things you never say enough to Rupesh Anna
ENVELOPES = [
    {
        "label": "Thing 1",
        "icon":  "💛",
        "text":  "[Something you will always thank him for — add your real words here]",
    },
    {
        "label": "Thing 2",
        "icon":  "🛡️",
        "text":  "[A time he showed up when it really mattered]",
    },
    {
        "label": "Thing 3",
        "icon":  "🌙",
        "text":  "[Something he does that you quietly appreciate but never tell him]",
    },
    {
        "label": "Thing 4",
        "icon":  "😤",
        "text":  "[Something that annoys you but you'd miss if it was gone]",
    },
    {
        "label": "Thing 5",
        "icon":  "🤍",
        "text":  "[The most important thing you want him to know]",
    },
]

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="scene">
      <div style="text-align:center; max-width:700px; padding:0 20px; width:100%;">
        <p style="font-family:'Lato',sans-serif; font-size:0.75rem; letter-spacing:0.35em;
                  text-transform:uppercase; color:rgba(212,168,67,0.65); margin-bottom:1rem;"
           class="fade-in">chapter five</p>
        <h2 class="title fade-in">Things I never say enough.</h2>
        <p class="subtitle fade-in" style="margin-bottom:2.5rem;">
          Tap each one. They're for you.
        </p>
    """, unsafe_allow_html=True)

    if "open_env" not in st.session_state:
        st.session_state.open_env = None

    cols = st.columns(3, gap="small")
    for i, env in enumerate(ENVELOPES):
        with cols[i % 3]:
            if st.button(f"{env['icon']}\n{env['label']}", key=f"env_{i}", use_container_width=True):
                if st.session_state.open_env == i:
                    st.session_state.open_env = None
                else:
                    st.session_state.open_env = i

    if st.session_state.open_env is not None:
        env = ENVELOPES[st.session_state.open_env]
        st.markdown(f"""
        <div class="card fade-in" style="margin-top:1.5rem; text-align:center;">
          <div style="font-size:2.5rem; margin-bottom:0.8rem;">{env['icon']}</div>
          <p class="handwritten" style="font-size:1.2rem; color:rgba(245,230,200,0.9);">
            {env['text']}
          </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("The distance between us →", key="s6_next", use_container_width=True):
            go(7)
