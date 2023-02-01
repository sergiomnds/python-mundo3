'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
'''
alunos = []
aluno = []
notas = []

while True:
    nomeAluno = str(input('Nome do aluno: ')).upper()
    aluno.append(nomeAluno)
    for c in range(0, 2):
        nota = float(input(f'A {c + 1}º NOTA:'))
        notas.append(nota)
    aluno.append(notas[:])
    alunos.append(aluno[:])
    
    resposta = str(input('Deseja Continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
    else:
        aluno.clear()
        notas.clear()

while True:
    soma = 0
    for c, a in enumerate(alunos):
        print(f'{c + 1}º Aluno(a) {a[0]} teve a MÉDIA: ',end='')
        for m in range(0, 2):
            soma += a[1][m]
        media = soma / 2
        soma = 0
        print(media)

    verNotas = str(input('\nDeseja ver as notas de algum aluno? [S/N] ')).upper()
    if verNotas == 'S':
        numeroAluno = int(input('Qual Aluno? (NÚMERO DO ALUNO NA LISTA) '))
        print(f'\nAs notas de {alunos[numeroAluno - 1][0]} foram {alunos[numeroAluno - 1][1]}')
        print()
    elif verNotas == 'N':
        break
