import streamlit as st

# Set page configuration
st.set_page_config(page_title="Fitness Info - Personal Fitness Tracker", layout="wide")

# Custom CSS for improved styling and centered content
custom_css = """
<style>
    /* Full Page Background with Pink Gradient */
    .stApp {
        background: linear-gradient(to right, #ffdde1, #ee9ca7);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Centered Content Box */
    .content-box {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 30px;
        width: 80%;
        max-width: 900px;
        text-align: center;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.3);
        margin: 20px auto;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Title Styling */
    h1, h2 {
        color: #d63384;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        text-align: center;
        font-weight: bold;
    }

    /* Properly Centered List */
    .styled-list {
        color: #4a4a4a;
        font-size: 1.1rem;
        line-height: 1.6;
        list-style: none; /* Remove default bullet points */
        padding: 0;
        width: 100%; /* Make it take full width */
        text-align: left; /* Keep text aligned properly */
    }

    .styled-list li {
        background: rgba(255, 255, 255, 0.6);
        margin: 10px 0;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        display: flex;
        align-items: center;
        justify-content: flex-start; /* Align items to start */
    }

    .styled-list li::before {
        content: "✔️";
        margin-right: 10px;
        color: #d63384;
        font-weight: bold;
    }

    /* Hover Effect */
    .styled-list li:hover {
        transform: scale(1.03);
        transition: all 0.3s ease-in-out;
        background: rgba(255, 255, 255, 0.8);
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Page Title
st.markdown('<h1>🔥 General Fitness Information</h1>', unsafe_allow_html=True)
st.markdown('<h2>🏋️‍♂️ Learn about different fitness routines and stay strong!</h2>', unsafe_allow_html=True)

# Centered Content Box
st.markdown('<div class="content-box">', unsafe_allow_html=True)

# Fitness Information List (Properly Structured & Centered)
st.markdown("""
<ul class="styled-list">
    <li><b>Strength Training</b>: Builds muscle, boosts metabolism, and strengthens bones.</li>
    <li><b>Cardio Workouts</b>: Improves heart health and burns calories.</li>
    <li><b>Flexibility & Mobility</b>: Prevents injuries and improves movement.</li>
    <li><b>Balanced Nutrition</b>: Fuels your body for better performance.</li>
    <li><b>Hydration</b>: Keeps you energized and improves focus.</li>
    <li><b>Recovery & Rest</b>: Essential for muscle growth and mental well-being.</li>
    <li><b>Common Fitness Myths Busted</b>: Understand facts vs. fiction.</li>
    <li><b>Stress Management & Mental Health</b>: Exercise helps reduce stress.</li>
    <li><b>Tracking Progress</b>: Keep a journal or use apps for motivation.</li>
    <li><b>Workout Routine & Tips</b>: Plan your workouts for better results.</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Closing div