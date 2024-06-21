# Solicitar uma quantidade indefinida de números inteiros
numeros = []

while len(numeros) < 4 or (num := int(input("Digite um número inteiro (ou 0 para parar): "))) != 0:
    numeros.append(num)

# Remover o zero final, se for o caso
if numeros[-1] == 0:
    numeros.pop()

# Imprimir a lista original
print(f"Lista original: {numeros}")

# Imprimir os 3 primeiros elementos
print(f"3 primeiros elementos: {numeros[:3]}")

# Imprimir os 2 últimos elementos
print(f"2 últimos elementos: {numeros[-2:]}")

# Imprimir a lista invertida
print(f"Lista invertida: {numeros[::-1]}")

# Imprimir os elementos de índice par
print(f"Elementos de índice par: {numeros[::2]}")

# Imprimir os elementos de índice ímpar
print(f"Elementos de índice ímpar: {numeros[1::2]}")
