import streamlit as st
import streamlit.components.v1 as components
import os

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)

    html_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ceremony.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # inject scroll-to-top at very start of body and force the parent app to reset too
    html = html.replace(
        "<body>",
        "<body onload=\"try{window.scrollTo(0,0);document.documentElement.scrollTop=0;document.body.scrollTop=0;}catch(e){};try{window.parent.scrollTo({top:0,behavior:'auto'});var app=window.parent.document.querySelector('[data-testid=stAppViewContainer]'); if(app) app.scrollTop=0;}catch(e){}\">"
    )

    components.html(html, height=1600, scrolling=False)

    if st.button("↩  Back to the beginning", key="s10_back", use_container_width=True):
        go(0)
