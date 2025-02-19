import streamlit as st
from openai import OpenAI
import os


import streamlit as st
from langchain.llms import OpenAI


def page_chat():
    st.header('Chat', divider='blue')

    div = f"""
    <iframe
        src="https://udify.app/chatbot/IWo3aE937CTUuSp6"
        style="width: 100%; height: 100%; min-height: 700px"
        frameborder="0"
        allow="microphone">
    </iframe>
    """
    st.markdown(div, unsafe_allow_html=True)