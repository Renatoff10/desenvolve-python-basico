def maior(x, y, z):
  """
  Função que retorna o maior entre três números.

  Args:
      x: O primeiro número.
      y: O segundo número.
      z: O terceiro número.

  Returns:
      O maior número entre x, y e z.
  """
  # Encontra o maior entre x e y
  maior_xy = max(x, y)
  # Retorna o maior entre maior_xy e z
  return max(maior_xy, z)

# Lê o primeiro número
x = float(input("Digite o primeiro número: "))

# Lê o segundo número
y = float(input("Digite o segundo número: "))

# Lê o terceiro número
z = float(input("Digite o terceiro número: "))

# Encontra o maior número
maior_numero = maior(x, y, z)

# Imprime o maior número
print("O maior número é:", maior_numero)

print("Fim")
