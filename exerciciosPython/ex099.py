'''
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

def maior(*num):
    listaNumeros = []
    for valor in num:
        listaNumeros.append(valor)
        print(valor, end=' ')
    print(f'Foram informados {len(listaNumeros)} valores ao todo.')
    if len(listaNumeros) > 0:
        print(f'O maior número é: {max(listaNumeros)}')
    else:
        print('O maior número é: 0')
    print('-='*20)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
