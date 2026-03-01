try:
    material = input("Digite o nome do material:");

    with open("estoque.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(material + "\n");

    print("Material adicionado ao estoque com sucesso!");
#----------------------------------------------------------------------------------------
    print("ESTOQUE ATUALIZADO!!")

    with open("estoque1.txt", "r", encoding="utf-8")as arquivoLer:
        conteudo = arquivoLer.read();

    print(conteudo + "\n");

    print("ESTOQUE ATUALIZADO!!")

except FileNotFoundError:
    print ("Ocorreu um erro ao tentar acessar o arquivo estoque.txt. Por favor, tente novamente.");
except Exception as e:
    print (f"Ocorreu um erro inesperado: {e}");