# Solicitando idade, quantidade de jogos e número de vitórias
idade = int(input("Digite sua idade: "))
jogou_tres_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? ").lower() == "true"
venceu_jogo = int(input("Quantos jogos já venceu? ")) >= 1

# Verificando as condições para ingressar no clube de jogos de tabuleiro
apto_ingresso = idade >= 16 and idade <= 18 and jogou_tres_jogos and venceu_jogo

# Imprimindo o resultado
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto_ingresso}")
