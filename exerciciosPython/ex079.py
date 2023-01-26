
#? Programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#? Caso o número já exista lá dentro, ele não será adicionado.
#? No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

listaNumeros = []
while True:
    resposta = str(input('Deseja adicionar um número à lista? [S/N] '))
    if resposta in 'Ss':
        numero = int(input('Digite o número:'))
        if numero in listaNumeros:
            print('Número Duplicado, não vou adicionar!')
        else:
            listaNumeros.append(numero)
    elif resposta in 'Nn':
        break
    else:
        print('Resposta Inválida')
print(f'Você adicionou os números {sorted(listaNumeros)} na lista!')
