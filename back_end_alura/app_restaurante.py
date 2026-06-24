import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False}, 
                {'nome': 'Hamburguer', 'categoria': 'Americana', 'ativo': False}, 
                {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False}]

def nome_do_programa():
    print('Sabor expresso\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def cadastrar_restaurante():
    subtitulo('Cadastrar restaurante')
    nome = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    if nome in [restaurante['nome'] for restaurante in restaurantes]:
        print(f'\nRestaurante {nome} já está cadastrado!\n')
        reset()
    elif not nome or not categoria:
        print('\nNome e categoria são obrigatórios!\n')
        reset()
    else:
        restaurantes.append({'nome': nome, 'categoria': categoria, 'ativo': False})
        print(f'\nRestaurante {nome} cadastrado com sucesso!')
        reset()

def listar_restaurantes():
    subtitulo('Restaurantes cadastrados')
    if not restaurantes:
        print('Nenhum restaurante cadastrado.\n')
    else:
        for i, restaurante in enumerate(restaurantes):
            nome_restaurantes = restaurante['nome']
            categorias_restaurantes = restaurante['categoria']
            ativo = restaurante['ativo']
            print(f'{i+1}. {nome_restaurantes} - {categorias_restaurantes} - {"Ativo" if ativo else "Inativo"}')
    reset()

def reset():
    input('\nPressione qualquer tecla para continuar...')
    main()

def finalizar_programa():
    subtitulo('Encerrando o programa')

def subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def opcao_invalida():
    subtitulo('Opção inválida')
    reset()

def escolher_opcao():
    try:
        opcao = int(input('Digite a opção desejada: '))

        match opcao:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
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
