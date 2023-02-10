'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

listaJogadores = []
while True:
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
    
    listaJogadores.append(jogador.copy())
    resposta = str(input('Deseja continuar? [S/N]')).upper()[0]
    if resposta == 'N':
        break

print('='*30)
print('Código - Nome - Gols - Total')
print('-'*20)
for j in listaJogadores:
    print(listaJogadores.index(j), end=' ')
    for v in j.values():
        if v == j['Total de Gols feitos no Campeonato']:
            print(v)
        else:
            print(v, end= ' ')
print('-'*20)

codigo = 0
while True:
    codigo = int(input('Mostrar dados de qual jogador? (999 para PARAR)'))
    if codigo == 999:
        print('FINALIZADO')
        break
    else:
        print(f'LEVANTAMENTO DO JOGADOR {listaJogadores[codigo]["Nome do Jogador"]}')
        for c, v in enumerate(listaJogadores[codigo]["Gols por Partida"]):
            print(f'Na {c+1}º partida fez {v} gols')
        print('-'*20)
