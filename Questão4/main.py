print('Bem vindo a Livraria do Luan Patric de Castro')
print('-' * 50)
print('-' * 20, 'Menu Principal', '-' * 20)
print('Escolha a opção desejada:')
print(' 1 - Cadastrar Livro')
print(' 2 - Consultar Livro')
print(' 3 - Remover Livro')
print(' 4 - Encerrar Programa')

lista_livros = []

def cadastrarlivro():
    global lista_livros
    quantidadelivros = int(input('Informe quantos livros quer cadastrar: '))
    for i in range(quantidadelivros):
        livro = {}
        livro['nome'] = input('Qual o nome do livro: ')
        livro['autor'] = input('Qual o autor do livro: ')
        livro['editora'] = input('Qual a editora do livro: ')
        lista_livros.append(livro)
    return lista_livros

def consultarlivro(lista_livros):
    print('Opções disponíveis:')
    print('1 - consultar todos')
    print('2 - consultar por id')
    print('3 - consultar por Autor')
    print('4 - Retornar ao Menu')
    opcaoconsulta = int(input('Escolha uma opção: '))
    if opcaoconsulta == 1:
        print('Livros cadastrados no sistema:')
        print(lista_livros)
    elif opcaoconsulta == 2:
        indice = int(input('Informe o índice do livro que deseja consultar: '))
        if indice < len(lista_livros):
            print(lista_livros[indice])
        else:
            print('Índice inválido')
    elif opcaoconsulta == 3:
        autor = input('Informe o nome do autor: ')
        livros_do_autor = [livro for livro in lista_livros if livro['autor'] == autor]
        if livros_do_autor:
            print('Livros do autor', autor + ':')
            for livro in livros_do_autor:
                print(livro)
        else:
            print('Nenhum livro encontrado para o autor', autor)
    elif opcaoconsulta == 4:
        return
    else:
        print('Opção inválida')

def removerlivro(lista_livros):
    idlivroremover = int(input('Escolha um id de livro para remover: '))
    if idlivroremover < len(lista_livros):
        del lista_livros[idlivroremover]
    else:
        print('id inválido')

opcao = int(input('Escolha uma opção: '))
while opcao != 4:
    if opcao == 1:
        lista_livros = cadastrarlivro()
    elif opcao == 2:
        consultarlivro(lista_livros)
    elif opcao == 3:
        removerlivro(lista_livros)
    else:
        print('A opção escolhida não existe.')
    opcao = int(input('Escolha uma opção: '))
print('Você decidiu encerrar o programa.')


