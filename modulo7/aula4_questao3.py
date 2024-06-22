def processar_estomago():
    with open("estomago.txt", "r", encoding='latin-1') as file:
        linhas = file.readlines()

    print("Primeiras 25 linhas:")
    for linha in linhas[:25]:
        print(linha.strip())
    
    print(f"\nNúmero de linhas do arquivo: {len(linhas)}")
    
    linha_maior = max(linhas, key=len)
    print(f"\nLinha com maior número de caracteres:\n{linha_maior.strip()}")
    
    mencoes_nonato = sum(1 for linha in linhas if re.search(r'\bnonato\b', linha, re.IGNORECASE))
    mencoes_iria = sum(1 for linha in linhas if re.search(r'\bíria\b', linha, re.IGNORECASE))
    print(f"\nNúmero de menções aos personagens 'Nonato': {mencoes_nonato}")
    print(f"Número de menções aos personagens 'Íria': {mencoes_iria}")

processar_estomago()
