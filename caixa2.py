descricao = input("Qual o produto do cliente? ");
valor = float(input("Qual o valor do item? "));
quantidade = int(input("Quantos itens o cliente vai levar "));

valorTotal = valor * quantidade;

print(f"O Cliente pegou {quantidade} do produto {descricao} o mesmo tem o valor de {valor:.2f}");

print("-" * 30);
pagamento = input("Como gostaria de pagar? 1 - Debito, 2- Crédito, 3- Pix ");

if pagamento == "1":
    print(f" Certo, o seu pagamento é no Débito,a sua compra é de {valorTotal:.2f}, muito obrigado pela compra!");


elif pagamento == "2":
    print(f"Entendido seu pagamento vai ser no crédito");
    parcelamento= input(f"Digite a quantidade de vezes que vai parcelar(Parcelamento em até 3x) 1 - Uma vez, 2 - Duas vezes, 3 = Três vezes ");

    if parcelamento == "1":
        print(f"Sua compra ficou no valor de {parcelamento} parcela de {valorTotal:.2f}");
    
    elif parcelamento == "2":
        
        parcelamento2 = valorTotal / 2;
        parcelamento2Juros = valorTotal + ((5 / 100) * valorTotal);
        parcelamento2Jurossimples = parcelamento2Juros / 2;
        print(f"Sua compra ficou no valor de {parcelamento2Juros} com parcelas de {parcelamento2Jurossimples:.2f}, devido ao parcelamento será cobrado um juros de 5%");
    else:
        parcelamento3 = valorTotal / 3;
        parcelamento3Juros = valorTotal + ((7 / 100) * valorTotal);
        parcelamento3Jurossimples = parcelamento3Juros / 3;
        print(f"Sua compra ficou no valor de {parcelamento3Juros} com parcelas de {parcelamento3Jurossimples:.2f}, devido ao parcelamento será cobrado um juros de 7%");

elif pagamento == "3":
    valorDescontopix = (15 / 100) * valorTotal
    valorTotalPix = valorTotal - valorDescontopix
    print(f"Perfeito, seu pagamento é no pix, pagamentos no pix tem 15% de desconto, o valor da sua compra é {valorTotalPix:.2f}, muito obrigado pela preferência");


