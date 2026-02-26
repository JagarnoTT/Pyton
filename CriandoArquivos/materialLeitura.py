try:
    with open("estoque.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read());
    print("-" * 50);
    print("Arquivo lido com sucesso!");
    arquivo.close();

except:
    print("O arquivo estoque.txt não existe. Por favor, adicione materiais primeiro.");