
#? Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol
#? na ordem de colocação. Depois mostre:
#? a) Os 5 primeiros times.
#? b) Os últimos 4 colocados.
#? c) Times em ordem alfabética.
#? d) Em que posição está o time da Chapecoense.

brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
    'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
    'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba',
    'Cuiabá', 'Ceará', 'Atlético-GO','Avaí', 'Juventude')

print(f'A lista dos 20 primeiros colocados:\n{brasileirao}\n')

print('Os 05 primeiros colocados são:', end='')
for c in range(0, 5):
    if c == 4:
        print(f' {brasileirao[c]} \n')
    else:
        print(f' {brasileirao[c]},', end='')

print('Os 04 últimos colocados são:', end='')
for c in range(-4, 0):
    if c == -1:
        print(f' {brasileirao[c]} \n')
    else:
        print(f' {brasileirao[c]},', end='')

print(f'Os times em ordem alfabética fica:\n{sorted(brasileirao)} \n')

if 'Chapecoense' not in brasileirao:
    print('O Chapecoense não está entre os 20 primeiros')
else:
    print(f'O Chapecoense está na {brasileirao.index("Chapecoense") + 1}º posição.')