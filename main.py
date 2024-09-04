from auth0_component import login_button
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

st.set_page_config(
    'Admin LucIAna',
    '🦅',
    layout='centered',
    initial_sidebar_state='expanded'
)

# user_info = login_button(os.environ.get('CLIENT_ID'), os.environ.get('DOMAIN'))
# st.write(user_info)

# Here is the start of the site
# First, we create the sidebar
st.sidebar.write('This is a experiment')
st.header('LucIAna Portal 🧠', divider='blue')
st.image('LucIAnaChat\static\LucIAna photo.jpg')