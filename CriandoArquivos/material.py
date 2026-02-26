try:
    material = input("Digite o nome do material:");

    with open("estoque.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(material + "\n");

    print("Material adicionado ao estoque com sucesso!");
#----------------------------------------------------------------------------------------
    print("ESTOQUE ATUALIZADO!!")

    with open("estoque.txt", "r", encoding="utf-8")as arquivoLer:
        conteudo = arquivoLer.read();

    print(conteudo + "\n");

    print("ESTOQUE ATUALIZADO!!")

except:
    print("Ocorreu um erro ao tentar adicionar o material. Por favor, tente novamente.");