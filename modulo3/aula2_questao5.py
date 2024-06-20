# Solicitando gênero, idade e tempo de serviço
genero = input("Digite seu gênero (M/F): ").upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Verificando se a pessoa pode se aposentar
if (genero == "F" and idade >= 60) or (genero == "M" and idade >= 65):
    pode_se_aposentar = True
elif tempo_servico >= 30:
    pode_se_aposentar = True
elif idade >= 60 and tempo_servico >= 25:
    pode_se_aposentar = True
else:
    pode_se_aposentar = False

# Imprimindo o resultado
print(pode_se_aposentar)
