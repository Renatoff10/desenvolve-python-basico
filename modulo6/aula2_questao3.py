import random
from collections import Counter

# Preencher duas listas com 20 valores inteiros aleatórios entre 0 a 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Criar uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas
interseccao = list(set(lista1) & set(lista2))

# Imprimir ambas as listas
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

# Imprimir a lista intersecção ordenada
print(f"Interseccao: {sorted(interseccao)}")

# Contar a quantidade de vezes que cada elemento aparece em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Imprimir a contagem de elementos
print("Contagem")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})")
