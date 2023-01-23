
#? Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#? Depois disso, mostre a listagem de números gerados
#? e também indique o menor e o maior valor que estão na tupla.

from random import randint

sorteados = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os números escolhidos foram: {sorteados}')

print(f'O maior número é: {max(sorteados)}')
print(f'O menor número é: {min(sorteados)}')

#* print(f'O maior número é: {sorted(sorteados)[-1]}')
#* print(f'O menor número é: {sorted(sorteados)[0]}')
