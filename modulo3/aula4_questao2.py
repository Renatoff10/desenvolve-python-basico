# Leitura da avaliação do filme
avaliacao = int(input("Digite a avaliação do filme (de 1 a 5): "))

# Verificando a avaliação e imprimindo a classificação correspondente
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Digite um número de 1 a 5.")
