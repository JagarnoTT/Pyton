import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

comando_sql = '''CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    codigo_barras TEXT UNIQUE,
    validade TEXT,
    quantidade INTEGER NOT NULL,
    valor_unitario REAL NOT NULL,
    observacao TEXT
    )'''
cursor.execute(comando_sql)
conexao.commit()

print("Banco criado com sucesso e tabela 'produtos' criada com sucesso!")
conexao.close()