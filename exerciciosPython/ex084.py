'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

dados = []
pessoas = []
print('REGISTRO DE PESOS')
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    
    pessoas.append(dados[:])
    dados.clear()

    resposta = str(input('Deseja continuar? [S/N]')).upper()
    if resposta == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'O maior peso registrado foi de {maior} KG. As pessoas mais pesadas são:',end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso registrado foi de {menor} KG. As pessoas mais leves são:',end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
