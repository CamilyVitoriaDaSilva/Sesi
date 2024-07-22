import streamlit as st

st.title('Titulo da página')
st.header('Cabeçalho')
st.subheader('sub cabeçalho')
st.text('texto simples')

st.markdown('Titulo Markdown')

valor = st.slider('Selecione um valor',0,100,50)
st.write('Valor selecionado:',valor )

if st.button('Clique aqui'):
    st.write('Botão clicado!')

nome = st.text_input('Digite seu nome: ')
st.write('Nome:', nome)

opcao = st.selectbox('Escolha uma opção: ',['op 1','op 2','op 3'])
st.write('Opção escolhida: ',opcao)

opcoes = st.multiselect('Escolha multiplas opções: ',['op 1','op 2','op 3'])
st.write('Opções escolhidas: ',opcoes)

arquivo = st.file_uploader('Escolha um arquivo')
if arquivo is not None:
    st.write('Arquivo carregado:',arquivo.name)

if st.checkbox('Mostrar texto'):
    st.write('Texto mostrado!')

genero = st.radio('Escolha seu gênero: ',['Masculino','Feminino','Outro'])
st.write('Gênero: ',genero)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1,2,3,4],[10,20,30,40])
st.pyplot(fig)
#dividindo em 2 colunas
col1 , col2 = st.columns(2)
col1.write('Coluna 01')
col2.write('Coluna 02')
#Barras laterais
st.sidebar.title('Barra Lateral')
st.sidebar.slider('Slide na barra lateral',0,100,50)
#Expansor
with st.expander('Clique para expandir'):
    st.write('Texto dentro do expansor.')

tab1, tab2 = st.tabs(['Tab1','Tab2'])
with tab1:
    st
st.image("senai.png",width=100)