import streamlit as st

# Here is the start of the site
# First, we create the sidebar
st.sidebar.write('This is a experiment')
st.header('Dashboard', divider='blue')

div = f"""
<iframe title="Dashbirds - LucIAna" 
        width="100%" 
        height="100%" 
        style="min-width: 300px; min-height: 1000px; border: none;" 
        src="https://app.powerbi.com/view?r=eyJrIjoiMjQ0N2IwZGUtNTdhZC00MTg2LWI4NDItYmM0MDdmZGUzY2IzIiwidCI6ImUxNjhhZTdjLWY5ZmMtNDIwZi04ODM4LTUwNmQxY2NlNWMwMiJ9" 
        allowFullScreen="true">
</iframe>
"""
st.markdown(div, unsafe_allow_html=True)