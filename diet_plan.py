import streamlit as st


st.set_page_config(page_title="Diet Plan - Personal Fitness Tracker", layout="wide")


background_css = """
<style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
        background-size: cover;
        background-attachment: fixed;
    }
    .diet-container {
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(15px);
        padding: 40px;
      
        max-width: 600px;
        margin: auto;
        text-align: center;
        
    }
    h1 {
        text-align: center;
        color: #000000;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: none;
        padding: 20px;
    }
    .input-label {
        font-size: 5rem;
        font-weight: bold;
        color: black;
        padding: 10px;
        text-align: center;
    }
    .diet-box {
        background: rgba(255, 255, 255, 0.6);
        padding: 30px;
        border-radius: 20px;
        margin-top: 20px;
        font-size: 1.3rem;
        font-weight: bold;
        text-align: center;
        color: black;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(0, 0, 0, 0.3);
        max-width: 500px;
        margin: auto;
    }
</style>
"""

st.markdown(background_css, unsafe_allow_html=True)


st.markdown("<h1>🥗 Diet Plan</h1>", unsafe_allow_html=True)


st.markdown('<div class="diet-container">', unsafe_allow_html=True)

st.markdown('<p class="input-label">Choose your goal:</p>', unsafe_allow_html=True)
goal = st.selectbox("", ["Weight Loss", "Muscle Gain", "Maintain Weight", "Improve Nutrition"], label_visibility="collapsed")

st.markdown('<p class="input-label">Select your diet type:</p>', unsafe_allow_html=True)
diet_type = st.selectbox("", ["Vegetarian", "Non-Vegetarian", "Vegan", "Keto", "Balanced Diet"], label_visibility="collapsed")

st.markdown("</div>", unsafe_allow_html=True)

if goal and diet_type:
    diet_message = ""

    if goal == "Weight Loss":
        if diet_type == "Vegetarian":
            diet_message = """
            🥦 **Weight Loss Diet Plan (Vegetarian)**  
            - **Breakfast:** Oats with nuts and fruits OR a vegetable smoothie.  
            - **Mid-morning Snack:** Handful of almonds and green tea.  
            - **Lunch:** Dal, brown rice, sabzi, and salad with a buttermilk drink.  
            - **Evening Snack:** Sprouts chaat or Greek yogurt with flaxseeds.  
            - **Dinner:** Light salad with quinoa OR vegetable soup.  
            
            ✅ **Avoid:** Sugar, fried food, and refined carbs.  
            ✅ **Drink:** At least 3 liters of water daily.  
            """
        elif diet_type == "Non-Vegetarian":
            diet_message = """
            🐟 **Weight Loss Diet Plan (Non-Vegetarian)**  
            - **Breakfast:** Scrambled eggs with avocado OR boiled eggs with brown bread.  
            - **Mid-morning Snack:** Black coffee with nuts.  
            - **Lunch:** Grilled chicken/fish with sautéed veggies & quinoa.  
            - **Evening Snack:** Low-fat cottage cheese or protein shake.  
            - **Dinner:** Light grilled fish/chicken with a green salad.  
            
            ✅ **Avoid:** Red meat, fried food, and sugary drinks.  
            ✅ **Hydrate:** At least 3 liters of water.  
            """

    
    elif goal == "Muscle Gain":
        if diet_type == "Vegetarian":
            diet_message = """
            💪 **Muscle Gain Diet Plan (Vegetarian)**  
            - **Breakfast:** Paneer paratha with yogurt OR oats with peanut butter.  
            - **Mid-morning Snack:** Banana shake with whey protein.  
            - **Lunch:** Dal, brown rice, sabzi, and sweet potato.  
            - **Evening Snack:** Almonds, walnuts, and protein shake.  
            - **Dinner:** Chickpea salad with Greek yogurt OR cottage cheese stir-fry.  
            
            ✅ **Include:** Protein-rich foods like tofu, soya, and dairy.  
            ✅ **Strength training** is key for muscle gain.  
            """
        elif diet_type == "Non-Vegetarian":
            diet_message = """
            🥩 **Muscle Gain Diet Plan (Non-Vegetarian)**  
            - **Breakfast:** Egg omelet with whole-wheat toast.  
            - **Mid-morning Snack:** Whey protein shake and nuts.  
            - **Lunch:** Grilled chicken/fish with brown rice and vegetables.  
            - **Evening Snack:** Boiled eggs or a peanut butter sandwich.  
            - **Dinner:** Chicken soup or fish with a vegetable salad.  
            
            ✅ **Eat protein-rich food every 3 hours.**  
            ✅ **Strength train at least 4 times a week.**  
            """

    
    elif goal == "Maintain Weight":
        diet_message = """
        🍽 **Healthy Weight Maintenance Plan**  
        - ✅ **Balanced meals** with good portions of carbs, protein, and fats.  
        - ✅ **Eat more whole grains, vegetables, and lean proteins.**  
        - ✅ **Exercise** regularly to maintain metabolism.  
        - ✅ **Drink at least 8 glasses of water daily.**  
        - ✅ **Follow mindful eating habits** (avoid overeating).  
        """

    elif goal == "Improve Nutrition":
        diet_message = """
        🥕 **Nutrition Boosting Diet Plan**  
        - ✅ **Eat more fresh vegetables and fruits daily.**  
        - ✅ **Consume healthy fats** like olive oil, nuts, and seeds.  
        - ✅ **Drink fresh juices** instead of packaged drinks.  
        - ✅ **Limit processed foods, excessive sugar, and salt.**  
        - ✅ **Get enough fiber** from whole grains and legumes.  
        """

    
    st.markdown(f'<div class="diet-box">{diet_message}</div>', unsafe_allow_html=True)
