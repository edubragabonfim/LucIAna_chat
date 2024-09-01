import streamlit as st
import streamlit_authenticator as stauth
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
        gu."_id_user" 
        , gu.date_created 
        , gu."name" 
        , gu.phone 
        , gu."type" 
        , gu.features_available 
        , concat(gu."_id_user", ' - ', initcap(gu."name")) as id_user_and_name
        , concat(gu.phone , ' - ', initcap(gu."name")) as phone_user_and_name  
        , max(gm.date_time) as last_interaction 
    from public.gpt_users gu
    left join public.gpt_messages gm on gm."_id_user"::int = gu."_id_user"::int
    group by 1,2,3,4,5,6,7,8
    order by gu."_id_user" desc
    '''
df_users = sqlio.read_sql_query(df_users_query, conn)


# Here is the start of the site
st.header('LucIAna Admin 🧠⚙', divider='blue')

col1, col2 = st.columns(2)
col1.metric("Users", df_users.shape[0])
col2.metric("Last User Created", df_users['name'].head(1).unique()[0])

st.header('Users', divider='blue')
if st.button('Render Users', key='render_users'):
    st.dataframe(df_users, hide_index=True)

st.divider()

st.header('Set Configs', divider='blue')

dropdown_userselected = st.selectbox('User Selected', df_users['_id_user'].unique())
dropdown_typeuser = st.selectbox('Type User', ['admin', 'user'])
dropdown_featuresavailable = st.selectbox('Features Available', ['all', 'few'])

if st.button('Submit', key='submit_changes'):
    st.write(f'dropdown_userselected: {dropdown_userselected}')
    st.write(f'dropdown_typeuser: {dropdown_typeuser}')
    st.write(f'dropdown_featuresavailable: {dropdown_featuresavailable}')

    # Update Features
    sql_update_featuresavailable_query = """UPDATE public.gpt_users
                        SET features_available = %s
                        WHERE _id_user = %s"""
    values_to_update = (dropdown_featuresavailable, int(dropdown_userselected))
    cur.execute(sql_update_featuresavailable_query, values_to_update)

    # Update Type User
    sql_update_typeuser_query = """UPDATE public.gpt_users
                        SET type = %s
                        WHERE _id_user = %s"""
    values_to_update = (dropdown_typeuser, int(dropdown_userselected))
    cur.execute(sql_update_typeuser_query, values_to_update)

    # Commit the changes to the database
    conn.commit()

    df_users = sqlio.read_sql_query(df_users_query, conn)

    st.dataframe(df_users.query(f'_id_user == {dropdown_userselected}'), hide_index=True)

st.info(st.session_state)

