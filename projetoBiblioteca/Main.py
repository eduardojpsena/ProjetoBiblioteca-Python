import json
import os.path
import Biblioteca

# Grupo:    Eduardo José Pereira de Sena
#           André Luis Moreira da Silva Santos

def main():

    ##lOGIN DO SISTEMA - id = admin / senha = 1234
    print("• Morais Lybrary •")
    statusLogin = Biblioteca.loginSistema()

    while True:
        if statusLogin == True:
            print("• Login efetuado com sucesso •")
            break
        else:
            print("• Id ou senha inválido, tente novamente •")
            statusLogin = Biblioteca.loginSistema()
    Biblioteca.importarLivros()  # Pedido de import no inicio para manter o sistema atualizado
    opcaoMenu = Biblioteca.menu()  # Menu de opções
    while opcaoMenu != 10:

        if opcaoMenu == 1:  # Cadastro de livros
            print("• CADASTRO DE LIVROS •\n")
            Biblioteca.livros.append(Biblioteca.cadastrodenovoslivros())

            export = str(input("Deseja exportar os dados do livro cadastrados "
                               "para o arquivo 'livros.json'? [S/N]: "))[0].strip().upper()
            if export == "S":
                with open('livros.json', 'w', encoding='utf-8') as json_file:
                    json.dump(Biblioteca.livros, json_file, indent=1, ensure_ascii=False)
                opcaoMenu = Biblioteca.menu()
            elif export == "N":
                opc = str(input("Deseja exportar os dados para outro arquivo? [S/N]: "))[0].strip().upper()
                if opc == "S":
                    arq = str(input("Qual o nome do arquivo json a ser salvo? siga o padrão "
                                    "[nomeArquivo.json]: "))
                    with open(arq, 'w', encoding='utf-8') as json_file:
                        json.dump(Biblioteca.livros, json_file, indent=1, ensure_ascii=False)
                    opcaoMenu = Biblioteca.menu()
                else:
                    opcaoMenu = Biblioteca.menu()
            else:
                print("Opção inválida")
                opcaoMenu = 1

        elif opcaoMenu == 2:  # Atualizar quantidade de um determinado titulo
            print("• ATUALIZAÇÃO DE QUANTIDADE •\n")
            Biblioteca.atualizarQuantidade()

            opcaoMenu = Biblioteca.menu()

        elif opcaoMenu == 3:  # Remover determinado titulo
            print("• REMOÇÃO DE TITULOS •\n")
            Biblioteca.removerLivros()
            export = str(input("Deseja exportar os dados do livro cadastrados "
                               "para o arquivo 'livros.json'? [S/N]: "))[0].strip().upper()
            if export == "S":
                with open('livros.json', 'w', encoding='utf-8') as json_file:
                    json.dump(Biblioteca.livros, json_file, indent=1, ensure_ascii=False)
                opcaoMenu = Biblioteca.menu()
            elif export == "N":
                opc = str(input("Deseja exportar os dados para outro arquivo? [S/N]: "))[0].strip().upper()
                if opc == "S":
                    arq = str(input("Qual o nome do arquivo json a ser salvo? siga o padrão "
                                    "[nomeArquivo.json]: "))
                    with open(arq, 'w', encoding='utf-8') as json_file:
                        json.dump(Biblioteca.livros, json_file, indent=1, ensure_ascii=False)
                    opcaoMenu = Biblioteca.menu()
                else:
                    opcaoMenu = Biblioteca.menu()

        elif opcaoMenu == 4:  # Buscar livros por titulo, ano, categoria[fisico/digital] ou temática
            print("• BUSCA DE EXEMPLARES •")
            Biblioteca.buscarLivros()

            opcaoMenu = Biblioteca.menu()

        elif opcaoMenu == 5:  # Importar dados
            print("• IMPORTANDO DADOS •")
            Biblioteca.livros.append(Biblioteca.importarLivros())
            Biblioteca.livros.pop(len(Biblioteca.livros)-1)

            opcaoMenu = Biblioteca.menu()

        elif opcaoMenu == 6:  # Obter Status dos livro [alugado/disponivel]
            print("• STATUS DO LIVRO •")
            Biblioteca.statusLivro()

            opcaoMenu = Biblioteca.menu()

        elif opcaoMenu == 7:  # Gerar relatórios do acervo completo, por categoria ou por temática
            print("• GERADOR DE RELATORIOS •")
            Biblioteca.relatorios()

            opcaoMenu = Biblioteca.menu()

        elif opcaoMenu == 8:  # Sair do sistema
            break
        else:
            print("Entrada invalida tente novamente !!!")
            opcaoMenu = Biblioteca.menu()
main()


