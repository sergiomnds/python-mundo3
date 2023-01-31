'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep

jogos = []
jogo = []
qntJogos = int(input('Quantos jogos serão criados? '))

for c in range(0, qntJogos):
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogos.append(jogo[:])
    jogo.clear()

for n, j in enumerate(jogos):
    print(f'{n+1}º JOGO: {sorted(j)}')
    sleep(1)
