# Leitura da temperatura em Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Conversão para Celsius
celsius = int((fahrenheit - 32) * (5/9))

# Impressão do resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
