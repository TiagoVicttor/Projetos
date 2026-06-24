import os

restaurantes = ['Pizza','hamburguer']

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
    if nome in restaurantes:
        print(f'\nRestaurante {nome} já está cadastrado!\n')
        reset()
    else:
        restaurantes.append(nome)
        print(f'\nRestaurante {nome} cadastrado com sucesso!\n')
        reset()

def listar_restaurantes():
    subtitulo('Restaurantes cadastrados')
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado.')
    else:
        for i, restaurante in enumerate(restaurantes):
            print(f'{i + 1}. {restaurante}')
    print('')
    reset()

def reset():
    input('Pressione qualquer tecla para continuar...')
    main()

def finalizar_programa():
    subtitulo('Encerrando o programa')

def subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def opcao_invalida():
    subtitulo('Opção inválida\n')

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
