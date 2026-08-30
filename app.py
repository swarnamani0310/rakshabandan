import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For Rupesh Anna 🧡",
    page_icon="🪢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "scene" not in st.session_state:
    st.session_state.scene = 0

def go(n):
    st.session_state.scene = n
    st.rerun()

# load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("animations.js") as f:
    st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)

# anchor at very top of DOM
st.markdown('<div id="page-top"></div>', unsafe_allow_html=True)

# scroll to top on every page load
st.markdown('''
<script>
function resetStreamlitScroll() {
  try { window.parent.scrollTo({ top: 0, behavior: 'auto' }); } catch (e) {}
  try {
    const view = window.parent.document.querySelector("[data-testid=stAppViewContainer]");
    if (view) view.scrollTop = 0;
  } catch (e) {}
  try { window.scrollTo(0, 0); document.documentElement.scrollTop = 0; document.body.scrollTop = 0; } catch (e) {}
}
resetStreamlitScroll();
window.addEventListener('load', resetStreamlitScroll, { once: true });
</script>
''', unsafe_allow_html=True)

scene = st.session_state.scene

if scene == 0:
    from scenes.s0_opening   import render; render(go)
elif scene == 1:
    from scenes.s1_dedication import render; render(go)
elif scene == 2:
    from scenes.s5_scrapbook import render; render(go)
elif scene == 3:
    from scenes.s7_distance  import render; render(go)
elif scene == 4:
    from scenes.s9_letter    import render; render(go)
elif scene == 5:
    from scenes.s10_ending   import render; render(go)
