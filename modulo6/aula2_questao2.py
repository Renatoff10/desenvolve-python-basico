import random

# Gerar um valor aleatório entre 5 e 20
num_elementos = random.randint(5, 20)

# Gerar valores aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Imprimir a lista elementos
print(f"Lista elementos: {elementos}")

# Calcular e imprimir a soma dos valores da lista
soma_elementos = sum(elementos)
print(f"Soma dos valores da lista: {soma_elementos}")

# Calcular e imprimir a média dos valores da lista
media_elementos = soma_elementos / num_elementos
print(f"Média dos valores da lista: {media_elementos:.2f}")
