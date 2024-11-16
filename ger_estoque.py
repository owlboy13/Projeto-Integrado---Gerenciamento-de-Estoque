import pandas as pd

#TESTE COMMIT
# Carregar o banco de dados do Excel ou criar um novo caso não exista
try:
    banco_de_dados = pd.read_excel("banco_de_dados.xlsx")
    estoque = banco_de_dados.to_dict(orient="records")
    print("Banco de dados carregado com sucesso!")
except FileNotFoundError:
    estoque = []
    print("Arquivo 'banco_de_dados.xlsx' não encontrado. Um novo será criado ao salvar.")

# Função para salvar o estoque no Excel
def salvar_dados():
    df = pd.DataFrame(estoque)
    df.to_excel("banco_de_dados.xlsx", index=False)
    print("Dados salvos no banco de dados com sucesso!")

# Função para deletar um produto
def deletar_produto(nome):
    global estoque  # Garantir que estamos manipulando a variável global
    for produto in estoque:
        if produto["nome"] == nome:
            estoque.remove(produto)
            salvar_dados()
            print(f"Produto '{nome}' removido com sucesso!")
            return
    print(f"Produto '{nome}' não encontrado no estoque!")

# Função para cadastrar novos produtos
def adicionar_produto(nome, categoria, quantidade, preco, localizacao):
    produto = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
        "localizacao": localizacao
    }
    estoque.append(produto)
    salvar_dados()
    print(f"Produto '{nome}' adicionado com sucesso!")

# Função para atualizar o estoque
def atualizar_estoque(nome, quantidade, operacao):
    for produto in estoque:
        if produto["nome"] == nome:
            if operacao == "entrada":
                produto["quantidade"] += quantidade
            elif operacao == "saida":
                if produto["quantidade"] >= quantidade:
                    produto["quantidade"] -= quantidade
                else:
                    print("Quantidade insuficiente no estoque!")
                    return
            salvar_dados()
            print(f"Estoque de '{nome}' atualizado com sucesso!")
            return
    print(f"Produto '{nome}' não encontrado!")

# Função para rastrear localização de um produto
def rastrear_produto(nome):
    for produto in estoque:
        if produto["nome"] == nome:
            print(f"Produto '{nome}' está localizado em: {produto['localizacao']}")
            return
    print(f"Produto '{nome}' não encontrado!")

# Função para gerar relatórios
def gerar_relatorio():
    print("\n--- Relatório de Estoque ---")
    for produto in estoque:
        status = produto['quantidade']
        if status > 15:
            status = "Excesso de estoque"
        elif status < 5:
            status = "Baixo Estoque"
        else:
            status = "Estoque normal"
        print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, Status: {status}")
    print("---------------------------\n")

# Programa principal
def menu():
    while True:
        print("\n--- Sistema de Gerenciamento de Estoque ---")
        print("1. Cadastrar Produto")
        print("2. Atualizar Estoque")
        print("3. Rastrear Produto")
        print("4. Gerar Relatório")
        print("5. Deletar Produto")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            localizacao = input("Localização: ")
            adicionar_produto(nome, categoria, quantidade, preco, localizacao)
        
        elif opcao == "2":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            operacao = input("Operação (entrada/saida): ").lower()
            atualizar_estoque(nome, quantidade, operacao)
        
        elif opcao == "3":
            nome = input("Nome do produto: ")
            rastrear_produto(nome)
        
        elif opcao == "4":
            gerar_relatorio()

        elif opcao == "5":
            nome = input("Qual produto deseja deletar do estoque? ")
            deletar_produto(nome)
        
        elif opcao == "6":
            print("Saindo do sistema. Até mais!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa
menu()
