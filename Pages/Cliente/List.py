import streamlit as st
import controllers.ClienteController as ClienteController
import models.Cliente as cliente
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.Edit as PageEditCliente



def List():
    colms = st.columns((1, 2, 1, 2, 1, 1))
    campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for x, item in enumerate(ClienteController.selecionar()):
        col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 2, 1, 1))
        col1.write(item.id)
        col2.write(item.nome)
        col3.write(item.idade)
        col4.write(item.profissao)
        button_space_excluir = col5.empty()
        on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.id))
        button_space_alterar = col6.empty()
        on_click_alterar = button_space_alterar.button('Alterar', 'btnAlterar' + str(item.id))

        if on_click_excluir:
            ClienteController.Excluir(item.id)

        if on_click_alterar:
            # Set the query parameter using st.query_params
            st.query_params['id'] = item.id
            PageEditCliente.Editar()
            