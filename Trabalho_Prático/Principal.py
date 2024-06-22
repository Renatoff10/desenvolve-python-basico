import csv

# Funções para gerenciar usuários

def carregar_usuarios():
    usuarios = []
    try:
        with open('usuarios.txt', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                usuarios.append(row)
    except FileNotFoundError:
        pass
    return usuarios

def salvar_usuarios(usuarios):
    with open('usuarios.txt', 'w', newline='') as file:
        fieldnames = ["nome", "senha", "permissao"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(usuarios)

def criar_usuario(usuarios):
    nome = input("Nome: ")
    senha = input("Senha: ")
    permissao = input("Permissão (gerente/funcionario/cliente): ")
    usuarios.append({"nome": nome, "senha": senha, "permissao": permissao})
    salvar_usuarios(usuarios)

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def atualizar_usuario(usuarios):
    nome = input("Nome do usuário a ser atualizado: ")
    for usuario in usuarios:
        if usuario["nome"] == nome:
            usuario["senha"] = input("Nova senha: ")
            usuario["permissao"] = input("Nova permissão: ")
            salvar_usuarios(usuarios)
            return
    print("Usuário não encontrado")

def deletar_usuario(usuarios):
    nome = input("Nome do usuário a ser removido: ")
    usuarios = [usuario for usuario in usuarios if usuario["nome"] != nome]
    salvar_usuarios(usuarios)

# Funções para gerenciar produtos

def carregar_produtos():
    produtos = []
    try:
        with open('produtos.txt', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["preco"] = float(row["preco"])
                row["quantidade"] = int(row["quantidade"])
                produtos.append(row)
    except FileNotFoundError:
        pass
    return produtos

def salvar_produtos(produtos):
    with open('produtos.txt', 'w', newline='') as file:
        fieldnames = ["codigo", "nome", "preco", "quantidade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)

def criar_produto(produtos):
    codigo = input("Código: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos(produtos)

def listar_produtos(produtos):
    for produto in produtos:
        print(produto)

def atualizar_produto(produtos):
    codigo = input("Código do produto a ser atualizado: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produto["nome"] = input("Novo nome: ")
            produto["preco"] = float(input("Novo preço: "))
            produto["quantidade"] = int(input("Nova quantidade: "))
            salvar_produtos(produtos)
            return
    print("Produto não encontrado")

def deletar_produto(produtos):
    codigo = input("Código do produto a ser removido: ")
    produtos = [produto for produto in produtos if produto["codigo"] != codigo]
    salvar_produtos(produtos)

def buscar_produto(produtos):
    termo = input("Nome ou código do produto: ")
    for produto in produtos:
        if produto["nome"] == termo or produto["codigo"] == termo:
            print(produto)
            return
    print("Produto não encontrado")

def ordenar_produtos_por_nome(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x["nome"])
    for produto in produtos_ordenados:
        print(produto)

def ordenar_produtos_por_preco(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x["preco"])
    for produto in produtos_ordenados:
        print(produto)

# Menu principal

def menu():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()

    while True:
        print("\n1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n1. Criar Usuário")
            print("2. Listar Usuários")
            print("3. Atualizar Usuário")
            print("4. Deletar Usuário")
            subopcao = input("Escolha uma opção: ")

            if subopcao == "1":
                criar_usuario(usuarios)
            elif subopcao == "2":
                listar_usuarios(usuarios)
            elif subopcao == "3":
                atualizar_usuario(usuarios)
            elif subopcao == "4":
                deletar_usuario(usuarios)

        elif opcao == "2":
            print("\n1. Criar Produto")
            print("2. Listar Produtos")
            print("3. Atualizar Produto")
            print("4. Deletar Produto")
            print("5. Buscar Produto")
            print("6. Ordenar Produtos por Nome")
            print("7. Ordenar Produtos por Preço")
            subopcao = input("Escolha uma opção: ")

            if subopcao == "1":
                criar_produto(produtos)
            elif subopcao == "2":
                listar_produtos(produtos)
            elif subopcao == "3":
                atualizar_produto(produtos)
            elif subopcao == "4":
                deletar_produto(produtos)
            elif subopcao == "5":
                buscar_produto(produtos)
            elif subopcao == "6":
                ordenar_produtos_por_nome(produtos)
            elif subopcao == "7":
                ordenar_produtos_por_preco(produtos)

        elif opcao == "3":
            break

if __name__ == "__main__":
    menu()
