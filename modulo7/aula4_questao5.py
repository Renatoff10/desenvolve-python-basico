def criar_arquivo_csv():
    livros = [
        {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1178},
        {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
        {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 96},
        # Adicione mais livros aqui
    ]
    
    with open("meus_livros.csv", "w", newline='') as file:
        file.write("Título,Autor,Ano de publicação,Número de páginas\n")
        for livro in livros:
            file.write(f"{livro['Título']},{livro['Autor']},{livro['Ano de publicação']},{livro['Número de páginas']}\n")

criar_arquivo_csv()
