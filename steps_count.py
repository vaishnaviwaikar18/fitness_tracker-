import streamlit as st
import random
from datetime import datetime, timedelta


st.set_page_config(page_title="🚶 Steps Tracker - Personal Fitness Tracker", layout="wide")


image_urls = [
    "https://source.unsplash.com/800x400/?walking,fitness",
    "https://source.unsplash.com/800x400/?running,exercise",
    "https://source.unsplash.com/800x400/?steps,shoes",
    "https://source.unsplash.com/800x400/?hiking,trail",
]


random_image = random.choice(image_urls)

custom_css = """
<style>
    .stApp {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        background-attachment: fixed;
        padding: 20px;
    }
    .content-box {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        width: 80%;
        max-width: 800px;
        text-align: center;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
        margin: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    h1, h2 {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        text-align: center;
        font-weight: bold;
        font-size: 2.5rem;
    }
    p, ul, ol, li {
        color: #f8f9fa;
        font-size: 1.3rem;
        text-align: center;
        font-weight: bold;
    }
    .steps-image {
        width: 100%;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    }
</style>
"""


st.markdown(custom_css, unsafe_allow_html=True)


st.markdown('<h1>🚶 Steps Tracker</h1>', unsafe_allow_html=True)
st.markdown('<h2>👣 Track your daily steps and stay active!</h2>', unsafe_allow_html=True)


st.image(random_image, use_column_width=True, caption="Stay Active, Keep Walking!")

st.markdown('<div class="content-box">', unsafe_allow_html=True)

st.write("""
### 📊 Why Track Your Steps?
- 🏃 Helps maintain a **healthy lifestyle**.
- ⚡ Boosts **energy levels** and **burns calories**.
- ❤️ Improves **heart health** and **stamina**.
- 📈 Encourages **daily movement** and keeps you motivated.

### 🎯 Daily Step Goals:
- Beginner: **5,000 steps/day**
- Moderate: **7,500 steps/day**
- Active: **10,000+ steps/day**
""")

st.write("### 🔢 Smart Step Tracker")
start_time = st.time_input("Start Time", value=datetime.now().time())
end_time = st.time_input("End Time", value=(datetime.now() + timedelta(hours=1)).time())

steps = st.number_input("🚶 Steps Walked:", min_value=0, max_value=50000, step=100)

if steps:
    if steps < 5000:
        st.warning("🔴 Try to walk more today! Every step counts.")
    elif 5000 <= steps < 10000:
        st.info("🟡 Good job! Keep pushing towards 10K.")
    else:
        st.success("🟢 Excellent! You're achieving your fitness goals!")


st.markdown("</div>", unsafe_allow_html=True)

st.success("🌿 Stay active, stay healthy! Keep stepping forward! 🚶💙")