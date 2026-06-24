import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False}, 
                {'nome': 'Hamburguer', 'categoria': 'Americana', 'ativo': False}, 
                {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False}]

def nome_do_programa():
    print('Sabor expresso\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def cadastrar_restaurante():
    subtitulo('Cadastrar restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    if nome_restaurante in [restaurante['nome'] for restaurante in restaurantes]:
        print(f'\nRestaurante {nome_restaurante} já está cadastrado!\n')
        voltar_menu()
    elif not nome_restaurante or not categoria:
        print('\nNome e categoria são obrigatórios!\n')
        voltar_menu()
    else:
        restaurantes.append({'nome': nome_restaurante, 'categoria': categoria, 'ativo': False})
        print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!')
        voltar_menu()

def listar_restaurantes():
    subtitulo('Restaurantes cadastrados')
    if not restaurantes:
        print('Nenhum restaurante cadastrado.\n')
    else:
        print(f'{"Nome do Restaurante".ljust(23)} | {"Categoria".ljust(20)} | Status')
        print('-' * 60)
        for i, restaurante in enumerate(restaurantes):
            nome_restaurantes = restaurante['nome']
            categorias_restaurantes = restaurante['categoria']
            ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
            print(f'{i+1}. {nome_restaurantes.ljust(20)} | {categorias_restaurantes.ljust(20)} | {ativo}')
    voltar_menu()

def alterar_status_restaurante():
    subtitulo('Alterar status do restaurante')
    if not restaurantes:
        print('Nenhum restaurante cadastrado.\n')
        voltar_menu()
    else:
        nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
        restaurante_encontrado = False

        for restaurante in restaurantes:
            if restaurante['nome'] == nome_restaurante:
                restaurante['ativo'] = not restaurante['ativo']
                ativo = "Ativado" if restaurante['ativo'] else "Desativado"
                print(f'\nRestaurante {nome_restaurante} agora está {ativo}!')
                restaurante_encontrado = True
        if not restaurante_encontrado:
            print(f'\nRestaurante {nome_restaurante} não encontrado!')
    voltar_menu()

def voltar_menu():
    input('\nPressione qualquer tecla para continuar...')
    main()

def finalizar_programa():
    subtitulo('Encerrando o programa')

def subtitulo(texto):
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    subtitulo('Opção inválida')
    voltar_menu()

def escolher_opcao():
    try:
        opcao = int(input('Digite a opção desejada: '))

        match opcao:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_status_restaurante()
            case 4:
                finalizar_programa()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
