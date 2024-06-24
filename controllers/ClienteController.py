import services.database as db

def incluir(cliente):
    Icount = db.cursor.execute( """
    INSERT INTO Cliente 
    (cli_Nome, cli_Idade, cli_Profissao)
        VALUES
    (?,?,?)""",
    cliente.nome, cliente.idade, cliente.profissao).rowcount
    db.conn.commit()
