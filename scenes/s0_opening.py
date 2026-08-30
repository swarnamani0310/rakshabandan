import streamlit as st

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="scene" style="background:#1a0a00; min-height:100vh;">
      <div style="text-align:center; max-width:700px; padding:0 20px;">
        <p style="font-family:'Lato',sans-serif; font-size:0.8rem; letter-spacing:0.35em;
                  text-transform:uppercase; color:rgba(212,168,67,0.7); margin-bottom:2rem;
                  animation: fadeIn 1s ease 0.2s both;">
          a little world, made just for you
        </p>
        <p class="opening-text" style="animation-delay:0.6s;">
          Somewhere between Chennai and Vellore,<br>
          a sister sat down and built you<br>
          a small secret world.
        </p>
        <div class="thread" style="margin-top:2.5rem; animation: fadeIn 1s ease 1.8s both;"></div>
        <p style="font-family:'Playfair Display',serif; font-style:italic;
                  font-size:clamp(1rem,2.5vw,1.3rem); color:rgba(245,230,200,0.55);
                  margin-top:1.5rem; animation: fadeIn 1s ease 2.2s both;">
          This is for you, Rupesh Anna. 🧡
        </p>
        <p style="font-family:'Lato',sans-serif; font-size:0.8rem; letter-spacing:0.2em;
                  color:rgba(245,230,200,0.3); margin-top:3rem;
                  animation: fadeIn 1s ease 3s both;">
          — from Swarna, with a full heart
        </p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("✦  Enter  ✦", key="enter_btn", use_container_width=True):
            go(2)

    st.markdown("""
    <style>
    div[data-testid="stButton"] > button {
        background: transparent !important;
        border: 1px solid rgba(212,168,67,0.4) !important;
        color: rgba(245,230,200,0.8) !important;
        border-radius: 999px !important;
        padding: 14px 40px !important;
        font-family: 'Lato', sans-serif !important;
        letter-spacing: 0.2em !important;
        font-size: 0.9rem !important;
        transition: all 0.4s ease !important;
        animation: fadeIn 1s ease 3.4s both;
        width: 100% !important;
    }
    div[data-testid="stButton"] > button:hover {
        border-color: #d4a843 !important;
        background: rgba(212,168,67,0.1) !important;
        color: #f5e6c8 !important;
    }
    </style>
    """, unsafe_allow_html=True)
