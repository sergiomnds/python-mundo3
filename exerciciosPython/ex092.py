'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime

pessoa = {}
anoAtual = 2023

pessoa['Nome'] = str(input('Informe o nome: '))

anoNascimento = int(input('Informe o ano de nascimento: '))
idade = datetime.now().year - anoNascimento
pessoa['Idade'] = idade

pessoa['CTPS'] = int(input('Informe o nº da Carteira de Trabalho (0 se não tiver): '))

if pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(input('Informe o ano de contratação: '))
    pessoa['Salário'] = float(input('Informe o salário: '))
    idadeAposentar = idade + ((pessoa['Ano de Contratação'] + 35) - datetime.now().year)
    pessoa['Idade de Aposentadoria'] = idadeAposentar

for k, v in pessoa.items():
    print(f'{k}: {v}')
