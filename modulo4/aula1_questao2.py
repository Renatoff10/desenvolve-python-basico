cont = 0

while True:
  n = int(input("Digite um número: "))
  if n < 0:
    break
  cont = cont + 1

print("Contador:", cont)
print("Fim")
