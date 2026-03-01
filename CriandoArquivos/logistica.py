def adicionar_item():
    try:
        with open("estoque.txt", 'w', encoding="utf-8") as estoque:
            while True:
                item = input("Digite o item a ser adicionado na lista(ou aperte sair para finalizar)" + "\n");
                print("-"* 50);
                if item.lower() == "sair":
                    print("Finalizando a adição de itens na lista do estoque... te aguardo para a próxima atualização!!");
                    break;
                else:
                    estoque.write(item + "\n");
    except FileNotFoundError:
        print("Ocorreu um erro ao acessar o arquivo estoque.txt. Tente novamente!");
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}");
#----------------------------------------------------------------------------------------
    print("Alteração no estoque identificada!!");
    try:
        with open("estoque.txt", "r", encoding="utf-8") as arquivo_atualizado:
            Dados = arquivo_atualizado.read();
            print("Abaixo segue os dados atualizado na lista do estoque:");
            print(Dados);
    except FileNotFoundError:
        print("Ocorreu um erro ao acessar o arquivo, por favor tente novamente!");
    except Exception as e:
        print("Ocorreu um erro inesperado: {e}");
adicionar_item();