'''
Como criar módulos em Python e reutilizar códigos em outros projetos.
Como agrupar módulos em pacotes, ampliando a modularização em grandes projetos.
'''
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
