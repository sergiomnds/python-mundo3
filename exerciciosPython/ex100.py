'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint

def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
        c += 1
    print(f'A lista de números foi {lista}')

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Soma dos nºs pars: {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)
