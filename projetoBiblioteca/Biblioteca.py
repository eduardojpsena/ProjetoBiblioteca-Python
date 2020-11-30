import os.path
import json
from reportlab.pdfgen import canvas



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
    livroEncontrado = 'não'
    livroNaoEncontrado = 'não'
    nomeLivro = str(input("Digite o titulo do livro que deseja atualizar a quantidade: ")).title().strip()
    for i in livros:
        if i["titulo"] == nomeLivro:
            quantLivro = int(input("Nova quantidade: "))
            i["quantidade"] = quantLivro

            print("• Atualizado com sucesso •")
            livroEncontrado = "sim"
        else:
            livroNaoEncontrado = "sim"
    if livroEncontrado == "não" and livroNaoEncontrado == "sim":
        print("\n• Livro não encontrado • ")

def removerLivros():  # Função para remover livros do sistema
    livroEncontrado = 'não'
    livroNaoEncontrado = 'não'
    removerLivro = str(input("Digite o titulo do livro que deseja remover: ")).title().strip()
    for i in livros:
        if i["titulo"] == removerLivro:
            livros.remove(i)
            print(f"• Livro {removerLivro} removido com sucesso! •")
            livroEncontrado = "sim"
            return True
        else:
            livroNaoEncontrado = "sim"
    if removerLivro == "":
        pass
    if livroEncontrado == "não" and livroNaoEncontrado == "sim":
        print("\n• Livro não encontrado • ")
        return False

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

def GeradorPDF(lista, relatorio):

    try:
        nome_pdf = input('Informe o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 710
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(200, 780, 'MORAIS LIBRARY'.center(40, " "))
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(220, 754, f'•Relatório {relatorio}•'.center(40, " "))
        pdf.drawString(180, 740, '--------------------'*3)
        pdf.drawString(180, 725, f"Total de livros: {len(lista)}")
        pdf.drawString(180, 710, '--------------------'*3)
        for i in lista:
            x -= 20
            pdf.drawString(180, x, i['titulo'])
        pdf.save()
    except:
        print(f'Erro ao gerar {nome_pdf}.pdf')


def relatorios():
    livroEncontrado = 'não'
    livroNaoEncontrado = 'não'
    print("[1] Relatório Acervo\n"
          "[2] Relatório por categoria\n"
          "[3] Relatório por temática\n"
          "[4] Sair")
    opcaoBusca = int(input("Digite a opção: "))
    if opcaoBusca == 1:
        print("Relatório sendo gerado...")
        GeradorPDF(livros, "completo")
        print('Relatório gerado com sucesso!!')

    elif opcaoBusca == 2:
        catLivro = str(input("Categoria [Fisico/Digital]: ")).title().strip()
        listaTemp = []
        for i in livros:
            if i['categoria'] == catLivro:
                listaTemp.append(i)
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"

        if livroEncontrado == "sim":
            print("Relatório sendo gerado...")
            GeradorPDF(listaTemp, f"por categoria {catLivro}")
            print('Relatório gerado com sucesso!!')
        elif livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com essa categoria • ")
        listaTemp.clear()
    elif opcaoBusca == 3:
        temaLivro = str(input("Tema: ")).title().strip()
        listaTemp = []
        for i in livros:
            if i['tematica'] == temaLivro:
                listaTemp.append(i)
                livroEncontrado = "sim"
            else:
                livroNaoEncontrado = "sim"

        if livroEncontrado == "sim":
            print("Relatório sendo gerado...")
            GeradorPDF(listaTemp, f"por tema {temaLivro}")
            print('Relatório gerado com sucesso!!')
        elif livroEncontrado == "não" and livroNaoEncontrado == "sim":
            print("\n• Não foi encontrado livro com essa tematica • ")
        listaTemp.clear()
    elif opcaoBusca == 4:
        pass
    else:
        print("Opção inválida, tente novamente.")
        relatorios()

## VARIAVEIS
livros = []