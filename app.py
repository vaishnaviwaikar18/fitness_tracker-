import streamlit as st

def set_background():
    image_url = "https://images.pexels.com/photos/1552249/pexels-photo-1552249.jpeg"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
        }}

        /* 🔥 Increase Font Size and Color */
        h1 {{
            font-size: 50px !important;
            text-align: center;
            color: #ffffff !important;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.7);
            font-weight: bold;
        }}
        
        h3 {{
            font-size: 30px !important;
            text-align: center;
            color: #ffffff !important;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.7);
        }}

        /* 🔥 Dashboard Text Color */
        .stMarkdown {{
            color: #ffffff !important;
        }}

        /* 🔥 Input Box */
        .stTextInput>div>div>input {{
            font-size: 20px !important;
            padding: 10px;
        }}

        /* 🔥 Button Styling */
        .stButton>button {{
            background: linear-gradient(to right, #ff416c, #ff4b2b);
            color: white;
            font-size: 22px !important;
            padding: 12px 25px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
            cursor: pointer;
        }}
        .stButton>button:hover {{
            background: linear-gradient(to right, #ff4b2b, #ff416c);
            transform: scale(1.1);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



if "page" not in st.session_state:
    st.session_state["page"] = "landing"


set_background()


if st.session_state["page"] == "landing":
    st.markdown("<h1 style='text-align: center;'>🏋️‍♂️ Personal Fitness Tracker</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Start your journey with us</h3>", unsafe_allow_html=True)

 
    user_name = st.text_input("Enter your name", key="name")

    if st.button("Get Started"):
        st.session_state["page"] = "dashboard"
        st.rerun() 

if st.session_state["page"] == "dashboard":
    st.markdown("<h1>Welcome to Your Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3>Hello, {st.session_state.get('name', 'User')}! Let's track your fitness journey. 💪</h3>", unsafe_allow_html=True)