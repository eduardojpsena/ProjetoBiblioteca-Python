import json
import os.path

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
    livroEncontrado = 'não'
    livroNaoEncontrado = 'não'
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
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"
        if livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com esse titulo • ")

    if opcaoBusca == 2:
        anoLivro = str(input("Ano: "))
        for i in livros:
            if i["ano"] == anoLivro:
                print(i)
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"
        if livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com esse ano de lançamento • ")

    if opcaoBusca == 3:
        catLivro = str(input("Categoria [Fisico/Digital]: "))
        for i in livros:
            if i["categoria"] == catLivro:
                print(i)
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"
        if livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com essa categoria • ")
    if opcaoBusca == 4:
        temaLivro = str(input("Tematica: "))
        for i in livros:
            if i["tematica"] == temaLivro:
                print(i)
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"
        if livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com essa temática • ")

def atualizarQuantidade():
    nomeLivro = str(input("Digite o titulo do livro que deseja atualizar a quantidade: "))
    quantLivro = int(input("Nova quantidade: "))
    for i in livros:
        if i["titulo"] == nomeLivro:
            i["quantidade"] = quantLivro

def removerLivros():  #Função para remover livros do sistema
    removerLivro = str(input("Digite o titulo do livro que deseja remover: "))
    for i in livros:
        if i["titulo"] == removerLivro:
            livros.remove(i)

def importarLivros():  #Função para importar livros para o sistema
    opcao = str(input(f"Deseja importar os dados do arquivo 'livros.json'? [S/N]: "))[0].upper().strip()
    if opcao == 'S':
        with open('livros.json', 'r', encoding='utf8') as json_file:
            obj = json.loads(json_file.read())
            for i in obj:
                livros.append(i)

            print("• Dados importados com sucesso •")
    elif opcao == 'N':
        opc = str(input(f"Deseja importar os dados de outro arquivo json? [S/N]: "))[0].upper().strip()
        if opc == "S":
            arq = str(input("Qual o nome do arquivo json a ser importado? siga o padrão "
                            "[nomeArquivo.json]: "))
            if os.path.exists(arq) == True:
                with open(arq, 'r', encoding='utf8') as json_file:
                    obj = json.loads(json_file.read())
                    for i in obj:
                        livros.append(i)

                    print("• Dados importados com sucesso •")
            else:
                print("• Arquivo não existente •")
                importarLivros()
        elif opc == "N":
            pass
        else:
            print("Opção inválida, tente novamente.")
            importarLivros()
    else:
        print("Opção inválida, tente novamente.")
        importarLivros()

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
    importarLivros()
    opcaoMenu = menu()
    while opcaoMenu != 10:

        if opcaoMenu == 1:  # Cadastro de livros
            print("• CADASTRO DE LIVROS •\n")
            livros.append(cadastrodenovoslivros())

            export = str(input("Deseja exportar os dados do livro cadastrados "
                               "para o arquivo 'livros.json'? [S/N]: "))[0].strip().upper()
            if export == "S":
                with open('livros.json', 'w', encoding='utf-8') as json_file:
                    json.dump(livros, json_file, indent=1, ensure_ascii=False)
            elif export == "N":
                opc = str(input("Deseja exportar os dados para outro arquivo? [S/N]: "))[0].strip().upper()
                if opc == "S":
                    arq = str(input("Qual o nome do arquivo json a ser salvo? siga o padrão "
                                    "[nomeArquivo.json]: "))
                    with open(arq, 'w', encoding='utf-8') as json_file:
                        json.dump(livros, json_file, indent=1, ensure_ascii=False)
                    opcaoMenu = menu()
                else:
                    opcaoMenu = menu()
            else:
                print("Opção inválida")
                opcaoMenu = 1

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

        elif opcaoMenu == 5:  # Importar dados
            print("• IMPORTANDO DADOS •")
            livros.append(importarLivros())
            livros.pop(len(livros)-1)

            print(livros)
            opcaoMenu = menu()

        elif opcaoMenu == 6:  # Obter Status dos livro [alugado/disponivel]
            pass
        elif opcaoMenu == 7:  # Gerar relatórios do acervo completo, por categoria ou por temática
            pass
        elif opcaoMenu == 8:  # Alugar determinado titulo
            pass
        elif opcaoMenu == 9:  # Sair do sistema
            break
        else:
            print("Entrada invalida tente novamente !!!")
            opcaoMenu = menu()
main()


