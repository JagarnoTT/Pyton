print("Caixa 1.0");

nome = input(" Digite o nome do cliente");
produto = input(" Qual produto o cliente pegou? ");
preco = float(input(" Qual o valor do Kg produto"));
peso = float(input(" Qual a quantidade que o cliente pegou? "));

total = preco * peso


print("-" * 30);
print(f"O cliente ${nome} comprou ${peso}Kg de ${produto} que custa o valor por Kg de ${preco}");
print(f"O valor total do pedido é ${total:.2f}");

print("-" * 30);
print(" Como gostaria de fazer o pagamento?");

pagamento = input(" Credito, Débito, pix ou dinheiro?");

print(f" Pagamento no ${pagamento} aprovado!");
print("-" * 30);
print("Volte sempre!")