import time;
def adicionar_item(novoItem):

    try:
        with open("estoqueLivraria.txt", "a", encoding="utf-8") as estoque:
            estoque.write(novoItem + "\n");
    
    except FileNotFoundError:
        print("Ocorreu um erro ao acessar o arquivo estoque.txt. Tente novamente!");
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}"); 
    
def listar_estoque():
        
    try:
        with open("estoqueLivraria.txt", 'r', encoding="utf-8") as estoque:
            print(estoque.read());
    except FileNotFoundError:
                print("Ocorreu um erro ao acessar o arquivo, por favor tente novamente!");
    except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}");
        
while True:
        time.sleep(2);
        print("Digite a oção que deseja utilizar: ");
        print("-" * 50);
        print("1 - Adicionar item!");
        print("2 - Listar estoque atualizado!");
        print("3 - Sair do programa!");
        print("-" * 50);
        opcao = input("Digite a opção que deseja abaixo: " + "\n");
        if opcao == "1":
            print("Opção de adicionar item selecionada...");
            print("-" * 50);
            novoItem = input("Digite o nome do item que deseja adicionar: ");
            adicionar_item(novoItem);
            print("-" * 50);
            print("Novo item adicionado ao estoque com sucesso!");
            print("-" * 50);
        elif opcao == "2":
            print("Listando o estoque atualizado...");
            time.sleep(2);
            listar_estoque();
        elif opcao == "3" or opcao == "sair".lower():
            print("Conforme solicitado o programa será finalizado, te aguardo para a próxima atualização!!");
            break;
            
        else:
            print("Opção solicitada é invalida, por favor tente novamente!!");