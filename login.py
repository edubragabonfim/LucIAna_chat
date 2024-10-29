import pickle
from pathlib import Path
import hashlib
import os
import time

import psycopg2
import pandas as pd
import streamlit as st
# from st_pages import add_page_title, get_nav_from_toml
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from streamlit_javascript import st_javascript
from dotenv import load_dotenv

load_dotenv()

# nav = get_nav_from_toml(".streamlit/pages.toml")

pg = st.navigation(
    [
        st.Page("views/main.py"),
        st.Page("views/settings.py"),
        st.Page("views/messages.py"),
        st.Page("views/models.py"),
    ]
)

pg.run()

# ## ---- USER  AUTHENTICATION ----
# h = hashlib.new("SHA256")

# conn = psycopg2.connect(
#     user=os.getenv('PG_USER'),
#     password=os.getenv('PG_PWD'),
#     host=os.getenv('PG_HOST'),
#     port=os.getenv('PG_PORT'),
# )

# # Função para conectar banco de dados
# def run_query(query, is_select=True):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         if is_select:
#             return cur.fetchall()
#         conn.commit()  # Essencial para comandos que alteram o banco de dados

# # Função para login, realizar busca no banco de dados gpt_users
# def fetch_user_data(input_username, password):
#     query = f"SELECT * FROM gpt_users WHERE username='{input_username}' AND password='{password}'"
#     rows = run_query(query)

#     data = pd.DataFrame(
#         rows, columns=['_id_user', 'date_created', 'name', 'username', 'password', 'type'])
#     return data

# # Titulo e Subtitulo
# st.markdown(f"""
#     <div class="img-container">
#     <h1 class="title">Boas vindas ao Dashbirds Hub 🦅</h1>
#     <p class="subtitle">Faça login abaixo para acessar. </p>
#     </div>
# """, unsafe_allow_html=True)

# with st.form(key='login'):
#     input_username = str(st.text_input(
#         label='Usuário', placeholder='Digite o seu usuário'))
#     input_senha = str(st.text_input(
#         label='Senha', type='password', placeholder='Digite a sua senha'))
#     btn_entrar = st.form_submit_button(label='Entrar')

# # Se clicar no botão de entrar
# if btn_entrar:

#     try:
#         # h.update(input_senha.encode())
#         # pass_hash = h.hexdigest()
#         pass_hash = input_senha

#         query = f"SELECT * FROM gpt_users WHERE email='{input_username.lower()}' AND pass='{pass_hash}'"
#         rows = run_query(query)

#         # Certifique-se de que os nomes das colunas correspondam à sua tabela de banco de dados
#         data = pd.DataFrame(
#             rows, columns=['_id_user', 'date_created', 'name', 'email', 'pass', 'type'])
#         count = len(data)
#     except:
#         st.error('Login ou Senha inválido. Tente novamente ou recupere a sua senha.')

#     if count == 1:
#         # Obter dados do usuário do DataFrame
#         id_user = data.iloc[0]['_id_user']
#         type_user = data.iloc[0]['type']
#         name_user = data.iloc[0]['name']
#         email_user = data.iloc[0]['email']

#         # Salvar Variáveis no Armazenamento Local via JavaScript
#         js_id_user = st_javascript(
#             f"localStorage.setItem('userId', '{id_user}');")

#         js_type_user = st_javascript(
#             f"localStorage.setItem('userType', '{type_user}');")

#         js_name_user = st_javascript(
#             f"localStorage.setItem('userName', '{name_user}');")

#         js_email_user = st_javascript(
#             f"localStorage.setItem('userLogin', '{email_user}');")

#         time.sleep(1)

#         if type_user == 'Admin':
#             switch_page("admin_users")
#         else:
#             switch_page("alphai_chat")

#     # Senão exibir erro
#     else:
#         st.error(
#             'Login ou Senha inválido. Tente novamente ou recupere a sua senha.')


# # Botão para página de cadastro
# btn_cadastro = st.button(label='Ainda não possui cadastro? Cadastre-se')
# if btn_cadastro:
#     switch_page("cadastro")

# names = ['Eduardo Bonfim', 'Administrator']
# usernames = ['ebbonfim', 'adminluciana']
# file_path = Path(__file__).parent / "hashed_pw.pkl"

# with file_path.open('rb') as file:
#     hashed_passwords = pickle.load(file)

# credentials = {
# "usernames":{
#     usernames[0]:{
#         "name": names[0],
#         "password": hashed_passwords[0]
#         },
#     usernames[1]:{
#         "name": names[1],
#         "password": hashed_passwords[1]
#         }            
#     }
# }

# authenticator = stauth.Authenticate(credentials, "some_cookie_name", 'some_signature_key', cookie_expiry_days=30)
# name, authentication_status, username = authenticator.login(location='main')

## ---- USER  AUTHENTICATION ----

# if authentication_status == False:
#     st.error('Username/Password is incorrect')
#     st.runtime.legacy_caching.clear_cache()

# if authentication_status == None:
#     st.warning('Please enter your username and password')
#     st.runtime.legacy_caching.clear_cache()

# if authentication_status:
#     st.runtime.legacy_caching.clear_cache()