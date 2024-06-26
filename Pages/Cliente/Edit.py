import streamlit as st
import controllers.ClienteController as ClienteController
import models.Cliente as cliente
import Pages.Cliente.Edit as tes

def Editar():
    idAlteracao = st.query_params['id']
    idAlteracao = int(idAlteracao)
    clienteRecuperado = ClienteController.selecionarById(idAlteracao)
 

    with st.form(key='alterar_cliente'):
        listOccupation = ['Desenvolvedor', 'Engenheiro', 'Design']
        input_name = st.text_input(label="Alterar seu nome*", value=clienteRecuperado.nome)
        input_age = st.number_input(label="Alterar sua idade*", format="%d", step=1, value=clienteRecuperado.idade)
        input_occupation = st.selectbox(label="Alterar sua profissão", options=listOccupation, index=listOccupation.index(clienteRecuperado.profissao))
        input_button_submit = st.form_submit_button("Enviar")

        if input_button_submit:
            # Atualiza os atributos do cliente diretamente
            clienteRecuperado.nome = input_name
            clienteRecuperado.idade = input_age
            clienteRecuperado.profissao = input_occupation

            
            # Chama o método de alteração no controller
            ClienteController.Alterar(clienteRecuperado)
            st.success('parabens')
