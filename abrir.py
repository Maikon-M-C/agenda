AGENDA = {
    'meu nome' : {
        'nome': 'meu nome',
        'telefone': '9889988998',
        'email': '@gmail.com',
        'endereco': 'Av lacerda'
    },
    'meu nome2' : {
        'nome': 'meu ds',
        'telefone': 'dsfas',
        'email': '@gmail.com',
        'endereco': 'Av lacerda'
    }
}

HEADER = 'nome,telefone,email,endereço\n'

def exportar_contatos(arquivo):
    with open(f'{arquivo}.csv', mode='a', encoding='utf-8') as file:
        file.write(HEADER)
        for info in AGENDA:
            file.write(f'{AGENDA[info]['nome']},{AGENDA[info]['telefone']},{AGENDA[info]['email']},{AGENDA[info]['endereco']} \n')

exportar_contatos(347809)