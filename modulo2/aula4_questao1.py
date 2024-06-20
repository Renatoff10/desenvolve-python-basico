# Leitura das dimensões do terreno e preço do metro quadrado
comprimento = int(input("Digite o comprimento do terreno (em metros): "))  # Leitura do comprimento
largura = int(input("Digite a largura do terreno (em metros): "))  # Leitura da largura
preco_m2 = float(input("Digite o preço do metro quadrado da região: "))  # Leitura do preço por metro quadrado

# Cálculo da área em metros quadrados
area_m2 = comprimento * largura

# Cálculo do preço total do terreno
preco_total = preco_m2 * area_m2

# Impressão do resultado formatado
print(f"O terreno possui {area_m2}m² e custa R${preco_total:.2f}")
