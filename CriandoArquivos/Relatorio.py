def salvar_log(temp):

    with open("relatorio.txt", "a", encoding="utf-8") as arquivo:

        while True:
            Operador = input("Digite o operador: ")

            if Operador == "SAIR".lower() or Operador == "":
                break;
            else:
                temperatura = float(input("Digite a temperatura da caldeira: "));
