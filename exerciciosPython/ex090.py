'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = {}

aluno['nome'] = str(input('Qual o nome do aluno? '))
aluno['media'] = float(input(f'Qual a média de {aluno["nome"]}? '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] <= 5:
    aluno['situacao'] = 'REPROVADO'
else:
    aluno['situacao'] = 'DE RECUPERAÇÃO'

print(f'O nome do aluno é: {aluno["nome"]}')
print(f'A média de {aluno["nome"]} foi de {aluno["media"]}')
print(f'Portanto, sua situação é: {aluno["situacao"]}')
