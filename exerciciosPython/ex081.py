'''
#? Crie um programa que vai ler vários números e colocar em uma lista.
#? Depois disso, mostre:
#? A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente.
#? C) Se o valor 5 foi digitado e está ou não na lista.
'''

listaNumeros = []
numero = int(input('Digite um número: '))
listaNumeros.append(numero)
resposta = str(input('Deseja continuar? [S/N]'))
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    listaNumeros.append(numero)

    resposta = str(input('Deseja continuar? [S/N]'))

print(f'Você digitou {len(listaNumeros)} números!')
print(f'A lista é: {sorted(listaNumeros, reverse=True)}')
if 5 in listaNumeros:
    print('O número 5 está na lista!')
else:
    print('O número 5 não foi digitado')
