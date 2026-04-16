import sqlite3

def Sensor():
    conexao = sqlite3.connect('fabrica.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sensor
        ( id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_sensor Text,
                leitura REAL,
                    unidade TEXT) ''')
    cursor.execute(''' INSERT INTO sensor(nome_sensor, leitura, unidade) VALUES ('Temperatura',  25.5, 'Celsius')''')
    conexao.commit()
    conexao.close()

    print("Dados inseridos com sucesso!")

Sensor()
