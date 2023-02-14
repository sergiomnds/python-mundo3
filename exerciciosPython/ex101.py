'''
Programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18:
        return 'OPCIONAL'
    elif 18 <= idade < 70:
        return 'OBRIGATÓRIO'
    elif idade > 70:
        return 'OPCIONAL'
    
anoNascimento = int(input('Informe o ano de nascimento: '))
situacao = voto(anoNascimento)

print(f'O vontade tem {datetime.now().year - anoNascimento} anos e seu voto é {situacao}')
