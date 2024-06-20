# Leitura do número de experimentos
N = int(input())

# Inicialização dos contadores
quantidade_sapos = 0
quantidade_ratos = 0
quantidade_coelhos = 0
total_cobaias = 0

# Processamento dos experimentos
for _ in range(N):
    # Leitura da quantidade e tipo de cobaia
    entrada = input().split()
    Quantia = int(entrada[0])
    Tipo = entrada[1]

    # Atualização dos contadores
    if Tipo == 'S':
        quantidade_sapos += Quantia
    elif Tipo == 'R':
        quantidade_ratos += Quantia
    elif Tipo == 'C':
        quantidade_coelhos += Quantia
    
    total_cobaias += Quantia

# Cálculo dos percentuais
percentual_sapos = (quantidade_sapos / total_cobaias) * 100
percentual_ratos = (quantidade_ratos / total_cobaias) * 100
percentual_coelhos = (quantidade_coelhos / total_cobaias) * 100

# Saída dos resultados formatados
print(f"Total: {total_cobaias} cobaias")
print(f"Total de sapos: {quantidade_sapos}")
print(f"Total de ratos: {quantidade_ratos}")
print(f"Total de coelhos: {quantidade_coelhos}")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
