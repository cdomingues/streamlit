import streamlit as st
import pandas as pd

st.header('Home Page')
st.success(' # Titulo *Secundário*')

dados = pd.read_csv('prof-dados-resumido.csv')
st.write(dados)

var = st.sidebar.selectbox('Selecione uma variável',['Idade','Profissão'])

ms = dados['Salário'].groupby(dados[var]).mean().apply(lambda x: "{:_.2f}".format(x).replace('.', ',').replace('_', '.'))
st.write    (ms) 
st.table(dados.describe())

plot = dados[var].value_counts().plot(kind='barh')
st.pyplot(plot.figure)

