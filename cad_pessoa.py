import streamlit as st

pessoas = []

def cadastro(nome,fone):
    pessoa = {'nome': nome, 'Telefone': fone}
    pessoas.append(pessoa)

st.image("senai.png",width=100)
st.title("Cadastrar Pessoa e Telefone")

with st.form(key='login_form'):
    nome = st.text_input('Nome da pessoa: ')
    telefone = st.text_input('Informe o Telefone')
    botao = st.form_submit_button(label='Cadastrar')

if botao:
    if nome and telefone:
        cadastro(nome,telefone)
        st.success(f"{nome} com telefone {telefone} cadastrado com sucesso!")
    else:
        st.error("Preencha todos os campos")
    