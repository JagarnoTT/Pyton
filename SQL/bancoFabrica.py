import sqlite3;

conexao = sqlite3.connect("bancoFabrica.db");

cursor = conexao.cursor();

cursor.execute(""" CREATE TABLE IF NOT EXISTS Sensores(ID INTEGER PRIMARY KEY AUTOINCREMENT, Operador TEXT, Temperatura REAL)""");

conexao.commit();
conexao.close();

print("Tabela criada com sucesso!");