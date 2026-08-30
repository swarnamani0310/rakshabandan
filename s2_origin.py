import streamlit as st

def render(go):
    st.markdown('<div class="festive-strip"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="scene">
      <div style="text-align:center; max-width:680px; padding:0 20px;">

        <p style="font-family:'Lato',sans-serif; font-size:0.75rem; letter-spacing:0.35em;
                  text-transform:uppercase; color:rgba(212,168,67,0.65); margin-bottom:1.5rem;"
           class="fade-in">chapter one</p>

        <h2 class="title fade-in">How it all started.</h2>

        <div class="thread fade-in"></div>

        <!-- PHOTO PLACEHOLDER -->
        <div class="photo-slot fade-in" style="max-width:480px; margin:1.5rem auto;">
          <span style="font-size:1.8rem;">📷</span>
          <span>photo of how/where you met</span>
        </div>

        <div class="card fade-in" style="margin-top:1.5rem; text-align:left;">
          <p class="handwritten" style="color:rgba(245,230,200,0.9); font-size:1.2rem;">
            <!-- ✏️ FILL IN: How you two met — the place, the moment, the first conversation -->
            [How we met — add your story here, Swarna. The place, the moment, what happened first.]
          </p>
        </div>

        <div class="card fade-in" style="margin-top:1.2rem; text-align:left;">
          <p style="font-family:'Lato',sans-serif; font-size:0.75rem; letter-spacing:0.2em;
                    text-transform:uppercase; color:rgba(212,168,67,0.6); margin-bottom:0.8rem;">
            the moment it shifted
          </p>
          <p class="handwritten" style="color:rgba(245,230,200,0.85); font-size:1.1rem;">
            <!-- ✏️ FILL IN: The moment you realized he felt like a brother -->
            [The moment you realized — this person is not just a friend. Add it here.]
          </p>
        </div>

      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("See our timeline →", key="s2_next", use_container_width=True):
            go(3)
