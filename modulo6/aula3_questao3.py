import random

# Gerar lista com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print(f"Original: {lista}")

# Encontrar o intervalo com maior quantidade de números negativos
intervalo_negativos = []
max_negativos = 0
intervalo_inicial = 0

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sub_lista = lista[i:j]
        num_negativos = len([x for x in sub_lista if x < 0])
        if num_negativos > max_negativos:
            max_negativos = num_negativos
            intervalo_negativos = sub_lista
            intervalo_inicial = i

# Deletar o intervalo com maior quantidade de números negativos
del lista[intervalo_inicial:intervalo_inicial + len(intervalo_negativos)]
print(f"Editada: {lista}")
