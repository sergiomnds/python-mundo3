'''
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida')
            return 0
        except (ValueError, TypeError):
            print('Valor não aceito.')
            continue
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida')
            return 0
        except (ValueError, TypeError):
            print('Valor não aceito.')
            continue
        else:
            return num    

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número float: ')

print(f'Você digitou o nº inteiro {inteiro}')
print(f'Você digitou o nº real {real}')
