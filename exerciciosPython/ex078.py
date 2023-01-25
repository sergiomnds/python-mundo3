
#? Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#? No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Os valores digitados foram: {valores}')

maiorValor = sorted(valores)[len(valores) - 1]
menorValor = sorted(valores)[0]
print(f'O maior valor digitado foi: {maiorValor} nas posições', end= ' ')
for c, v in enumerate(valores):
    if v == maiorValor:
        print(c, end=' ')

print(f'\nO menor valor digitado foi: {menorValor} nas posições', end= ' ')
for c, v in enumerate(valores):
    if v == menorValor:
        print(c, end=' ')