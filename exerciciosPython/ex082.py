'''
    Programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas
    os valores pares e os valores ímpares digitados,respectivamente.
    Ao final, mostre o conteúdo das três listas geradas.
'''

todosNumeros = []
apenasPares = []
apenasImpares = []

resposta = 'S'
while True:
    if resposta in 'Ss':
        numero = int(input('Digite um número: '))
        todosNumeros.append(numero)
        if numero % 2 == 0:
            apenasPares.append(numero)
        elif numero % 2 != 0:
            apenasImpares.append(numero)
        resposta = str(input('Deseja continuar? [S/N]')).upper()
    elif resposta in 'Nn':
        break
    else:
        print('Resposta Inválida')
        resposta = str(input('Deseja continuar? [S/N]')).upper()

print(f'A lista com todos os números: {todosNumeros}')
print(f'A lista só com números PARES: {apenasPares}')
print(f'A lista só com números ÍMPARES: {apenasImpares}')
