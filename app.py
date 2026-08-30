import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For Rupesh Anna 🧡",
    page_icon="🪢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read the HTML file
with open("ceremony.html", "r", encoding="utf-8") as f:
    html = f.read()

# Display the website
components.html(
    html,
    height=1000,
    scrolling=True
)
