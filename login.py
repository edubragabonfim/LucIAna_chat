import pickle
from pathlib import Path
import hashlib
import os
import time

import psycopg2
import pandas as pd
import streamlit as st
# from st_pages import add_page_title, get_nav_from_toml
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from streamlit_javascript import st_javascript
from dotenv import load_dotenv

from views.settings import page_settings
from views.models import page_models
from views.messages import page_messages
from views.main import page_main
from views.error import page_error
from views.dashboard import page_dashboard
from views.chat import page_chat

st.set_page_config(
    page_title='LucIAna',
    page_icon='static/LucIAna.jpg'
)

def main():
    load_dotenv() 
    
    _key = st.text_input('Enter your key...', type='password') 
    st.divider()

    if _key == os.getenv('KEY'):
        pg = st.navigation(
            [
                st.Page(page_main, title='Main', icon=':material/home:', url_path='home'),
                st.Page(page_settings, title='Settings', icon=':material/settings:', url_path='settings'),
                st.Page(page_messages, title='Messages', icon=':material/mail:', url_path='messages'),
                st.Page(page_models, title='Models', icon=':material/psychology:', url_path='models'),
                # st.Page(page_dashboard, title='Dashboard', icon=':material/monitoring:', url_path='dashboard'),
                st.Page(page_chat, title='Chat', icon=':material/chat:', url_path='chat')
            ]
        )
        pg.run()
    elif _key == '':
        st.warning('The key is empty')

        pg = st.navigation([
            st.Page(page_error, title='🏠 Main')
        ])
        pg.run()
    else:
        st.error('Invalid key')

        pg = st.navigation([
            st.Page(page_error, title='🏠 Main')
        ])
        pg.run()

        

# Just a comment
# Right Here
if __name__ == '__main__':
    main()