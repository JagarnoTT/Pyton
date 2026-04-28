def calcular_risco():

    try:
        dias_restantes = input("Digite a quantidade de dias restantes para o vencimento do produto: ")
        dias_restantes = int(dias_restantes)

        if dias_restantes <= 14:
            return "Alto risco de perder o produto"
        elif dias_restantes <= 30:
            return "Médio risco de perder o produto"
        else:
            return "Baixo risco de perder o produto"
    except ValueError as e:
        print("Ocorreu um erro ao calcular o risco, verifique os valores digitados.")
        return calcular_risco()
resultado = calcular_risco()
print(f"O risco do produto é: {resultado}")
