limited_temp = 90;

comando_sql= (f"SELECT * FROM Log_sensores WHERE temperatura > {limited_temp}");

print(f"Comando SQL: {comando_sql}");