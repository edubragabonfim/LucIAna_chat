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

load_dotenv()

# nav = get_nav_from_toml(".streamlit/pages.toml")

_key = st.text_input('Enter your key...')

if _key == os.getenv('KEY'):
    pg = st.navigation(
        [
            # st.Page("views/main.py"),
            st.Page(page_main, title='🏠 Main'),
            # st.Page("views/settings.py"),
            st.Page(page_settings, title='⚙️ Settings'),
            # st.Page("views/messages.py"),
            st.Page(page_messages, title='💬 Messages'),
            # st.Page("views/models.py"),
            st.Page(page_models, title='🤖 Models')
        ]
    )
    pg.run()
else:
    st.error('Invalid key')
