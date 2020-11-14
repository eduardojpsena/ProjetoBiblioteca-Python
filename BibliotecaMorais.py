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
          " 2- Atualizar quantidade de titulo \n"
          " 3- Remover titulos desatualizados \n"
          " 4- Buscar exemplares \n"
          " 5- Importar dados \n"
          " 6- Obter status do titulo \n"
          " 7- Gerar relatorio do acervo \n"
          " 8- Gerar relatorio por categoria de livro \n"
          " 9- Gerar relatorio por tematica do livro \n"
          "10- Sair do sistema \n")
    resposta = int(input("Digite a opção desejada: "))
    return resposta

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
    while opcaoMenu != 12:

        if opcaoMenu == 1:  # Cadastro de livros

            livros.append(cadastrodenovoslivros())

            opcaoMenu = menu()

        '''elif opcaoMenu == 2:

        elif opcaoMenu == 3:

        elif opcaoMenu == 4:

        elif opcaoMenu == 5:

        elif opcaoMenu == 6:

        elif opcaoMenu == 7:

        elif opcaoMenu == 8:

        elif opcaoMenu == 9:

        elif opcaoMenu == 10:
            break
        else:
            print("Entrada invalida tente novamente !!!")
            resposta = input("Digite a opção desejada: ")'''
main()


