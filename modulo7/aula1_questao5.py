frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contagem_vogais = [i for i, letra in enumerate(frase) if letra in vogais]
print(f"{len(contagem_vogais)} vogais")
print(f"Índices {contagem_vogais}")
