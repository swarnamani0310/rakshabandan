import streamlit as st
import streamlit.components.v1 as components
import base64, os

PHOTO = "pics/love.png"

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)

    img_tag = ""
    if os.path.exists(PHOTO):
        with open(PHOTO, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        ext = PHOTO.rsplit(".", 1)[-1].lower()
        mime = "image/jpeg" if ext in ("jpg","jpeg") else "image/png"
        img_tag = f'<img src="data:{mime};base64,{b64}" style="width:100%;max-width:560px;border-radius:16px;box-shadow:0 20px 60px rgba(0,0,0,0.5);display:block;margin:0 auto;" />'
    else:
        img_tag = '<div style="width:100%;max-width:560px;height:320px;border:2px dashed rgba(245,230,200,0.2);border-radius:16px;display:flex;align-items:center;justify-content:center;margin:0 auto;color:rgba(245,230,200,0.4);font-size:1.2rem;">📷 photo not found</div>'

    from PIL import Image as PILImage
    try:
        with PILImage.open(PHOTO) as im:
            w, h = im.size
        img_height = int(h * 560 / w) + 220
    except:
        img_height = 700

    components.html(f"""
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Caveat:wght@400;600&family=Lato:wght@300;400&display=swap" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#1a0a00; display:flex; flex-direction:column; align-items:center; padding:40px 20px 32px; font-family:'Lato',sans-serif; }}
.bg-glow {{ position:fixed; inset:0; z-index:0; pointer-events:none; background: radial-gradient(ellipse 60% 40% at 15% 10%, rgba(192,68,90,0.18), transparent 60%), radial-gradient(ellipse 50% 40% at 85% 20%, rgba(212,168,67,0.14), transparent 60%); }}
.content {{ position:relative; z-index:1; width:100%; max-width:680px; text-align:center; }}
.eyebrow {{ font-size:0.72rem; letter-spacing:0.35em; text-transform:uppercase; color:rgba(212,168,67,0.65); margin-bottom:0.8rem; animation:fadeUp 0.8s ease 0.1s both; }}
.title {{ font-family:'Playfair Display',serif; font-size:clamp(1.8rem,5vw,2.6rem); color:#f5e6c8; margin-bottom:0.4rem; animation:fadeUp 0.8s ease 0.2s both; }}
.sub {{ font-family:'Playfair Display',serif; font-style:italic; font-size:1rem; color:rgba(245,230,200,0.5); margin-bottom:2rem; animation:fadeUp 0.8s ease 0.3s both; }}
.photo-wrap {{ animation:fadeUp 1s ease 0.5s both; }}
.caption {{ font-family:'Caveat',cursive; font-size:1.25rem; color:rgba(245,230,200,0.85); margin-top:1rem; animation:fadeUp 1s ease 0.7s both; }}
@keyframes fadeUp {{ from {{ opacity:0; transform:translateY(18px); }} to {{ opacity:1; transform:none; }} }}
</style>
</head>
<body>
<div class="bg-glow"></div>
<div class="content">
  <p class="eyebrow"></p>
  <h1 class="title">Our scrapbook. 📸</h1>
  <p class="sub">One photo. But it holds everything.</p>
  <div class="photo-wrap">{img_tag}</div>
  <p class="caption">Us. 🧡 The only photo I have of us — and it's my favourite one.</p>
</div>
</body>
</html>
""", height=img_height, scrolling=False)

    if st.button("The distance between us →", key="s5_next", use_container_width=True):
        go(3)
