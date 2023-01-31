'''
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [[],[],[]]

for c in range(0,3):
    for p in range(0,3):
        numero = int(input(f'Digite o número da posição [{c}, {p}]: '))
        matriz[c].append(numero)

for m in matriz:
    for c in range(0, 3):
        if c == 2:
            print(f'[ {m[c]:^5} ]')
        else:
            print(f'[ {m[c]:^5} ]', end='')