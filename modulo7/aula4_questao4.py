import random

def escolher_palavra():
    with open("gabarito_forca.txt", "r") as file:
        palavras = file.readlines()
    return random.choice(palavras).strip()

def obter_estagios_enforcado():
    with open("gabarito_enforcado.txt", "r") as file:
        estagios = file.read().split('\n\n')
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogar_forca():
    palavra = escolher_palavra()
    estagios = obter_estagios_enforcado()
    tentativas = 6
    letras_corretas = ["_"] * len(palavra)
    letras_erradas = []

    while tentativas > 0:
        print(" ".join(letras_corretas))
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    letras_corretas[i] = letra
        else:
            tentativas -= 1
            letras_erradas.append(letra)
            imprime_enforcado(tentativas, estagios)

        if "_" not in letras_corretas:
            print(f"Parabéns, você ganhou! A palavra era {palavra}.")
            break
    else:
        print(f"Você perdeu! A palavra era {palavra}.")

jogar_forca()
