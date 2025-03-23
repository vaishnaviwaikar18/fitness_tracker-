import streamlit as st

st.set_page_config(page_title="Dashboard - Personal Fitness Tracker", layout="wide")


dashboard_style = """
<style>
    body {
        background: linear-gradient(to right, #f8f9fa, #e9ecef); /* Soft Background */
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background: #ffffff;
        border-radius: 15px;
        padding: 20px;
    }
    h1 {
        text-align: center;
        color: #d81b60; /* Dark Pink */
        font-size: 3.5rem;
        text-shadow: 2px 2px 8px rgba(216, 27, 96, 0.3);
        padding-bottom: 15px;
        border-bottom: 4px solid #d81b60;
    }
    .dashboard-container {
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        padding: 20px;
        margin-bottom: 20px;
        background: rgba(245, 245, 245, 0.9);
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
    }
    .fitness-card {
        width: 80%;  /* Wider Cards */
        display: block;
        margin: 20px auto;  /* Centered */
        text-align: center;
        padding: 20px;
        font-size: 24px;
        font-weight: bold;
        background: linear-gradient(to bottom, #ffffff, #f8d7da);
        border-radius: 15px;
        border: 3px solid #d81b60;
        transition: 0.3s ease-in-out;
        box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.15);
        cursor: pointer;
    }
    .fitness-card:hover {
        transform: scale(1.05);
        background: linear-gradient(to bottom, #d81b60, #ffccd5);
        color: white;
    }
    .stButton>button {
        width: 100%;
        background: #d81b60;
        color: white;
        font-size: 22px;
        padding: 15px;
        border-radius: 10px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background: #b71c1c;
        transform: scale(1.05);
    }
</style>
"""
st.markdown(dashboard_style, unsafe_allow_html=True)

st.markdown("<h1>📊 Personal Fitness Tracker Dashboard</h1>", unsafe_allow_html=True)


st.markdown('<div class="dashboard-container">Welcome to your fitness dashboard! Choose an option below:</div>', unsafe_allow_html=True)


st.markdown('<div class="fitness-card">📏 BMI Calculator</div>', unsafe_allow_html=True)
if st.button("Go to BMI", key="bmi"):
    st.switch_page("pages/bmi.py")

st.markdown('<div class="fitness-card">🥗 Diet Plan</div>', unsafe_allow_html=True)
if st.button("Go to Diet Plan", key="diet"):
    st.switch_page("pages/diet_plan.py")

st.markdown('<div class="fitness-card">🏋️ Workout Plan</div>', unsafe_allow_html=True)
if st.button("Go to Workout", key="workout"):
    st.switch_page("pages/workout.py")

st.markdown('<div class="fitness-card">📖 Fitness Info</div>', unsafe_allow_html=True)
if st.button("Go to Fitness Info", key="fitness_info"):
    st.switch_page("pages/fitness_info.py")

st.markdown('<div class="fitness-card">🧘 Meditation Guide</div>', unsafe_allow_html=True)
if st.button("Go to Meditation", key="meditation"):
    st.switch_page("pages/meditation.py")

st.markdown('<div class="fitness-card">🔥 Calories Burned Tracker</div>', unsafe_allow_html=True)
if st.button("Go to Calories Tracker", key="calories"):
    st.switch_page("pages/calories.py")

st.markdown('<div class="fitness-card">🚶 Steps Count</div>', unsafe_allow_html=True)
if st.button("Go to Steps Count", key="steps"):
    st.switch_page("pages/steps_count.py")

st.markdown('<div class="fitness-card">🏋️‍♂️ Workout Tracker</div>', unsafe_allow_html=True)
if st.button("Go to Workout Tracker", key="workout_tracker"):
    st.switch_page("pages/workout.py")
