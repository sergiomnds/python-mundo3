'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

jogador = {}
jogador['Nome do Jogador'] = str(input('Nome do Jogador: ')).upper()
jogador['Nº de Partidas'] = int(input(f'Qnt. de Partidas de {jogador["Nome do Jogador"]}: '))

gols = []
totalGols = 0
for c in range(0, jogador['Nº de Partidas']):
    gol = int(input(f'Quantos gols foi feito na {c+1}º partida ? '))
    gols.append(gol)
jogador['Gols por Partida'] = gols
jogador['Total de Gols feitos no Campeonato'] = sum(gols)

print('='*30)
for k, v in jogador.items():
    print(f'{k}: {v}')

print('='*30)
print(f'O jogador {jogador["Nome do Jogador"]} jogou {jogador["Nº de Partidas"]} partidas')
for c, v in enumerate(gols):
    print(f'Na {c+1}º partida fez {v} gols')
print(f'No total foram {jogador["Total de Gols feitos no Campeonato"]} gols no campeonato')
