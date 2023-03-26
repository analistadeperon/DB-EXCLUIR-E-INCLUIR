# importando o SQL
import sql as lite
con = lite.connect('dados.db') # conexão da tabela 

#Criando Tabela:
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Inventario(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, local TEXT, descricao TEXT,marca TEXT,  data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
    
    import sql as lite
from datetime import datetime

# Criando conexão
con = lite.connect('dados.db')

# Inserir Nomes e Dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Inventario (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Deletar Nomes e Dados
def deletar_form(i):

    with con:
        cur = con.cursor()
        query = "DELETE FROM Inventario WHERE id=?"
        cur.execute(query, i)


# Atualizar Nomes e Dados
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# Ver Nomes e Dados
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Iten no Nomes e Dados
def ver_iten(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario WHERE id=?",(id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens
