import streamlit as st


st.set_page_config(page_title="BMI Calculator - Personal Fitness Tracker", layout="wide")

bmi_css = """
<style>
    /* Set Background Image */
    .stApp {
        background: url('https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b') no-repeat center center fixed;
        background-size: cover;
    }

    /* Header - Bigger & More Visible */
    h1 {
        text-align: center;
        color: #ffffff;
        font-size: 4rem;  /* Increased font size */
        font-weight: bold;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.6);
        padding: 20px;
    }

    /* Container for Inputs */
    .bmi-container {
        background: rgba(0, 0, 0, 0.85);
        padding: 40px;
        border-radius: 12px;
        max-width: 700px;
        margin: 0 auto;
        text-align: center;
        box-shadow: 6px 6px 18px rgba(0, 0, 0, 0.6);
    }

    /* Input Labels - Larger */
    .input-label {
        font-size: 2.5rem;  /* Increased font size */
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 15px;
    }

    /* Input Fields - Bigger Text */
    .stTextInput input, .stNumberInput input {
        font-size: 2rem !important;  /* Increased font size */
        padding: 15px;
        text-align: center;
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
    }

    /* Button Styling - Bigger & Bolder */
    .stButton>button {
        width: 100%;
        background: #ff5733;
        color: white;
        font-size: 2.5rem;  /* Bigger button text */
        padding: 18px;
        border-radius: 12px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s ease;
        text-transform: uppercase;
    }

    .stButton>button:hover {
        background: #e64a19;
        transform: scale(1.08);
    }

    /* BMI Result Box - Bigger Text */
    .result-box {
        background: rgba(255, 255, 255, 0.2);
        padding: 30px;
        border-radius: 12px;
        margin-top: 25px;
        font-size: 4rem;  /* Increased font size */
        font-weight: bold;
        text-align: center;
        color: white;
    }

    /* Category Message - Bigger & More Noticeable */
    .category-message {
        font-size: 3rem;  /* Increased size */
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
</style>
"""
st.markdown(bmi_css, unsafe_allow_html=True)


st.markdown("<h1>📏 BMI Calculator</h1>", unsafe_allow_html=True)

st.markdown('<div class="bmi-container">', unsafe_allow_html=True)

st.markdown('<p class="input-label">Enter your height (in cm):</p>', unsafe_allow_html=True)
height = st.number_input("", min_value=50, max_value=250, step=1)

st.markdown('<p class="input-label">Enter your weight (in kg):</p>', unsafe_allow_html=True)
weight = st.number_input("", min_value=10, max_value=200, step=1)

st.markdown("</div>", unsafe_allow_html=True)


if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.markdown(f'<div class="result-box">Your BMI is: <span style="color:#00c9ff;">{bmi:.2f}</span></div>', unsafe_allow_html=True)

        category_message = ""
        if bmi < 18.5:
            category_message = "⚠️ You are underweight. Consider a healthy diet."
        elif 18.5 <= bmi < 24.9:
            category_message = "✅ You have a normal weight. Keep it up! 🎉"
        elif 25 <= bmi < 29.9:
            category_message = "⚠️ You are overweight. Consider a fitness plan."
        else:
            category_message = "🚨 You are in the obese category. Consult a professional."

        
        st.markdown(f'<div class="category-message">{category_message}</div>', unsafe_allow_html=True)
