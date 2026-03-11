def adicionar_item(novoItem):

    try:
        with open(estoqueLivaria.txt, "w", encoding="utf-8") as estoque:
            estoque.write(novoItem + "\n");
    
    except FileNotFoundError:
        print("Ocorreu um erro ao acessar o arquivo estoque.txt. Tente novamente!");
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}"); 
    
def listar_estoque():
        
    try:
        with open(estoqueLivraria.txt, 'r', encoding="utf-8") as estoque:
            print(estoque.read());
        
        while True:
            print("Digite a função que deseja realizar: "+ "\n" + "1: Adicionar item" + "\n" + "2: Listar estoque de itens" + "\n" + "3: Sair");
            opcao = input("Digite a opção que deseja abaixo: " + "\n");
            if opcao == "1":
                novoItem = input("Digite o nome do item que deseja adicionar: ");
                adicionar_item(novoItem);
                print("Novo item adicionado ao estoque com sucesso!");
            elif opcao == "2":
                print("Listando o estoque atualizado...");
                listar_estoque();
            elif opcao == "3":
                print("Conforme solicitado o programa será finalizado, te aguardo para a próxima atualização!!");
                break;
            else:
                print("Opção solicitada é invalida, por favor tente novamente!!");
            break;
    except FileExistsError:
                print("Ocorreu um erro ao acessar o arquivo, por favor tente novamente!");
    except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}");