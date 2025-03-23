import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

CONFIG_FILE = "config.yaml" 

def load_authenticator():
    """Loads authentication settings from config.yaml and initializes the authenticator."""
    try:
        with open(CONFIG_FILE) as file:
            config = yaml.load(file, Loader=SafeLoader)
    except FileNotFoundError:
        st.error("Configuration file not found!")
        return None, None
    except yaml.YAMLError:
        st.error("Error reading YAML configuration.")
        return None, None

   
    cookie_settings = config.get('cookie', {'expiry_days': 30})  

    authenticator = stauth.Authenticate(
        config['credentials'],
        "fitness_tracker_auth",
        "random_signature_key",
        cookie_settings.get('expiry_days', 30)
    )

    return authenticator, config

def save_authentication_config(config):
    """Saves updated authentication settings to config.yaml."""
    try:
        with open(CONFIG_FILE, 'w') as file:
            yaml.safe_dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(f"Error saving config: {e}")

def login():
    """Handles user authentication and login."""
    authenticator, config = load_authenticator()
    if not authenticator:
        return None, None, False 

    name, authentication_status, username = authenticator.login('Login', 'sidebar')

    if authentication_status:
        st.sidebar.success(f"Welcome, {name}! 🎉")
        return name, username, True
    elif authentication_status is False:
        st.sidebar.error("Invalid username or password!")
    else:
        st.sidebar.info("Please enter your credentials.")

    return None, None, False

def logout():
    """Handles user logout."""
    authenticator, _ = load_authenticator()
    if authenticator:
        authenticator.logout("Logout", "sidebar")

def register_user(username, name, email, password):
    """Registers a new user by adding credentials to config.yaml."""
    authenticator, config = load_authenticator()
    if not authenticator:
        return

    
    if 'credentials' not in config:
        config['credentials'] = {'usernames': {}}
    
    hashed_password = stauth.Hasher([password]).hash()[0]

    
    config['credentials']['usernames'][username] = {
        'name': name,
        'email': email,
        'password': hashed_password
    }

    save_authentication_config(config)

    st.success(f"User {name} registered successfully! 🎉")
