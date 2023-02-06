'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from operator import itemgetter
from random import randint
from time import sleep
sorte = {
        'Jogador 01': randint(1, 6),
        'Jogador 02': randint(1, 6),
        'Jogador 03': randint(1, 6),
        'Jogador 04': randint(1, 6)
        }
print('Os números sorteados foram: ')
for k, v in sorte.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
    
ranking = sorted(sorte.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
