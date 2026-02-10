print(f"carrinho de compras");
total = 0;

while True:
    valor = float(input(f"Qual o valor do produto? "));

    if valor == 0:
        break

    total = total + valor;
print(f"O valor da sua compra é: {total:.2f}");


print("-" * 30);
print(f"Sua compra foi finalizada o total a pagar é de: {total}");