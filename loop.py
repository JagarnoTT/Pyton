Salario = float(input("Digite o salário do funcionário: "))

while True:
    conta = float(input("Digite o valor da conta (ou 0 para sair): "))

    if conta == 0:
        print(f"Você terminou o mês positivo! Seu saldo é de {Salario:.2f}");
        break;

    Salario -= conta

    if Salario < 0:
        print(f"Você terminou o mês no vermelho {Salario:.2f}!")
        break;

    print(f"Seu saldo atual é de {Salario:.2f}");