'''
Programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(Digite um n: )
'''

def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('Valor Errado')
    return valor

n = leiaInt('Digite um n: ')
print(f'Você digitou o número {n}')
