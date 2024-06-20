# Solicitando as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verificando se ambas são maiores de 17 anos
podem_entrar = idade_juliana > 17 and idade_cris > 17

# Imprimindo o resultado
print(podem_entrar)
