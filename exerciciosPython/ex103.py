'''
Programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
    
jogador = str(input('Nome do Jogador: ')).upper()
qntGols = str(input('Qnt. de Gols: '))

if qntGols.isnumeric():
    qntGols = int(qntGols)
else:
    qntGols = 0

if jogador.strip() == '':
    ficha(gols=qntGols)
else:
    ficha(jogador, qntGols)
