import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
import base64


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="KGF Heritage Explorer: A prototype website (creator: [🐙 GitHub] nh3342)",
    page_icon="🪔",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS (Background, Animations, Sidebar, Gold Theme)
# ---------------------------------------------------

def get_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


bg_base64 = get_base64("assets/background/bg.jpg")

st.markdown(
    f"""
    <style>

        /* PARALLAX BACKGROUND */
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* SIDEBAR DARK GOLD THEME */
        [data-testid="stSidebar"] {{
            background-color: #1a1408 !important;
            border-right: 2px solid #8a6d2c;
        }}
        [data-testid="stSidebar"] * {{
            color: #f7d07a !important;
        }}

        /* HEADER BANNER */
        .banner {{
            width: 100%;
            padding: 50px 0;
            text-align: center;
            background: linear-gradient(90deg, #8a6d2c, #e7c065, #8a6d2c);
            color: black;
            font-size: 40px;
            font-weight: 900;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
        }}

        /* Frosted Content Box */
        .content-box {{
            background: rgba(0, 0, 0, 0.65);
            padding: 25px;
            border-radius: 20px;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            animation: fadeIn 1s ease-in-out;
        }}

        /* Fade-in Animation */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(15px); }}
            to {{ opacity: 1; transform: translateY(0px); }}
        }}

        /* GOLD TITLE */
        .section-title {{
            font-size: 28px;
            font-weight: 700;
            color: #f7d07a;
            margin-bottom: 10px;
        }}

        /* FLOATING GOLDIE CHATBOT BUTTON */
        .goldie-button {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: #f7d07a;
            color: black;
            padding: 18px;
            border-radius: 50%;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            cursor: pointer;
            z-index: 9999;
            transition: transform 0.2s ease;
        }}
        .goldie-button:hover {{
            transform: scale(1.1);
        }}

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# HEADER BANNER
# ---------------------------------------------------
st.markdown("<div class='banner'>KGF HERITAGE EXPLORER</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# MAIN NAVIGATION
# ---------------------------------------------------
page = st.sidebar.radio(
    "Explore",
    ["Articles", "Maps & Resources", "Videos & Audio"]
)


# ---------------------------------------------------
# PAGE: ARTICLES
# ---------------------------------------------------
if page == "Articles":
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>📚 Featured Article</div>", unsafe_allow_html=True)

    article_path = Path("assets/articles/article.html")

    if article_path.exists():
        with open(article_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Render full HTML with CSS + JS
        components.html(html_content, height=2200, scrolling=True)
    else:
        st.error("article.html not found in assets/articles/")
    st.markdown("</div>", unsafe_allow_html=True)



# ---------------------------------------------------
# PAGE: MAPS & RESOURCES
# ---------------------------------------------------
elif page == "Maps & Resources":
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>🗺️ Interactive Maps & Downloads</div>", unsafe_allow_html=True)

    st.markdown("### 🎥 Kotilingeshwara Temple From Space")
    st.video("assets/maps/KGF_Google_Earth_ZOOM-Video.mp4")
    st.divider()

    st.markdown("### 📍 Open Interactive Map (Requires Sign in)")
    st.link_button(
        "KGF Historical Landmarks Map",
        "https://padlet.com/baakia560/kgf-heritage-explorer-18wq7s2fsisaalil"
    )

    st.divider()

    st.markdown("### 📱 QR Code : KGF Historical Landmarks Map (Requires Sign In)")
    st.image("assets/maps/KGF_Landmarks_QR.png", width=250)

    st.divider()
    st.markdown("### KGF Historical Landmarks PDF")
    pdf_file = Path("assets/maps/Padlet - KGF Historical Landmarks.pdf")
    with open(pdf_file, "rb") as f:
        st.download_button(
            "📥 Download KGF Historical PDF",
            data=f,
            file_name="KGF_Historical_Landmarks.pdf",
            mime="application/pdf"
        )

    st.divider()

    st.markdown("</div>", unsafe_allow_html=True)



# ---------------------------------------------------
# PAGE: VIDEOS & AUDIO
# ---------------------------------------------------
elif page == "Videos & Audio":
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>🎧 Voices & Videos of KGF</div>", unsafe_allow_html=True)

    st.markdown("### 🎥 Cornish Miners in KGF")
    st.video("https://youtu.be/88fcVkFJ6n8")

    st.divider()

    st.markdown("### 🎧 Audio Stories")

    st.markdown("#### 🇮🇳 Tamil — Cornish Miners in KGF")
    st.audio("assets/videos/TTS_Tamil_Audio.mp3")

    st.divider()

    st.markdown("#### 🇮🇳 Hindi — Cornish Miners in KGF")
    st.audio("assets/videos/Hindi_TTS_Audio.mp3")

    st.markdown("</div>", unsafe_allow_html=True)



# ---------------------------------------------------
# FLOATING CHATBOT BUTTON
# ---------------------------------------------------
st.markdown(
    """
    <div class="goldie-button">AI Chat</div>
    """,
    unsafe_allow_html=True
)
