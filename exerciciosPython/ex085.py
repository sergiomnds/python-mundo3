'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''
paresImpar = [[],[]]

while True:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        paresImpar[0].append(numero)
    elif numero % 2 != 0:
        paresImpar[1].append(numero)

    resposta = str(input('Deseja continuar? [S/N] ')).upper()
    if resposta == 'N':
        break

print(f'Lista dos números pares: {sorted(paresImpar[0])}')
print(f'Lista dos números ímpares: {sorted(paresImpar[1])}')
