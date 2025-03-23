import streamlit as st
import random


st.set_page_config(page_title="Workout Plan - Personal Fitness Tracker", layout="wide")


image_urls = [
    "https://source.unsplash.com/800x400/?workout,fitness",
    "https://source.unsplash.com/800x400/?exercise,training",
    "https://source.unsplash.com/800x400/?gym,weights",
    "https://source.unsplash.com/800x400/?yoga,stretching",
]


random_image = random.choice(image_urls)


custom_css = """
<style>
    /* Faint Blue Background */
    .stApp {
        background-color: #e0f7fa; /* Light blue color */
        color: #000; /* Default text color */
    }

    /* Dashboard Container */
    .dashboard-container {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }

    h1, h2 {
        text-align: center;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


st.image(random_image, use_container_width=True, caption="Stay Fit, Stay Strong!")  # Updated here


st.markdown("<h1>🏋️‍♂️ Workout Plan</h1>", unsafe_allow_html=True)
st.markdown('<div class="dashboard-container">Pick your workout routine:</div>', unsafe_allow_html=True)


workout_type = st.selectbox("Select workout type:", ["Cardio", "Strength Training", "Flexibility & Yoga"])


if workout_type == "Cardio":
    st.success("Try running, cycling, or HIIT for at least 30 minutes.")
    st.write("### Suggested Cardio Workouts:")
    st.write("- **Running**: Great for cardiovascular health.")
    st.write("- **Cycling**: Low-impact and excellent for leg strength.")
    st.write("- **HIIT**: High-Intensity Interval Training for maximum calorie burn.")
elif workout_type == "Strength Training":
    st.success("Focus on weight lifting and resistance exercises.")
    st.write("### Suggested Strength Workouts:")
    st.write("- **Squats**: Great for legs and core.")
    st.write("- **Deadlifts**: Excellent for overall strength.")
    st.write("- **Bench Press**: Focus on upper body strength.")
else:
    st.success("Include yoga and stretching for flexibility.")
    st.write("### Suggested Flexibility Workouts:")
    st.write("- **Hatha Yoga**: Great for beginners.")
    st.write("- **Vinyasa Yoga**: A more dynamic flow.")
    st.write("- **Static Stretching**: Essential for muscle recovery.")


st.markdown("<h2>💪 Keep pushing your limits!</h2>", unsafe_allow_html=True)
st.success("Stay consistent, and you'll see results! 🚀")

st.write("### Tips for a Successful Workout:")
st.write("- **Warm-up**: Always start with a warm-up to prevent injuries.")
st.write("- **Stay Hydrated**: Drink plenty of water before, during, and after your workout.")
st.write("- **Cool Down**: Finish with a cool-down to help your body recover.")

st.markdown("<h4>🌟 Remember, every step counts towards your fitness journey!</h4>", unsafe_allow_html=True)