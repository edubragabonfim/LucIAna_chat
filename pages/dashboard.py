import streamlit as st

st.set_page_config(
    'Admin LucIAna',
    '🦅',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# Here is the start of the site
# First, we create the sidebar
st.sidebar.write('This is a experiment')
st.header('Dashboard', divider='blue')

div = f"""
<iframe title="Dashbirds - LucIAna" width="2000" height="1100" src="https://app.powerbi.com/view?r=eyJrIjoiMjQ0N2IwZGUtNTdhZC00MTg2LWI4NDItYmM0MDdmZGUzY2IzIiwidCI6ImUxNjhhZTdjLWY5ZmMtNDIwZi04ODM4LTUwNmQxY2NlNWMwMiJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
st.markdown(div, unsafe_allow_html=True)