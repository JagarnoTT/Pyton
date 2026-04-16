def registrar_divergência():
    id_produto = input("Digite o ID do produto: ")
    quantidade_sistema = int(input("Digite a quantidade registrada no sistema: "))
    quantidade_fisica = int(input("Digite a quantidade física encontrada: "))

    try:
        quantidade_sistema = int(input('Digite um numero: '))
        quantidade_fisica = int(input('Digite um numero: '))

    except ValueError as e:
        print(f"Ocorreu um erro ao registrar os valores, verifique os valores digitados: {e}")

refistrar_divergência()