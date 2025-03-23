import streamlit_authenticator as stauth


passwords = ["your_password_here"]  


hasher = stauth.Hasher(passwords)  


hashed_passwords = hasher.generate()


print(hashed_passwords)
