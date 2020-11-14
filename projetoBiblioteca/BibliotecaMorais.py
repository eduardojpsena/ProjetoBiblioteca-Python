# Funcionalidades implementadas: Cadastro novos livros, Cadastro Categorias
# Adicionar titulos que podem ser reservados, Login no sistema
# Grupo:    Eduardo José Pereira de Sena
#           André Luis Moreira da Silva Santos

def cadastroFuncionario():
    idFuncionario = 'admin'
    senhaFuncionario = '1234'
    return {'id': idFuncionario, 'senha': senhaFuncionario}

def loginSistema():
    while True:
        idLogin = str(input("ID: "))
        senhaLogin = str(input("Senha: "))
        if idLogin == cadastroFuncionario()['id'] and senhaLogin == cadastroFuncionario()['senha']:
            return True
            break
        else:
            print("Login ou senha inválida, tente novamente")

def cadastrodenovoslivros():
    titulo = input("Digite o titulo do livro: ")
    ano = input("Digite o ano do livro: ")
    quantidade = input("Digite a quantidade de exemplares: ")
    categoria = input("Livro fisico ou digital: ")
    tematica = input("Qual o tema do livro: ")
    reservado = input("Livro é reservado? [S/N]: ")
    return {'titulo': titulo, 'ano': ano, 'quantidade': quantidade, 'categoria': categoria,
            'tematica': tematica, 'reservado': reservado}


def menu():
    print("\n ### MENU DE OPÇÕES ###")
    print(" 1- Cadastro de novos livros \n"
          " 2- Atualizar quantidade de livros \n"
          " 3- Remover titulos desatualizados \n"
          " 4- Buscar exemplares \n"
          " 5- Importar dados \n"
          " 6- Obter status do titulo \n"
          " 7- Gerar relatorios\n"
          " 8- Alugar livro \n"
          " 9- Sair do sistema \n")
    resposta = int(input("Digite a opção desejada: "))
    return resposta

def buscarLivros():
    print("[1] Buscar por titulo\n"
          "[2] Buscar por ano\n"
          "[3] Buscar por categoria\n"
          "[4] Buscar por tema")
    opcaoBusca = int(input("Digite a opção: "))
    if opcaoBusca == 1:
        nomeLivro = str(input("Titulo: "))
        for i in livros:
            if i["titulo"] == nomeLivro:
                print(i)
            else:
                print("• Não existe livro com o titulo desejado •")
    if opcaoBusca == 2:
        anoLivro = str(input("Ano: "))
        for i in livros:
            if i["ano"] == anoLivro:
                print(i)
            else:
                print("• Não existe livro com o ano desejado •")
    if opcaoBusca == 3:
        catLivro = str(input("Categoria: "))
        for i in livros:
            if i["categoria"] == catLivro:
                print(i)
            else:
                print("• Não existe livro com a categoria desejada •")
    if opcaoBusca == 4:
        temaLivro = str(input("Tematica: "))
        for i in livros:
            if i["tematica"] == temaLivro:
                print(i)
            else:
                print("• Não existe livro com a tematica desejada •")

def atualizarQuantidade():
    nomeLivro = str(input("Digite o titulo do livro que deseja atualizar a quantidade: "))
    quantLivro = int(input("Nova quantidade: "))
    for i in livros:
        if i["titulo"] == nomeLivro:
            i["quantidade"] = quantLivro

def removerLivros():
    removerLivro = str(input("Digite o titulo do livro que deseja remover: "))
    for i in livros:
        if i["titulo"] == removerLivro:
            livros.remove(i)

## VARIAVEIS
livros = []

def main():

    ##lOGIN DO SISTEMA - id = admin / senha = 1234
    print("• Morais Lybrary •")
    statusLogin = loginSistema()

    while True:
        if statusLogin == True:
            print("• Login efetuado com sucesso •")
            break
        else:
            print("• Id ou senha inválido, tente novamente •")
            statusLogin = loginSistema()

    opcaoMenu = menu()
    while opcaoMenu != 10:
        print("• CADASTRO DE LIVROS •\n")
        if opcaoMenu == 1:  # Cadastro de livros

            livros.append(cadastrodenovoslivros())

            opcaoMenu = menu()

        elif opcaoMenu == 2:  # Atualizar quantidade de um determinado titulo
            print("• ATUALIZAÇÃO DE QUANTIDADE •\n")
            atualizarQuantidade()

            opcaoMenu = menu()

        elif opcaoMenu == 3:  # Remover determinado titulo
            print("• REMOÇÃO DE TITULOS •\n")
            removerLivros()

            opcaoMenu = menu()

        elif opcaoMenu == 4:  # Buscar livros por titulo, ano, categoria[fisico/digital] ou temática
            print("• BUSCA DE EXEMPLARES •")
            buscarLivros()

            opcaoMenu = menu()

        '''elif opcaoMenu == 5:  # Importar dados

        elif opcaoMenu == 6:  # Obter Status dos livro [alugado/disponivel]

        elif opcaoMenu == 7:  # Gerar relatórios do acervo completo, por categoria ou por temática

        elif opcaoMenu == 8:  # Alugar determinado titulo

        elif opcaoMenu == 9:  # Sair do sistema
            break
        else:
            print("Entrada invalida tente novamente !!!")
            resposta = input("Digite a opção desejada: ")'''
main()


