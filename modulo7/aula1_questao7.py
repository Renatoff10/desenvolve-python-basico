import random

def encrypt(nomes):
    n = random.randint(1, 10)
    nomes_criptografados = []
    for nome in nomes:
        criptografado = ''.join(chr(((ord(c) - 33 + n) % 94) + 33) for c in nome)
        nomes_criptografados.append(criptografado)
    return nomes_criptografados, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")
