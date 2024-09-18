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
        , gu.notifications
        , gu._id_current_model
        , lm.model_name 
        , concat(gu."_id_user", ' - ', initcap(gu."name")) as id_user_and_name
        , concat(gu.phone , ' - ', initcap(gu."name")) as phone_user_and_name  
        , max(gm.date_time) as last_interaction 
        , count(gm."_id_message") as n_interactions
    from public.gpt_users gu
    left join public.gpt_messages gm on gm."_id_user"::int = gu."_id_user"::int
    left join public.llm_models lm on lm."_id_model"::int = gu."_id_current_model"::int
    group by 1,2,3,4,5,6,7,8,9
    order by gu."_id_user"
    '''
df_users = sqlio.read_sql_query(df_users_query, conn)

df_models_query = '''
    select
        lm."_id_model" 
        , lm.model_name 
    from public.llm_models lm
    where able = 'Yes'
    '''
df_models = sqlio.read_sql_query(df_models_query, conn)


# Here is the start of the site
# First, we create the sidebar
st.sidebar.write('This is a experiment')
st.header('LucIAna Admin 🧠⚙', divider='blue')

# Indicadores
col1, col2 = st.columns(2)
col1.metric("Users", df_users.shape[0])
col2.metric("Last User Created", (df_users.sort_values('_id_user', ascending=False)).name.head(1).unique()[0])
st.dataframe((df_users.sort_values('_id_user', ascending=False)).head(3), hide_index=True)  # Exibe os últimos 3 usuários que entraram

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
toggle_model_option = col1.toggle("Model Name")
toggle_notifications_option = col1.toggle('Notifications')

# DropDowns
if toggle_typeuser_option:
    dropdown_typeuser = col2.selectbox('Type User', ['admin', 'user'])
    st.session_state.typeuser = dropdown_typeuser
if toggle_featuresavailable_option:
    dropdown_featuresavailable = col2.selectbox('Features Available', ['all', 'few'])
    st.session_state.featuresavailable = dropdown_featuresavailable
if toggle_model_option:
    dropdown_model = col2.selectbox('Model Name', df_models['model_name'].unique())
    st.session_state.model = dropdown_model
    st.session_state._id_model = df_models.query(f"model_name == '{dropdown_model}'")._id_model.values[0]
if toggle_notifications_option:
    dropdown_notifications = col2.selectbox('Notifications', ['0', '1'])
    st.session_state.notifications = dropdown_notifications

# Se o botão for pressionado, faça...
if st.button('Submit', key='submit_changes'):
    toggle_list = [
        toggle_typeuser_option,
        toggle_featuresavailable_option,
        toggle_model_option,
        toggle_notifications_option
    ]

    if toggle_list[0]: # Type User
        sql_update_typeuser_query = """UPDATE public.gpt_users
                            SET type = %s
                            WHERE _id_user = %s"""
        values_to_update = (st.session_state.typeuser, int(dropdown_userselected))
        cur.execute(sql_update_typeuser_query, values_to_update)

    if toggle_list[1]: # Features Available
        sql_update_typeuser_query = """UPDATE public.gpt_users
                            SET features_available = %s
                            WHERE _id_user = %s"""
        values_to_update = (st.session_state.featuresavailable, int(dropdown_userselected))
        cur.execute(sql_update_typeuser_query, values_to_update)

    if toggle_list[2]: # Current Model
        sql_update_typeuser_query = """UPDATE public.gpt_users 
                            SET _id_current_model = %s 
                            WHERE _id_user = %s"""
        values_to_update = (str(st.session_state._id_model), int(dropdown_userselected))
        cur.execute(sql_update_typeuser_query, values_to_update)

    if toggle_list[3]: # Notifications
        sql_update_notifications_query = """UPDATE public.gpt_users 
                            SET notifications = %s 
                            WHERE _id_user = %s"""
        values_to_update = (str(st.session_state.notifications), int(dropdown_userselected))
        cur.execute(sql_update_notifications_query, values_to_update)
    
    df_users = sqlio.read_sql_query(df_users_query, conn)
    st.dataframe(df_users.query(f'_id_user == {dropdown_userselected}'), hide_index=True)

    # Commit the changes to the database
    conn.commit()

st.sidebar.json(st.session_state, expanded=True)
