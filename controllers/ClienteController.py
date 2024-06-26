from typing import List
import services.database as db
import models.Cliente as cliente

def incluir(cliente):
    Icount = db.cursor.execute( """
    INSERT INTO Cliente 
    (cli_Nome, cli_Idade, cli_Profissao)
        VALUES
    (?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao).rowcount
    db.conn.commit()


def selecionar():
    select = db.cursor.execute('SELECT * FROM cliente')
    constumerList = []

    for row in select.fetchall():
        constumerList.append(cliente.Cliente(row[0], row[1],row[2],row[3]))
    return constumerList


def alterar(cliente):
    alter = db.cursor.execute(
    '''
    Update cliente
        SET ?, ?, ?
    where id = ?

    ''', cliente.nome, cliente.idade, cliente.profissao, cliente.nome ).rowcount
    db.conn.commit()

def Excluir(id):
    count = db.cursor.execute('''
    DELETE FROM cliente
        WHERE id = ?''', id).rowcount
    db.conn.commit()