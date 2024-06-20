# Solicitando classe e pontos de atributo
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()
pontos_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Verificando os pontos de atributo consistentes com a classe escolhida
if classe == "guerreiro":
    pontos_consistentes = pontos_forca >= 15 and pontos_magia <= 10
elif classe == "mago":
    pontos_consistentes = pontos_forca <= 10 and pontos_magia >= 15
elif classe == "arqueiro":
    pontos_consistentes = pontos_forca > 5 and pontos_magia > 5 and pontos_forca <= 15 and pontos_magia <= 15
else:
    pontos_consistentes = False

# Imprimindo o resultado
print(f"Pontos de atributo consistentes com a classe escolhida: {pontos_consistentes}")
