import streamlit as st
from streamlit import runtime
 
import pandas as pd
import hashlib
import psycopg2
import time
from db_pas import db_host, db_dbname, db_user, db_password, db_port
from st_pages import Page, show_pages
from streamlit_extras.switch_page_button import switch_page
from streamlit_javascript import st_javascript
from rodape import rodape, rodape_links

# URL do logo
logo = 'https://drive.google.com/uc?export=view&id=1-I7moLDQoxG5jk-d2YMatu-Ola03qEFw'

st.set_page_config(
    initial_sidebar_state="expanded",
    page_title="Dashbirds Hub",
    page_icon="🦉",
)

h = hashlib.new("SHA256")

id_user = 0
name_user = 'indefinido'
email_user = 'indefinido'
type_user = 'indefinido'


# CSS personalizado
custom_css = """

<style>   

    .st-emotion-cache-6qob1r{
        display: none;
    }  
    .st-emotion-cache-1vglrfb{
       display: none; 
    }
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }    
    .stChatMessage svg {
        display: none;
    }
    .st-emotion-cache-xabiqo:disabled{
        color: #1e7a75; 
    }
    .st-emotion-cache-62i85d{
        background-color: #fbd700 !important; 
        width: 25px !important;
        height: 25px !important;
        border-radius: 20px !important;
    }
    .st-emotion-cache-1lr5yb2{
        background-color: #1e7a75 !important;
        width: 25px !important;
        height: 25px !important;
        border-radius: 20px !important;
    }
    .img-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .title {
        color: #6495ed;  
    }

    .subtitle {
        font-size: 16px; 
        color: #777777;
    }   
    .rodape-suporte {
        font-size: 16px; 
        color: #777777;
    }   
      [data-testid="stSidebarNav"] {
        display: none;
    } 
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi5 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div > div > div:nth-child(4) > div > button > div > p{
    text-decoration: underline;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi5 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div > div > div:nth-child(4) > div{
        text-align: center;
    }
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi5 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div > div > div:nth-child(4) > div > button{
        color: #999 !important;  
        border: 0px solid #fff !important;  
        text-align: center;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi5 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div > div > div.st-emotion-cache-ixecyn.e10yg2by1{
       border: 2px solid #f4f4f4 !important;   
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi5 > div.block-container.st-emotion-cache-1y4p8pa.ea3mdgi4 > div > div > div.st-emotion-cache-ixecyn.e10yg2by1 > div > div > div:nth-child(3) > div > div > button{
        background-color: #1e7a75 !important;  
        color: #fff !important;  
        border: 2px solid #1e7a75 !important;  
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > div{
        display:none;
    }
    
    @media only screen and (max-width: 600px) {
    .title {
        font-size: 26px;  
    }
    .st-emotion-cache-1sls4c0 {
        margin-top: -30px;
    }
    }
    
    )

</style>
"""
# Adicionando o CSS personalizado ao aplicativo Streamlit
st.markdown(custom_css, unsafe_allow_html=True)

# Optional -- adds the title and icon to the current page
# add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be

show_pages(
    [
        Page("index.py", "index", ""),
        Page("cadastro.py", "cadastro", ""),
        Page("chat.py", "alphai_chat", ""),
        Page("chat_especifico.py", "alphai_chat_specific", ""),
        Page("chat_pdf.py", "alphai_chat_pdf", ""),
        Page("admin_users.py", "admin_users", ""),
        Page("admin_messages.py", "admin_messages", ""),
        Page("admin_log.py", "admin_log", ""),
        Page('dashboards.py', 'dashboards', ''),
    ]
)

# Variável para conexão com banco de dados
db_connection = psycopg2.connect(
    host=db_host,
    dbname=db_dbname,
    user=db_user,
    password=db_password,
    port=db_port
)

# Função para conectar banco de dados
def run_query(query, is_select=True):
    with db_connection.cursor() as cur:
        cur.execute(query)
        if is_select:
            return cur.fetchall()
        db_connection.commit()  # Essencial para comandos que alteram o banco de dados

# Função para login, realizar busca no banco de dados gpt_users
def fetch_user_data(input_email, pass_hash):
    query = f"SELECT * FROM gpt_users WHERE email='{input_email}' AND pass='{pass_hash}'"
    rows = run_query(query)

    data = pd.DataFrame(
        rows, columns=['_id_user', 'date_created', 'name', 'email', 'pass', 'type'])
    return data


# Titulo e Subtitulo
st.markdown(f"""
    <div class="img-container">
    <img src="{logo}" alt="Logo" width="150"/>
    <h1 class="title">Boas vindas ao Dashbirds Hub 🦅</h1>
    <p class="subtitle">Faça login abaixo para acessar. </p>
    </div>
""", unsafe_allow_html=True)


# Forms can be declared using the 'with' syntax
with st.form(key='login'):
    input_email = str(st.text_input(
        label='Email', placeholder='Digite o seu email'))
    input_senha = str(st.text_input(
        label='Senha', type='password', placeholder='Digite a sua senha'))
    btn_entrar = st.form_submit_button(label='Entrar')


# Se clicar no botão de entrar
if btn_entrar:

    try:
        h.update(input_senha.encode())
        pass_hash = h.hexdigest()

        query = f"SELECT * FROM gpt_users WHERE email='{input_email.lower()}' AND pass='{pass_hash}'"
        rows = run_query(query)

        # Certifique-se de que os nomes das colunas correspondam à sua tabela de banco de dados
        data = pd.DataFrame(
            rows, columns=['_id_user', 'date_created', 'name', 'email', 'pass', 'type'])
        count = len(data)
    except:
        st.error(
            'Login ou Senha inválido. Tente novamente ou recupere a sua senha.')

    if count == 1:
        # Obter dados do usuário do DataFrame
        id_user = data.iloc[0]['_id_user']
        type_user = data.iloc[0]['type']
        name_user = data.iloc[0]['name']
        email_user = data.iloc[0]['email']

        # Salvar Variáveis no Armazenamento Local via JavaScript
        js_id_user = st_javascript(
            f"localStorage.setItem('userId', '{id_user}');")

        js_type_user = st_javascript(
            f"localStorage.setItem('userType', '{type_user}');")

        js_name_user = st_javascript(
            f"localStorage.setItem('userName', '{name_user}');")

        js_email_user = st_javascript(
            f"localStorage.setItem('userLogin', '{email_user}');")

        time.sleep(1)

        # Se der match de 1 item exatdo Email e Senha, continuar o código

        # Adicionar dado de login no Log
        update_acesso = run_query("""
        INSERT INTO gpt_log(date_log,_id_user, email,activity)
        VALUES (CURRENT_TIMESTAMP, '{}', '{}', 'LOGIN')
        """.format(id_user, input_email.lower()), is_select=False)

        if type_user == 'Admin':
            switch_page("admin_users")
        else:
            switch_page("alphai_chat")

    # Senão exibir erro
    else:
        st.error(
            'Login ou Senha inválido. Tente novamente ou recupere a sua senha.')


# Botão para página de cadastro
btn_cadastro = st.button(label='Ainda não possui cadastro? Cadastre-se')
if btn_cadastro:
    switch_page("cadastro")

# Rodapé com a versão
st.markdown(rodape, unsafe_allow_html=True)

# Links rodapé
# st.markdown(rodape_links, unsafe_allow_html=True)

