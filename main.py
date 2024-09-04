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
st.image('https://dashbirds.s3.us-east-1.amazonaws.com/LucIAna%20photo.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCbv369uvkYwGtVgm1kiK6OUoVaLaBxly9osb7kNMZZlAIgNTmWmHAXXqt0YvjF%2FFrCrFJKDstKWQYCNffF6yQJfIYq8QII3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARACGgw4MjY0NzIzMDg4ODEiDF9LJw%2BYfH49fT3E6SrFAqPzf67oLXwdHXx0k34nVK0%2F0BXpzv7JlU9Vlr1KQixOR9EgSiW8GvfoF6ygD5TJC6vkKt4z0970PjnsuxANAkj9c6QU32i%2BkB1kGlNrScnJ93Ni%2FJ7d7QhuEvCl5Aemq0MLa%2FG%2Brbb4ZsARnriC8g0c1c9TrlJNH7p%2BuwPHochTRjhNDKGn%2FsmfzW8dz26B6lyNEcU9DupDWSmrvaA4TflbvjYkRtUDR5K%2F8GS%2BH99suZ5MtC%2BPuEc5TtyJmH0umDNm4N135Mbu4Snbphnylti4RVqegPijYDmxn5l7290jL6PdEXL0SZnMaqw3oI07j5wPynKvXSCTHnLs66cNUsZajFXkLSA0IxvOi1ZMgbYMHvkypgkVXT5Hl9CxVfBTijYOqYNUvGSMoQG0uxq%2BRQu89Di3gzD12aX4JKtADS5dDIPdEwMwgKrjtgY6swKUTQxqavaxN10tyYIYdAV8tQaNnuHY6%2BVDT5q%2FOkUnIlD1uCcgtrvZIxsHSeLvYuvYJrw3%2FTpnmn2b1yfSQJC4%2FVmBKinS5Uyrcr2Kigq%2BQKA9Pecyo7At1JLjw6EP5aUXARcvmqGV0e57hBwl4N88iAE3CYmAkxlmyEN7QuGJxvrM0%2FThHCgrljzWMwLOBDSqNaPsp%2F6ViVQLwujnkSnEGdo9Pnf21ytUIE8AoGFi2uSPkJxXaXD4U1UKnkhi%2Fc0hfK8BZWn8kwdVw5cYtdVOXLHxUf7eQs%2FvyL7r8PSiqVFYmg249upbvkq4OoXYo3aBkba2HPi9hhOitiK%2FqHGEFyB9yr1NPJPFGS73XXV7r18v7qk%2FS2w%2Fb1FR1Wwnq3%2F1gBa1irXDJkFf8zfOdFCLuQi8&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240904T214622Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA4A3MWUCITAWZIXSR%2F20240904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=522c9fd9dd0be49d65b60e20fe9f8b8090d8c00e1a9e02de802824b7a4ba3318')