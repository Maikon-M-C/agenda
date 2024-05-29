AGENDA = {
    'meu nome' : {
        'nome': 'meu nome',
        'telefone': '9889988998',
        'email': '@gmail.com',
        'endereco': 'Av, lacerda'
    },
    'meu nome2' : {
        'nome': 'meu nome',
        'telefone': 'sdfgsdfg',
        'email': '@gmail.com',
        'endereco': 'Av, lacerda'
    }
}

ERROS = {
    'ContatoInexistente': {
        'error': (KeyError, TypeError),
        'resposta': 'Contato Inexistente.'
    },
    'ContatoExistente': {
        'error': KeyError,
        'resposta': 'Contato já esta na Agenda.'
    },
    'OpcaoInvalida': {
        'error': KeyError,
        'resposta': 'Opçao invalida!'        
    }
}

passagem = '='*20


def tratamento(error=Exception, resposta='Ocorreu algun erro inesperado'):
    def decorador(func):
        def closure(*args, **kwargs):

            try:
                func(*args, **kwargs)
                
            except error:
                print(passagem)
                print(resposta)
                print(passagem)

            except Exception as er:   
                print(passagem)
                print(f'{resposta}: {er}')
                print(passagem)
                  
        return closure
    return decorador


def get_error(erro):
    return ERROS.get(erro)


def exportar_contatos(arquivo):
    with open('agenda.txt', mode='a', encoding='utf-8') as file:
        file.writelines(AGENDA.values()+'\n')



def criar_contato():
    contato = {
        'nome': input('Nome: '),
        'telefone': input('telefone: '),
        'email': input('email: '),
        'endereco': input('endereço: ')
    }

    adicionar_contato(contato)


@tratamento(**(get_error('ContatoInexistente')))
def editar_contato():
    editando = input('Qual contato você deseja editar: ')
    editando = AGENDA.get(editando)

    novo_contato = {
        'nome': input(f'Nome({editando['nome']}): '),
        'telefone': input(f'telefone({editando['telefone']}): '),
        'email': input(f'email({editando['email']}): '),
        'endereco': input(f'endereço({editando['endereco']}): ')
    }

    for info in novo_contato.keys():
        if novo_contato[info] == '':
            novo_contato[info] = editando[info]

    editando.update(novo_contato)


@tratamento(**(get_error('ContatoExistente')))
def adicionar_contato(contato):

    AGENDA[contato['nome']] = {
        'nome': contato['nome'],
        'telefone': contato['telefone'],
        'email': contato['email'],
        'endereco': contato['endereco']
    }

    formatar_contato(contato)
    print(f'>>>>> {contato['nome']} atualizado na sua lista de contatos <<<<<')


def formatar_contato(contato):
    print(passagem)
    print('Nome: ', contato['nome'])
    print('Telefone: ', contato['telefone'])
    print('Email: ', contato['email'])
    print('Endereço: ', contato['endereco'])
    print(passagem+'\n')


def mostrar_todos_contatos():
    for contato in AGENDA.values():
        formatar_contato(contato)


@tratamento(**(get_error('ContatoInexistente')))
def buscar_contato():
    contato = input('Qual contato voce deseja ver: ')
    formatar_contato(AGENDA[contato])


@tratamento(**(get_error('ContatoInexistente')))
def remover_contato():
    contato = input('Digite o nome do contato a ser deletado: ')
    AGENDA.pop(contato)
    print(f'>>>>> {contato} atualizado na sua lista de contatos <<<<<')
    print(passagem)


def imprimir_menu():
    print('escolha uma opção')
    print('1 -> Mostrar todos os contatos')
    print('2 -> Buscar contato')
    print('3 -> Incluir contato')
    print('4 -> Editar contato')
    print('5 -> Remover contato')

    print('0 -> salvar e sair da Agenda')


def kill_program():
    exit()


def opcoes_menu(opcao):
    opcoes = {
        '1': mostrar_todos_contatos,
        '2': buscar_contato,
        '3': criar_contato,
        '4': editar_contato,
        '5': remover_contato,
        '0': kill_program
    }

    return opcoes[opcao]()


@tratamento(**(get_error('OpcaoInvalida')))
def main():
    imprimir_menu()

    opcao = input('digite uma opção: ')

    opcoes_menu(opcao)
    
    main()


main()