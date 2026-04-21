import pyodbc
from datetime import datetime

dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-3E9BL5V\\SQLEXPRESS;"
    "DATABASE=banco;"
    "Trusted_Connection=yes;"
)

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

    except Exception:
        print("Erro ao buscar.")


def listar():
    try:
        cursor.execute("SELECT * FROM vendas")
        resultado = cursor.fetchall()

        for linha in resultado:
            print(f"ID: {linha[0]} | Cliente: {linha[1]} | Produto: {linha[2]} | Data: {linha[3]} | Valor: {linha[4]} | Quantidade: {linha[5]}")

    except Exception:
        print("Erro ao listar.")


def pedir_data():
    while True:
        data_input = input("Digite a data (YYYY-MM-DD): ")

        try:
            return datetime.strptime(data_input, "%Y-%m-%d")
        except:
            print("Data inválida! Use o formato YYYY-MM-DD.")


def cadastrar():
    try:
        id_venda = int(input('Qual é o ID da venda? ').strip())
        cliente = input('Qual é o nome do cliente? ').strip().lower()
        produto = input('Qual é o nome do produto? ').strip().lower()
        data = pedir_data()

        try:
            preco = float(input('Diga o valor (sem formatação): ').strip())
        except ValueError:
            print("Preço inválido!")
            return

        quantidade = int(input('Quantos pedidos foram feitos? ').strip())

        cursor.execute("SELECT * FROM vendas WHERE id_vendas = ?", (id_venda,))
        if cursor.fetchone():
            print("Esse ID já existe!")
            return

        comando = """INSERT INTO vendas
        (id_vendas, cliente, produto, data_venda, preco, quantidade)
        VALUES (?, ?, ?, ?, ?, ?)"""

        valores = (id_venda, cliente, produto, data, preco, quantidade)

        cursor.execute(comando, valores)
        conexao.commit()

        print("Cadastrado com sucesso!")

    except Exception:
        print("Erro ao cadastrar.")


def atualizar():
    try:
        id_venda = int(input('Qual o ID da venda? ').strip())

        cursor.execute("SELECT * FROM vendas WHERE id_vendas = ?", (id_venda,))
        resultado = cursor.fetchone()

        if not resultado:
            print('Poxa! não encontrei esse ID cadastrado.')
        else:
            atualizacao = input('O que você gostaria de atualizar? (nome/produto/preco/quantidade) ').strip().lower()

            if not atualizacao:
                print("Você precisa digitar uma opção válida!")
                return

            if atualizacao == "nome":
                novo_nome = input("Digite o novo nome: ").strip()

                if not novo_nome:
                    print("Valor inválido!")
                    return

                comando = "UPDATE vendas SET cliente = ? WHERE id_vendas = ?"
                cursor.execute(comando, (novo_nome, id_venda))

            elif atualizacao == "produto":
                novo_produto = input("Digite o nome do produto: ").strip().lower()

                if not novo_produto:
                    print("Você precisa digitar um produto válido!")
                    return

                comando = "UPDATE vendas SET produto = ? WHERE id_vendas = ?"
                cursor.execute(comando, (novo_produto, id_venda))

            elif atualizacao == "preco":
                novo_preco = float(input("Digite o novo preço: ").strip())

                comando = "UPDATE vendas SET preco = ? WHERE id_vendas = ?"
                cursor.execute(comando, (novo_preco, id_venda))

            elif atualizacao == "quantidade":
                nova_quantidade = int(input("Digite a nova quantidade: ").strip())

                comando = "UPDATE vendas SET quantidade = ? WHERE id_vendas = ?"
                cursor.execute(comando, (nova_quantidade, id_venda))

            else:
                print("Opção inválida!")
                return

            conexao.commit()
            print("Atualizado com sucesso!")

    except Exception:
        print("Erro ao atualizar.")


def deletar():
    try:
        id_venda = int(input('Qual é o ID da venda? ').strip())

        cursor.execute("SELECT * FROM vendas WHERE id_vendas = ?", (id_venda,))
        resultado = cursor.fetchone()

        if not resultado:
            print('Poxa! não encontrei esse ID cadastrado.')
        else:
            print("Cadastro encontrado:")
            print(f"ID: {resultado[0]} | Cliente: {resultado[1]} | Produto: {resultado[2]} | Data: {resultado[3]} | Valor: {resultado[4]} | Quantidade: {resultado[5]}")

            exclusao = input('Tem certeza? [S/N] ').strip().lower()

            if exclusao in ['s', 'sim']:
                comando = "DELETE FROM vendas WHERE id_vendas = ?"
                cursor.execute(comando, (id_venda,))
                conexao.commit()
                print("Venda excluída com sucesso!")
            else:
                print('Nada foi excluído.')

    except Exception:
        print("Erro ao deletar.")


def main():
    while True:
        print("\n1 - Buscar por nome")
        print("2 - Listar")
        print("3 - Cadastrar")
        print("4 - Atualizar venda")
        print("5 - Deletar venda")
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
        elif opcao == "5":
            deletar()
        elif opcao == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida!")


main()
conexao.close()