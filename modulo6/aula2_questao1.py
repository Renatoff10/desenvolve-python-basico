import random

# Gerar 20 valores inteiros aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Imprimir a lista ordenada sem modificar a lista original
lista_ordenada = sorted(lista)
print(f"Lista ordenada: {lista_ordenada}")

# Imprimir a lista original
print(f"Lista original: {lista}")

# Índice do maior valor da lista
indice_maior = lista.index(max(lista))
print(f"Índice do maior valor da lista: {indice_maior}")

# Índice do menor valor da lista
indice_menor = lista.index(min(lista))
print(f"Índice do menor valor da lista: {indice_menor}")
