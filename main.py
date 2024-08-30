import streamlit as st
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
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

df_users_query = '''
select
    *
    , concat("_id_user", ' - ', initcap("name")) as id_user_and_name
    , concat(phone , ' - ', initcap("name")) as phone_user_and_name  
from public.gpt_users gu 
order by "_id_user" 
'''
df_users = sqlio.read_sql_query(df_users_query, conn)


# Here is the start of the site
st.title('LucIAna Admin')

dropdown_userselected = st.selectbox('User Selected', df_users['_id_user'].unique())
# dropdown_typeuser = st.selectbox('Type User', ['admin', 'user'])
dropdown_featuresavailable = st.selectbox('Features Available', ['all', 'few'])

if st.button('Submit'):
    st.write(f'dropdown_userselected: {dropdown_userselected}')
    # st.write(f'dropdown_typeuser: {dropdown_typeuser}')
    st.write(f'dropdown_featuresavailable: {dropdown_featuresavailable}')

    # Write the update query
    sql_update_query = """UPDATE public.gpt_users
                        SET features_available = %s
                        WHERE _id_user = %s"""

    # Tuple of values to update (new salary, employee id)
    values_to_update = (dropdown_featuresavailable, int(dropdown_userselected))

    # Execute the query
    cur.execute(sql_update_query, values_to_update)

    # Commit the changes to the database
    conn.commit()

    df_users = sqlio.read_sql_query(df_users_query, conn)

    st.dataframe(df_users.query(f'_id_user == {dropdown_userselected}'), hide_index=True)