# Depósito inicial na conta poupança
saldo = 500.0

# Calculando o saldo após 3 meses de juros
juros = 1.01  # 1% de juros ao mês
saldo *= juros ** 3  # Equivalente a saldo = saldo * juros * juros * juros

# Imprimindo o novo saldo após 3 meses
print("Após 3 meses meu novo saldo é")
print(saldo)
