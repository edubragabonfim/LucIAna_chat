from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth

def page_main():
    link = 'http://wa.me/5531973513292'

    st.sidebar.write(f"Chat with LucIAna in [WhatsApp]({link})")
    st.sidebar.json(st.session_state, expanded=False)
    st.header('LucIAna Portal 🧠', divider='blue')
    st.image('https://drive.google.com/file/d/1cXhnzARrCVFpsDjSp7-qWQ4odTPNalln/view')

