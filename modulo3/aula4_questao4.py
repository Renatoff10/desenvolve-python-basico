# Leitura da distância em km e peso em kg
distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

# Calculando o valor do frete
if peso <= 10:
    if distancia <= 100:
        valor_frete = peso * 1
    elif distancia <= 300:
        valor_frete = peso * 1.50
    else:
        valor_frete = peso * 2
else:
    if distancia <= 100:
        valor_frete = peso * 1 + 10
    elif distancia <= 300:
        valor_frete = peso * 1.50 + 10
    else:
        valor_frete = peso * 2 + 10

# Imprimindo o valor do frete
print(f"O valor do frete é R${valor_frete:.2f}")
