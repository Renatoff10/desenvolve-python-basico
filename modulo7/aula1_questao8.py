def calcular_digito(cpf, multiplicadores):
    soma = sum(int(digito) * multiplicador for digito, multiplicador in zip(cpf, multiplicadores))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]
    if len(cpf_numeros) != 11:
        return False

    primeiro_digito = calcular_digito(cpf_numeros[:9], range(10, 1, -1))
    segundo_digito = calcular_digito(cpf_numeros[:10], range(11, 1, -1))

    return cpf_numeros[9] == primeiro_digito and cpf_numeros[10] == segundo_digito

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
if validar_cpf(cpf):
    print("Válido")
else:
    print("Inválido")
