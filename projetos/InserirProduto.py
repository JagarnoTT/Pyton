import sqlite3

def cadastar_produto(nome, codigo_barras, validade, quantidade, valor_unitario, observacao):
    conexao = sqlite3.connect('banco.db')
    cursor = conexao.cursor()

    comando_sql = """INSERT INTO produtos (nome, codigo_barras, validade, quantidade, valor_unitario, obervacao)
    VALUES(?, ?, ?, ?, ?, ?)"""

    dados_do_produto = (nome, codigo_barras, validade, quantidade, valor_unitario, observacao)

    try:
        cursor.execute(comando_sql, dados)