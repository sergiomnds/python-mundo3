'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[],[],[]]
somaPares = somaColuna = 0
for c in range(0,3):
    for p in range(0,3):
        numero = int(input(f'Digite o número da posição [{c}, {p}]: '))
        if numero % 2 == 0:
            somaPares += numero
        if c == 2:
            somaColuna += numero
        matriz[c].append(numero)

#* PRINT
for m in matriz:
    for c in range(0, 3):
        if c == 2:
            print(f'[ {m[c]:^5} ]')
        else:
            print(f'[ {m[c]:^5} ]', end='')

print(f'SOMA DE TODOS VALORES PARES: {somaPares}')
print(f'SOMA DOS VALORES DA TERCEIRA COLUNA: {somaColuna}')
print(f'O MAIOR VALOR DA SEGUNDA COLUNA: {max(matriz[1])}')
