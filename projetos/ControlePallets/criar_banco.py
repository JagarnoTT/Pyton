from banco import conectar
from werkzeug.security import generate_password_hash

conexao = conectar()
cursor = conexao.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
            usuario TEXT NOT NULL UNIQUE,
            senha_hash TEXT NOT NULL)''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS pallets(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT NOT NULL UNIQUE,
            observacao TEXT)''')

cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pallet_id INTEGER NOT NULL,
            descricao TEXT NOT NULL,
            codigo_barras TEXT,
            valor_unitario REAL NOT NULL,
            data_vencimento TEXT NOT NULL,
            risco TEXT NOT NULL,
            FOREIGN KEY(pallet_id) REFERENCES pallets(id)) ''')
senha_admin = generate_password_hash('admin123')

cursor.execute('''INSERT OR IGNORE INTO usuarios (nome, usuario, senha_hash)
            VALUES(?,?,?)''', ('Administrador', 'admin', senha_admin))
conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso")
print("Usuario: admin")
print("admin123")