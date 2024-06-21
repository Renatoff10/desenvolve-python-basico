# Solicitar a frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais
vogais = sorted([letra for letra in frase if letra.lower() in 'aeiou'])
print(f"Vogais: {vogais}")

# Lista de consoantes
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in 'aeiou']
print(f"Consoantes: {consoantes}")
