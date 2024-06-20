def calculate_average_age(n):
    """
    Calcula a média de idade dos respondentes.

    Args:
        n: O número de respondentes.

    Returns:
        A média de idade.
    """
    total_age = 0

    # Lê as idades dos respondentes
    for _ in range(n):
        age = int(input("Digite a idade do respondente: "))
        total_age += age

    # Calcula a média de idade
    average_age = total_age / n
    return average_age

# Lê o número de respondentes
n = int(input("Digite o número de respondentes: "))

# Calcula e imprime a média de idade
average_age = calculate_average_age(n)
print("A média de idade dos respondentes é:", average_age)
