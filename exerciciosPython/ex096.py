'''
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
'''
def area(larg, comp):
    print(f'O terreno possui {larg*comp} metros quadrados')
    
largura = int(input('Qual a largura do terreno? '))
comprimento = int(input('Qual o comprimento do terreno? '))

area(largura, comprimento)
