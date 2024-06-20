# Leitura dos dados dos produtos
nome_produto1 = input("*Digite o nome do produto 1:* ")
preco_unitario1 = float(input("*Digite o preço unitário do produto 1:* "))
quantidade1 = int(input("*Digite a quantidade do produto 1:* "))

nome_produto2 = input("*Digite o nome do produto 2:* ")
preco_unitario2 = float(input("*Digite o preço unitário do produto 2:* "))
quantidade2 = int(input("*Digite a quantidade do produto 2:* "))

nome_produto3 = input("*Digite o nome do produto 3:* ")
preco_unitario3 = float(input("*Digite o preço unitário do produto 3:* "))
quantidade3 = int(input("*Digite a quantidade do produto 3:* "))

# Cálculo do preço total de cada produto e total da compra
total_produto1 = preco_unitario1 * quantidade1
total_produto2 = preco_unitario2 * quantidade2
total_produto3 = preco_unitario3 * quantidade3
preco_total = total_produto1 + total_produto2 + total_produto3

# Impressão do resultado formatado
print(f"Total: R${preco_total:.2f}")
