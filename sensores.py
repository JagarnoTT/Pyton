try:

    with open('sensores.txt', 'r', encoding="utf-8") as arquivo:
        LerArquivo = arquivo.read();
        print(LerArquivo);

except FileNotFoundError:
    with open("sensores.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Iniciando leitura de automação!");
    
    print(f"Ocorreu um erro ao tentar acessar o arquivo");