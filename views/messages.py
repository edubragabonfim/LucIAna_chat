import streamlit as st
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio
import os
from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(
    user=os.getenv('PG_USER'),
    password=os.getenv('PG_PWD'),
    host=os.getenv('PG_HOST'),
    port=os.getenv('PG_PORT'),
)

cur = conn.cursor()


# @st.cache_data
def load_data():
    query = '''
        select
            *
            , length(prompt) as prompt_length
            , length(response) as response_length
        from public.gpt_messages gm 
        order by gm."_id_message" desc
        '''
    df = sqlio.read_sql_query(query, conn)
    return df


if st.button('Query Messages'):
    df_messages = load_data()
    col1, col2 = st.columns(2)
    col1.metric("Messages", df_messages.shape[0])
    st.dataframe(df_messages, hide_index=True)
