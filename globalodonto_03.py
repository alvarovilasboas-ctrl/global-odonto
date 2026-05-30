# -----------------------------------Importar libray - Biblioteca
# import numpy as np                  # Numeric Python - USADA PARA GERAR DADOS , TRANSFORMAR UM DADO DE UM TIPO PARA OUTRO
# import pandas as pd                 # Pandas - TRABALHAR COM AS TABELAS =   GERAR UMA TABELA NOVA ATRAVÉS DA ANTIGA, SALVAR A TABELA
import streamlit as st
# import altair as alt                #  Bliblioteca de gráficos
# import plotly.express as px         #  criar gráficos interativos complexos com pouquíssimas linhas de código. 
# import matplotlib.pyplot   as  plt  #  criar, personalizar e visualizar gráficos e dados de forma simples e eficiente. 
import datetime
##############################################################################################################
#----------ATENÇÃO   ------------------ Colocar site = Faça no terminal >> pip freeze > requirements.txt  
#                               
################################################################################################################- 
st.title('Wingets Avançados de Entrada ')     
st.write('Seleção de Opções')


col1, col2, col3 = st.columns([1, 1, 2])   #  Tamanho do Botão 4,5 cm
with col1:
    opcoes= st.selectbox( 
#   label='Qual a sua fruta favorita?',    É OPCIONAL
    'Qual é sua fruta favorita ? ' ,
    ('Maçã','Laranja','Mamão','Goiaba'),
    index=None,
    placeholder='Selecione a Frutas',
    ) 


#------------------ Multi Seleções -------
col1, col2, col3 = st.columns([1, 1, 1])   #  Tamanho do Botão 6 cm
with col1:
    varias_opcoes= st.multiselect(
#    label='Qual a sua fruta favorita?',    É OPCIONAL    
    'Quais as Frutas Desejadas ? ',
    ['Maçã','Laranja','Mamão','Goiaba'],
    placeholder='Selecione as Frutas',
    )


#st.write(f'Você gosta de: {", ".join(varias_opcoes) if varias_opcoes else "Nenhuma"}')   É OPCIONAL

#  ----------------- Radio Button --------------------
st.write(" ")
genero = st.radio(
    "Qual é o tipo de Filme que Você Gosta ?",
    [":rainbow[Comédia]", "***Drama***", "Documentário :movie_camera:"],
    index=None,
    captions=[
        "Loucademia de Polícia",
        "E o Vento Levou",
        "A vida de Álvaro",
        
    ],
)
if genero == ":rainbow[Comédia]":
    st.write("Você Selecionou Comédia")
else:
    if genero == "***Drama***":
       st.write("Você Selecionou Drama") 
    else:
        if genero=='Documentário :movie_camera:':
           st.write("Você Selecionou Documentário :movie_camera:")

#---------------- Selecionar Data ------------------------------
col1, col2, col3 = st.columns([1, 1, 4])         #  Tamanho do Botão 3 cm
with col1:
    today = datetime.datetime.now()
    d = st.date_input("Escolha a Data :", value=None,
    format="MM.DD.YYYY",
)
st.write(f'Você escolheu essa data : ',d)

#---------------- Selecionar Hora ------------------------------
col1, col2, col3 = st.columns([1, 1, 4])         #  Tamanho do Botão 3 cm
with col1:
    t = st.time_input("Escolha a Hora :", value=None)
    st.write("Hora Escolhida", t)

#-----------------  ChackBox  e  Download -------------
col1, col2, col3 = st.columns([1, 1, 1])          #  Tamanho da Mensagem : "Por Favor, aceite os termos" de 6  cm
with col1:
    termo = st.checkbox("Condições Aceitas")

    if termo:
      st.success('Termos Aceitos')
      st.download_button(
      label="Download Relatório",
      data='Conteúdo do Relatório',
      file_name="C:\\Python\\Teste\\Lendo arquivo.txt",
      mime="Text/plain",
    )
    else:
         st.info("Por Favor, aceite os termos")

#--------------------------------- Usar o st.form - Formulário ------------------------
#        
with st.form('Meu Formulário Conteúdo'):
    st.write('Preencha os seus dados') 
    nome= st.text_input ('Nome :')
    email= st.text_input('E_mail :')
    mensagem= st.text_area('Mensagem :')
    submissao= st.form_submit_button('Enviar mensagem ')

    if submissao:
        if nome and email and mensagem:
            st.success(f'mensagem de {nome} enviada com sucesso')
            st.write(f'E_mail {email} ')
            st.write(f'Mensagem : {mensagem}')
        else:
            st.error('Por favor, preencha todos os campos do formulário')