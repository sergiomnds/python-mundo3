'''
Programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicandose uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    if idade < 18:
        return 'NEGADO'
    # elif 18 <= idade < 70:
        