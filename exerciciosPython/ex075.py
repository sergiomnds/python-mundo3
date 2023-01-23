
#? Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#? A) Quantas vezes apareceu o valor 9.
#? B) Em que posição foi digitado o primeiro valor 3.
#? C) Quais foram os números pares.

valores = (int(input('Digite o 1º Valor: ')), int(input('Digite o 2º Valor: ')),
    int(input('Digite o 3º Valor: ')), int(input('Digite o 4º Valor: ')))

print(f'Os valores digitados foram: {valores}')

print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 está na {valores.index(3) + 1}º posição')
else:
    print('O número 3 não está entre os valores digitados.')

print('Os números pares são:')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ') 