import enum

class Opcoes(enum.Enum):
    VISUALIZAR = 1
    CADASTRAR = 2
    SAIR = 3

def menu(texto):
    print('-'*40)
    print(f'{texto:^40}')
    print('-'*40)
    print('''1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do Sistema''')
    print('-'*40)


def validarOpcao(entrada):
    while True:   
        try:
            opcao = int(input(entrada))
            try:
                Opcoes(opcao)
                break
            except:
                print('Essa opção não está listada!')
        except (ValueError, TypeError):
            print('Valor Inválido!')
    
    return opcao


def visualizar():
    print('-'*40)
    print(f'{"LISTA DE PESSOAS":^40}')
    print('-'*40)
    ver = open("pessoas.txt", "rt")
    for linha in ver:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastrar():
    while True:
        try:
            nome = str(input('Escreva o nome da pessoa: ')).upper().strip()
            try:
                idade = int(input(f'Informe a idade de {nome}: '))
                break
            except (ValueError, TypeError):
                print('Valor Inválido!')
        except (ValueError, TypeError):
            print('Nome Inválido!')

    editar = open("pessoas.txt", "a")
    editar.write(f'{nome};{idade}\n')
    editar.close()
