import streamlit as st


st.set_page_config(page_title="🧘‍♂️ Meditation - Personal Fitness Tracker", layout="wide")

custom_css = """
<style>
    /* Smooth Gradient Background */
    .stApp {
        background: linear-gradient(to right, #ffafbd, #ffc3a0); /* Light pink gradient */
        background-attachment: fixed;
        padding: 20px;
    }

    /* Centered Content Box */
    .content-box {
        background: rgba(255, 255, 255, 0.9); /* Slightly more opaque for better readability */
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        width: 80%;
        max-width: 800px;
        text-align: center; /* Center text in the content box */
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
        margin: auto;
    }

    /* Title Styling */
    h1, h2 {
        color: #ffffff; /* Pure white for high contrast */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        text-align: center;
        font-weight: bold;
    }

    /* Text Styling */
    p, ul, ol, li {
        color: #333333; /* Darker color for better readability */
        font-size: 1.2rem; /* Adjusted font size for better readability */
        line-height: 1.5; /* Increased line height for better spacing */
    }

    /* List Styling */
    ul {
        list-style-type: disc; /* Use disc for bullet points */
        padding-left: 20px; /* Indent list items */
    }

    /* Section Spacing */
    .section {
        margin-bottom: 30px; /* Add space between sections */
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


st.markdown('<h1>🧘‍♂️ Meditation & Mindfulness</h1>', unsafe_allow_html=True)
st.markdown('<h2>🌿 Relax, breathe, and find your inner peace.</h2>', unsafe_allow_html=True)

st.markdown('<div class="content-box">', unsafe_allow_html=True)


st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("### 🌟 Benefits of Meditation:")
st.write("""
- 🧘 **Reduces stress and anxiety.**
- 🧠 **Improves concentration and focus.**
- 💖 **Enhances emotional well-being.**
- 😴 **Promotes better sleep and relaxation.**
""")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.write("### 🕰️ Try This Simple 5-Minute Meditation")
st.write("""
1. **Find a quiet, comfortable place to sit.**
2. **Close your eyes and take a deep breath in... and out.**
3. **Focus on your breath.** Feel the air entering and leaving your body.
4. **If thoughts come, let them pass** like clouds in the sky.
5. **Stay in this moment for a few minutes.** Feel the calmness.
""")
st.markdown('</div>', unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)


st.success("🌿 Take a deep breath, relax, and enjoy the moment! 💙")