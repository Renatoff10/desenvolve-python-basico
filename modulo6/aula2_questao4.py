# Receber duas listas de números do usuário
def receber_lista(nome_lista):
    n = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    for i in range(n):
        elemento = int(input(f"Digite o elemento {i + 1} da {nome_lista}: "))
        lista.append(elemento)
    return lista

lista1 = receber_lista("lista 1")
lista2 = receber_lista("lista 2")

# Combinar as duas listas de forma alternada
lista_intercalada = []
tamanho_max = max(len(lista1), len(lista2))

for i in range(tamanho_max):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])

# Imprimir a lista intercalada
print(f"Lista intercalada: {lista_intercalada}")
