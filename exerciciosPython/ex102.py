'''
Programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(numero, show = False):
    cont = numero
    fat = 1
    if show:
        print(f'{numero}! = ', end='')
    while cont > 0:
        if show:
            print(f'{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
        fat *= cont
        cont -= 1
    print(f'{fat}')

fatorial(5, True)
fatorial(9, False)
fatorial(3, True)
