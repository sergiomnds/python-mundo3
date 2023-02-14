'''
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''
def notas(*nota, situacao = False):
    dictNotas = {}
    dictNotas['Qnt. de Notas'] = len(nota)
    dictNotas['Maior Nota'] = max(nota)
    dictNotas['Menor Nota'] = min(nota)
    dictNotas['Médita da Nota'] = sum(nota) / len(nota)
    if situacao:
        if dictNotas['Médita da Nota'] < 6:
            dictNotas['Situação'] = 'RUIM'
        elif 6 <= dictNotas['Médita da Nota'] < 8:
            dictNotas['Situação'] = 'RAZOÁVEL'
        else:
            dictNotas['Situação'] = 'BOA'

notas(5.5, 3, 4)