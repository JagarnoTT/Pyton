import sqlite3

def conectar():
    conexao = sqlite3.connect('controle_pallets.db')
    conexao.row_factory = sqlite3.Row
    return conexao