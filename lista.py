print(f"Sua lista de itens de compras ");

itens = [];

while True:
    produto = input("Digite o nome do produto (ou 'sair' para finalizar): ");

    if produto == 'sair':
        break;
    
    print(f"Sua lista de compra tem {len(itens) + 1} unidade do item {produto.upper()}");

    itens.append(produto);

print(f"Sua lista de compras final é: ");

for produto in itens:
    print(f"{produto.upper()} ");      