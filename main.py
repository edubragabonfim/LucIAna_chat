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

st.set_page_config(
    'Admin LucIAna',
    '🦅',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# Here is the start of the site
# First, we create the sidebar
st.sidebar.write('This is a experiment')
st.header('LucIAna Admin 🧠⚙', divider='blue')

# Indicadores
col1, col2 = st.columns(2)
col1.metric("Users", df_users.shape[0])
col2.metric("Last User Created", df_users['name'].head(1).unique()[0])
st.dataframe(df_users.head(3), hide_index=True)  # Exibe os últimos 3 usuários que entraram

st.header('Users', divider='blue')
if st.button('Render Users', key='render_users'):
    st.dataframe(df_users.sort_values('_id_user', ascending=True), hide_index=True)

st.divider()


# Set configs container
st.header('Set Configs', divider='blue')
dropdown_userselected = st.selectbox('User Selected', df_users['_id_user'].unique(), index=0)
st.session_state.userselected = dropdown_userselected
    #Exibe  as configurações do usuário selecionado
st.write('User Selected:', st.session_state.userselected)
# st.write('Model:', st.session_state.userselected)


# Divide em colunas para poder dizer qual opção quer mudar ou não
col1, col2 = st.columns(2)
toggle_typeuser_option = col1.toggle("Type User")
toggle_featuresavailable_option = col1.toggle("Features Available")

# DropDowns
if toggle_typeuser_option:
    dropdown_typeuser = col2.selectbox('Type User', ['admin', 'user'])
    st.session_state.typeuser = dropdown_typeuser
if toggle_featuresavailable_option:
    dropdown_featuresavailable = col2.selectbox('Features Available', ['all', 'few'])
    st.session_state.featuresavailable = dropdown_featuresavailable

# Se o botão for pressionado, faça...
if st.button('Submit', key='submit_changes'):
    toggle_list = [
        toggle_typeuser_option,
        toggle_featuresavailable_option
    ]
    if toggle_list[0] == True and  toggle_list[1] == True:
        # Update Type User
        sql_update_typeuser_query = """UPDATE public.gpt_users
                            SET type = %s
                            WHERE _id_user = %s"""
        values_to_update = (st.session_state.typeuser, int(dropdown_userselected))
        cur.execute(sql_update_typeuser_query, values_to_update)

        # Update Features
        sql_update_featuresavailable_query ="""UPDATE public.gpt_users
                        SET features_available = %s
                        WHERE _id_user = %s"""
        values_to_update = (st.session_state.featuresavailable, int(dropdown_userselected))
        cur.execute(sql_update_featuresavailable_query, values_to_update)
    elif toggle_list[0] == True and toggle_list[1] == False:
        sql_update_typeuser_query = """UPDATE public.gpt_users
                            SET type = %s
                            WHERE _id_user = %s"""
        values_to_update = (st.session_state.typeuser, int(dropdown_userselected))
        cur.execute(sql_update_typeuser_query, values_to_update)
    elif toggle_list[0] == False and toggle_list[1] == True:
        # Update Features
        sql_update_featuresavailable_query ="""UPDATE public.gpt_users
                        SET features_available = %s
                        WHERE _id_user = %s"""
        values_to_update = (st.session_state.featuresavailable, int(dropdown_userselected))
        cur.execute(sql_update_featuresavailable_query, values_to_update)
    else:
        pass
    
    df_users = sqlio.read_sql_query(df_users_query, conn)
    st.dataframe(df_users.query(f'_id_user == {dropdown_userselected}'), hide_index=True)

    # Commit the changes to the database
    conn.commit()

st.sidebar.json(st.session_state, expanded=True)
