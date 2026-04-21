import pyodbc
from datetime import datetime

dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-3E9BL5V\\SQLEXPRESS;"
    "DATABASE=banco;"
    "Trusted_Connection=yes;"
)

#  conexão única
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()


def buscar():
    try:
        nome = input('Qual nome você quer buscar? ').strip()

        comando = "SELECT * FROM vendas WHERE cliente = ?"
        cursor.execute(comando, (nome,))
        resultado = cursor.fetchall()

        if not resultado:
            print("Cliente não encontrado")
        else:
            for linha in resultado:
                print(f"ID: {linha[0]} | Cliente: {linha[1]} | Produto: {linha[2]} | Data: {linha[3]} | Valor: {linha[4]} | Quantidade: {linha[5]}")

    except Exception as erro:
        print("Erro ao buscar:", erro)


def listar():
    try:
        cursor.execute("SELECT * FROM vendas")
        resultado = cursor.fetchall()

        for linha in resultado:
            print(f"ID: {linha[0]} | Cliente: {linha[1]} | Produto: {linha[2]} | Data: {linha[3]} | Valor: {linha[4]} | Quantidade: {linha[5]}")

    except Exception as erro:
        print("Erro ao listar:", erro)


def pedir_data():
    while True:
        data_input = input("Digite a data (YYYY-MM-DD): ")

        try:
            data_formatada = datetime.strptime(data_input, "%Y-%m-%d")
            return data_formatada
        except:
            print("Data inválida! Use o formato YYYY-MM-DD.")


def cadastrar():
    try:
        id = int(input('Qual é o ID do cliente? ').strip())
        cliente = input('Qual é o nome do cliente? ').strip().lower()
        produto = input('Qual é o nome do produto? ').strip().lower()
        data = pedir_data()
        preco = float(input('Diga o valor (sem formatação): ').strip())
        quantidade = int(input('Quantos pedidos foram feitos? ').strip())

        cursor.execute("SELECT * FROM vendas WHERE id_vendas = ?", (id,))
        if cursor.fetchone():
            print("Esse ID já existe!")
            return

        comando = """INSERT INTO vendas
        (id_vendas, cliente, produto, data_venda, preco, quantidade)
        VALUES (?, ?, ?, ?, ?, ?)"""

        valores = (id, cliente, produto, data, preco, quantidade)

        cursor.execute(comando, valores)
        conexao.commit()

        print("Cadastrado com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar:", erro)


def atualizar():
    try:
        id = int(input('Qual o ID do cliente? ').strip())

        cursor.execute("SELECT * FROM vendas WHERE id_vendas = ?", (id,))
        resultado = cursor.fetchall()

        if not resultado:
            print('Poxa! não encontrei esse ID cadastrado.')
        else:
            atualizacao = input('O que você gostaria de atualizar? (nome/produto/preco/quantidade) ').strip().lower()

            if not atualizacao:
                print("Você precisa digitar uma opção válida!")
                return

            if atualizacao == "nome":
                novo_nome = input("Digite o novo nome: ").strip().lower()

                if not novo_nome:
                    print("Valor inválido!")
                    return

                comando = "UPDATE vendas SET cliente = ? WHERE id_vendas = ?"
                cursor.execute(comando, (novo_nome, id))
                conexao.commit()

                print(f"Atualizado com sucesso! Novo nome: {novo_nome}")

            elif atualizacao == "produto":
                novo_produto = input("Digite o nome do produto: ").strip().lower()

                if not novo_produto:
                    print("Você precisa digitar um produto válido!")
                    return

                comando = "UPDATE vendas SET produto = ? WHERE id_vendas = ?"
                cursor.execute(comando, (novo_produto, id))
                conexao.commit()

                print(f"Atualizado com sucesso! Novo produto: {novo_produto}")

            elif atualizacao == "preco":
                novo_preco = float(input("Digite o novo preço: ").strip())

                comando = "UPDATE vendas SET preco = ? WHERE id_vendas = ?"
                cursor.execute(comando, (novo_preco, id))
                conexao.commit()

                print(f"Atualizado com sucesso! Novo preço: {novo_preco}")

            elif atualizacao == "quantidade":
                nova_quantidade = int(input("Digite a nova quantidade: ").strip())

                comando = "UPDATE vendas SET quantidade = ? WHERE id_vendas = ?"
                cursor.execute(comando, (nova_quantidade, id))
                conexao.commit()

                print(f"Atualizado com sucesso! Nova quantidade: {nova_quantidade}")

            else:
                print("Opção inválida!")

    except Exception as erro:
        print("Erro ao atualizar:", erro)


#  MENU PRINCIPAL
def main():
    while True:
        print("\n1 - Buscar por nome")
        print("2 - Listar")
        print("3 - Cadastrar")
        print("4 - Atualizar venda")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            buscar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            cadastrar()
        elif opcao == "4":
            atualizar()
        elif opcao == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida!")


#  EXECUÇÃO
main()

# fechar conexão
conexao.close()