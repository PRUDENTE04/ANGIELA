import base64
import plotly.express as px
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


img = get_img_as_base64("download.jfif")
page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-size: 110%;
    background-attachment: local;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: left; 
    background-repeat: no-repeat;
    background-size: 150%;
    background-attachment: local;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("i1.png")
img_lottie_animation = Image.open("image1.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, Angiela Prudente :wave:")
    st.title("A BSCpE Student from SNSU")
    st.write(
        "Embrace the challenge, code your dreams."
    )
    st.write("[Learn More >](https://www.facebook.com/jella.etnedurp)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Women Empowerment")
        st.write("##")
        st.write(
            """
            On my Facebook Page, I posted Empowering Women for their freedom.
            - The uniqueness lies in celebrating the strenght
            - Reselience and achievements of women.
            - Fostering inclusivity and advocating for gender equality.
            - It's about uplifting women to reaize their full potential and creating a more equitable world."

            If you are interesting to to this content, consider liking and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[Facebook Page >](https://github.com/PRUDENTE04/ANGIELA)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Video Suggestion")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Female Empowerment")
        st.write(
            """
            Female empowerment is distinctive in its focus on elevating women's voices, rights, and opportunities. 
            It revolves around creating a platform for women to thrive, fostering leadership,
              breaking societal barriers,and promoting inclusivity and equality across various domains.
            It's about enabling women to embrace their strengths, achieve their aspirations, and contribute
            meaningfully to society without limitations based on gender

            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=PC0Zx7VxxNg)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Advocacy Campaingn Violence")
        st.write(
            """
           Advocacy campaigns against violence are crucial for raising awareness, educating communities, and promoting change. 
           Whether it's addressing domestic violence, bullying, or societal aggression, such campaigns aim to foster empathy, 
           encourage intervention, and push for policy reforms to create safer environments for everyone.

            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=rP_Y_S87Tpo&t=5s)")

  # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
contact_form = """
            <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
left_column, right_column = st.columns(2)
with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
                st.empty()