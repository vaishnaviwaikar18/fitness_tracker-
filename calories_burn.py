import streamlit as st


st.set_page_config(page_title="🔥 Calories Burned Tracker", layout="wide")

custom_css = """
<style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(to right, #6dd5ed, #2193b0); /* Sky Blue Gradient */
        background-attachment: fixed;
        padding: 20px;
    }

    /* Content Box with Glassmorphism */
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

    /* Title Styling */
    h1, h2 {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        text-align: center;
        font-weight: bold;
        font-size: 2.5rem;
    }

    /* Text Styling */
    p, ul, ol, li {
        color: #ffebcd; /* Soft Cream Color for Better Contrast */
        font-size: 1.2rem;
        text-align: center;
        font-weight: bold;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #ff6f61;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: #ff4f41;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.markdown('<h1>🔥 Calories Burned </h1>', unsafe_allow_html=True)
st.markdown('<h2>💪 Track your workouts and burn those calories!</h2>', unsafe_allow_html=True)


st.markdown('<div class="content-box">', unsafe_allow_html=True)

st.write("## 🔥 What are Calories?")
st.write("Calories are a measure of energy. Your body needs them for daily functions, workouts, and overall activity.")

st.write("## 🏃‍♂️ How are Calories Burned?")
st.write(
    """
    Calories are burned through various activities:
    - **🏃‍♂️ Aerobic Exercises**: Running, cycling, swimming.
    - **🏋️ Strength Training**: Weightlifting, resistance exercises.
    - **🚶 Daily Activities**: Walking, cleaning, and standing.
    """
)

st.write("## 📊 Track Your Workouts Below!")

exercise_type = st.selectbox("Select Exercise Type:", ["Running", "Cycling", "Swimming", "Weightlifting", "Yoga"])
duration = st.number_input("Enter Duration (minutes):", min_value=1)


if st.button("🔥 Calculate Calories Burned"):
    calories_per_minute = {
        "Running": 10,
        "Cycling": 8,
        "Swimming": 7,
        "Weightlifting": 6,
        "Yoga": 4,
    }
    calories_burned = calories_per_minute[exercise_type] * duration
    st.success(f"🔥 You burned approximately **{calories_burned} calories** during **{duration} minutes** of **{exercise_type}**!")


st.write("## 🏆 Tips for Effective Workouts")
st.write(
    """
    - ✅ **Stay Hydrated**: Drink water before, during, and after your workout.
    - ✅ **Warm-Up & Cool Down**: Always stretch before and after exercising.
    - ✅ **Listen to Your Body**: Take rest if you feel discomfort.
    """
)


st.markdown("</div>", unsafe_allow_html=True)

st.success("💪 Stay consistent and track your progress! 🚀")
