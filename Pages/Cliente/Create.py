import streamlit as st
import streamlit as st
import controllers.ClienteController as ClienteController
import models.Cliente as cliente

def Create():
    
    st.title('Incluir cliente')

    with st.form(key='incluir_cliente'):

        input_name = st.text_input(label="Insira seu nome*")
        input_age = st.number_input(label="Insira sua idade*", format="%d", step=1)
        input_occupation = st.selectbox(label="Selecione sua profissão", options=['Desenvolvedor', 'Engenheiro', 'Design'])
        input_button_submit = st.form_submit_button("Enviar")
      

    if input_button_submit:
            
        novo_cliente = cliente.Cliente(0, input_name, input_age, input_occupation)
        ClienteController.incluir(novo_cliente)
        st.success('Cliente incluído com sucesso!')

