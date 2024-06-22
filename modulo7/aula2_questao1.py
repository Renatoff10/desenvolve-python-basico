def data_nascimento_extenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    dia, mes, ano = data.split('/')
    mes_extenso = meses[int(mes) - 1]
    return f"Você nasceu em {dia} de {mes_extenso} de {ano}."

data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
print(data_nascimento_extenso(data))
