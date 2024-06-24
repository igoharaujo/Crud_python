from numpy.core.fromnumeric import size
from os import write
import streamlit as st;
import controllers.ClienteController as ClienteController
import models.Cliente as cliente

st.title('Incluir Cliente')

with st.form(key='include_cliente'):
    input_name = st.text_input(label="Insira seu nome*")
    input_age = st.number_input(label="Insira sua idade*", format="%d", step=1)
    input_occupation = st.selectbox(label="Selecione sua profissão", options=['Desenvolvedor', 'Engenheiro', 'Desing'])
    input_button_submit = st.form_submit_button("Enviar")


if input_button_submit:
    cliente.nome = input_name
    cliente.idade = input_age
    cliente.profissao = input_occupation

    ClienteController.incluir(cliente)
    st.success('Operação bem sucedida')

    
