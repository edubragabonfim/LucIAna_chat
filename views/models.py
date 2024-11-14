import streamlit as st
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio
import os
from dotenv import load_dotenv

def page_models():
    load_dotenv()

    conn = psycopg2.connect(
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PWD'),
        host=os.getenv('PG_HOST'),
        port=os.getenv('PG_PORT'),
    )

    cur = conn.cursor()

    if st.button('Query Models'):
        df_models_query = '''
            select * from public.llm_models
            order by "_id_model"
            '''
        df_models = sqlio.read_sql_query(df_models_query, conn)

        col1, col2 = st.columns(2)
        col1.metric("Models", df_models.shape[0])

        st.dataframe(df_models, hide_index=True)