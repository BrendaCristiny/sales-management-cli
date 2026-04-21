Sales Management CLI
Sistema de gerenciamento de vendas desenvolvido em Python com integração ao SQL Server.

Funcionalidades:
Buscar vendas por nome do cliente,
Listar todas as vendas,
Cadastrar nova venda,
Atualizar dados (cliente, produto, preço e quantidade).

Tecnologias utilizadas:
Python,
SQL Server,
Pyodbc.

Estrutura do projeto:
O sistema funciona via terminal (CLI), permitindo interação direta com o usuário para realizar operações no banco de dados.

Demonstração:

Exemplo de uso no terminal;

1 - Buscar por nome
2 - Listar
3 - Cadastrar
4 - Atualizar venda
0 - Sair

Como executar?

1- Clone o repositório:
git clone https://github.com/BrendaCristiny/sales-management-cli.git
2- Instale as dependências:
pip install pyodbc
3-Configure a conexão com seu SQL Server no código:
SERVER=SEU_SERVIDOR
DATABASE=SEU_BANCO
4- Execute o programa:
python sales_cli.py


Este projeto foi desenvolvido com foco em:

Integração entre Python e banco de dados
Execução de comandos SQL via código
Estruturação de um sistema com menu interativo
Tratamento de erros com try/except
Validação de dados de entrada

Próximas melhorias:
Implementar exclusão de registros (DELETE)
Melhorar tratamento de erros
Refatorar código em módulos
Criar versão com API (FastAPI)
Implementar sistema bancário

Autora:
Brenda Cristiny
