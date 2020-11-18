import os.path
import json

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
    titulo = input("Digite o titulo do livro: ").title().strip()
    autor = input("Digite o autor do livro: ").title().strip()
    ano = input("Digite o ano do livro: ").strip()
    quantidade = input("Digite a quantidade de exemplares: ").strip()
    categoria = input("Livro fisico ou digital: ").title().strip()
    tematica = input("Qual o tema do livro: ").title().strip()
    reservado = input("Livro é reservado? [S/N]: ")[0].strip().lower()
    return {'titulo': titulo, 'autor': autor, 'ano': ano, 'quantidade': quantidade, 'categoria': categoria,
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
          " 8- Sair do sistema \n")
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
        nomeLivro = str(input("Titulo: ")).title().strip()
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
        catLivro = str(input("Categoria [Fisico/Digital]: ")).title().strip()
        for i in livros:
            if i["categoria"] == catLivro:
                print(i)
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"
        if livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com essa categoria • ")
    if opcaoBusca == 4:
        temaLivro = str(input("Tematica: ")).title().strip()
        for i in livros:
            if i["tematica"] == temaLivro:
                print(i)
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"
        if livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com essa temática • ")

def atualizarQuantidade():  # Função para atualizar a quantidade de determinado livro
    nomeLivro = str(input("Digite o titulo do livro que deseja atualizar a quantidade: ")).title().strip()
    quantLivro = int(input("Nova quantidade: "))
    for i in livros:
        if i["titulo"] == nomeLivro:
            i["quantidade"] = quantLivro

def removerLivros():  # Função para remover livros do sistema
    removerLivro = str(input("Digite o titulo do livro que deseja remover: ")).title().strip()
    for i in livros:
        if i["titulo"] == removerLivro:
            livros.remove(i)
    if removerLivro == "":
        pass

def importarLivros():  # Função para importar livros para o sistema
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

def statusLivro():
    livroEncontrado = 'não'
    livroNaoEncontrado = 'não'
    status = str(input("Digite o titulo do livro que deseja verificar: ")).title().strip()
    for i in livros:
        if i["titulo"] == status:
            if i['reservado'] == 's':
                print(f"• O livro {status} pode ser alugado •")
            elif i['reservado'] == 'n':
                print(f"• O livro {status} só pode ser lido na biblioteca •")
            livroEncontrado = "sim"
        else:
            livroNaoEncontrado = "sim"
    if livroEncontrado == "não" and livroNaoEncontrado == "sim":
        print("\n• Não foi encontrado livro com essa temática • ")

def relatorios():
    livroEncontrado = 'não'
    livroNaoEncontrado = 'não'
    relatorioCriado = False
    print("[1] Relatório Acervo\n"
          "[2] Relatório por categoria\n"
          "[3] Relatório por temática\n"
          "[4] Sair")
    opcaoBusca = int(input("Digite a opção: "))
    if opcaoBusca == 1:
        print("Relatório sendo gerado...")
        relatorio = open('relatoriocompleto.txt', 'w', encoding="utf8")
        relatorio.writelines('RELATÓRIO DO ACERVO'.center(40, " ") + "\n")
        relatorio.writelines('MORAIS LIBRARY'.center(40, " ") + "\n")
        for i in livros:
            relatorio.write("=" * 40 + "\n")
            relatorio.write(f"Livro: {i['titulo']}".center(40, " ") + "\n" +
                            f"Ano: {i['ano']}".center(40, " ") + "\n" +
                            f"Autor: {i['autor']}".center(40, " ") + "\n" +
                            f"Quantidade de exemplares: {i['quantidade']}".center(40, " ") + "\n" +
                            f"Categoria: {i['categoria']}".center(40, " ") + "\n" +
                            f"Tema: {i['tematica']}".center(40, " ") + "\n")
        relatorio.close()
        print('Relatório gerado com sucesso!!')

    elif opcaoBusca == 2:
        catLivro = str(input("Categoria [Fisico/Digital]: ")).title().strip()

        for i in livros:
            if i['categoria'] == catLivro and relatorioCriado == False:
                print("Relatório sendo gerado...")
                relatorio = open(f'relatorioLivros{catLivro}.txt', 'w', encoding="utf8")
                relatorio.writelines('RELATÓRIO DO ACERVO'.center(40, " ") + "\n")
                relatorio.writelines('MORAIS LIBRARY'.center(40, " ") + "\n")
                relatorio.writelines(F'CATEGORIA: Livros {catLivro}'.center(40, " ") + "\n")
                relatorioCriado = True
            if i['categoria'] == catLivro:
                relatorio.write("=" * 40 + "\n")
                relatorio.write(f"Livro: {i['titulo']}".center(40, " ") + "\n" +
                                f"Ano: {i['ano']}".center(40, " ") + "\n" +
                                f"Autor: {i['autor']}".center(40, " ") + "\n" +
                                f"Quantidade de exemplares: {i['quantidade']}".center(40, " ") + "\n" +
                                f"Categoria: {i['categoria']}".center(40, " ") + "\n" +
                                f"Tema: {i['tematica']}".center(40, " ") + "\n")
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"
        print(livroEncontrado)
        print(livroNaoEncontrado)
        if livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com essa categoria • ")

    elif opcaoBusca == 3:
        temaLivro = str(input("Tema: ")).title().strip()

        for i in livros:
            if i['tematica'] == temaLivro and relatorioCriado == False:
                print("Relatório sendo gerado...")
                relatorio = open(f'relatorio{temaLivro}.txt', 'w', encoding="utf8")
                relatorio.writelines('RELATÓRIO DO ACERVO'.center(40, " ") + "\n")
                relatorio.writelines('MORAIS LIBRARY'.center(40, " ") + "\n")
                relatorio.writelines(F'CATEGORIA: {temaLivro}'.center(40, " ") + "\n")
                relatorioCriado = True
            if i['tematica'] == temaLivro:
                relatorio.write("=" * 40 + "\n")
                relatorio.write(f"Livro: {i['titulo']}".center(40, " ") + "\n" +
                                f"Ano: {i['ano']}".center(40, " ") + "\n" +
                                f"Autor: {i['autor']}".center(40, " ") + "\n" +
                                f"Quantidade de exemplares: {i['quantidade']}".center(40, " ") + "\n" +
                                f"Categoria: {i['categoria']}".center(40, " ") + "\n" +
                                f"Tema: {i['tematica']}".center(40, " ") + "\n")
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"
        print(livroEncontrado)
        print(livroNaoEncontrado)
        if livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com essa tematica • ")
    elif opcaoBusca == 4:
        pass
    else:
        print("Opção inválida, tente novamente.")
        relatorios()

## VARIAVEIS
livros = []