import streamlit as st
from openai import OpenAI
import os


import streamlit as st
from langchain.llms import OpenAI


def page_chat():
    openai_api_key = os.getenv('OPENAI_API_kEY')
    st.title("💬 LucIAna Chat")

    '''
    # if "messages" not in st.session_state:
    #     st.session_state["messages"] = [{"role": "assistant", "content": "Hi Braga. LucIAna here. How can i help you today?"}]

    # for msg in st.session_state.messages:
    #     st.chat_message(msg["role"]).write(msg["content"])

    # if prompt := st.chat_input():
    #     if not openai_api_key:
    #         st.info("Please add your OpenAI API key to continue.")
    #         st.stop()

    #     client = OpenAI(api_key=openai_api_key)
    #     st.session_state.messages.append({"role": "user", "content": prompt})
    #     st.chat_message("user").write(prompt)
    #     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    #     msg = response.choices[0].message.content
    #     st.session_state.messages.append({"role": "assistant", "content": msg})
    #     st.chat_message("assistant").write(msg)
    # st.title("🦜🔗 Langchain Quickstart App")
    '''

    def generate_response(input_text):
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info(llm(input_text))


    with st.form("my_form"):
        text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
        submitted = st.form_submit_button("Submit")
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
        elif submitted:
            generate_response(text)