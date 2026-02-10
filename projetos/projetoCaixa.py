print("--- MERCADÃO DO DEV ---")

carrinho_produtos = []
carrinho_precos = []
total_geral = 0.0

while True:
    print("\n--- NOVO ITEM ---")
    produto = input("Nome do produto (ou FIM): ")
    
    # 1. CONDIÇÃO DE SAÍDA (O Break)
    if produto.upper() == "FIM":
        break

    # 2. PEGAR O PREÇO
    preco = float(input("Preço: R$ "))


    # 3. GUARDAR NAS LISTAS (O Segredo)
    # Adicione o produto na lista de produtos
    # Adicione o preço na lista de preços
    carrinho_produtos.append(produto) # Guardar o produto na lista de produtos
    carrinho_precos.append(preco) # Guardar o preço na lista de preços

    # 4. ATUALIZAR O TOTAL GERAL
    total_geral += preco;

    print(f"Adicionado: {produto} custando R$ {preco:.2f}")

# --- HORA DA NOTA FISCAL ---
print("\n" + "="*30)
print("       CUPOM FISCAL")
print("="*30)

# AQUI VEM A MÁGICA DO ÍNDICE
# Vamos repetir de 0 até o tamanho da lista
quantidade_itens = len(carrinho_produtos) # Se tem 3 itens, conta até 3

for i in range(quantidade_itens):
    # 'i' vai valer 0, depois 1, depois 2...
    # Assim pegamos o produto[0] e o preco[0] juntos
    
    nome_da_vez = carrinho_produtos[i]
    preco_da_vez = carrinho_precos[i]

    print(f"Item {i+1}: {nome_da_vez} .......... R$ {preco_da_vez:.2f}")

print("-" * 30)
print(f"TOTAL DE ITENS: {quantidade_itens}")
print(f"TOTAL A PAGAR: R$ {total_geral:.2f}")
print("="*30)