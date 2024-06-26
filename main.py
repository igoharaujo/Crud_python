from numpy.core.fromnumeric import size
from os import write
import streamlit as st;
import controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd
import Pages.Cliente.Create as PageIncluirCliente
import Pages.Cliente.List as PageListCliente

st.sidebar.title('Menu')
page_cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])


if page_cliente == 'Consultar':
    PageListCliente.List()

if page_cliente == 'Incluir':
    PageIncluirCliente.IncluirClientePage()

    

