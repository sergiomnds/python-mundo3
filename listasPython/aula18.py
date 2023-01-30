'''
    Continuando a última aula, agora trabalhando listas dentro de outras listas.
'''
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) #? Uso dos [:] para dizer que é uma cópia e não uma ligação
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [['João', 19], ['Ana', 35], ['Joaquim', 13], ['Maria', 45]]
print(galera2[2][1]) #* 13

for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade')

pessoas = list()
dado = list()
maiorIdade = menorIdade = 0
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maiorIdade += 1
    else:
        print(f'{p[0]} é menor de idade')
        menorIdade += 1

print(f'Temos {maiorIdade} maiores e {menorIdade} menores de Idade.')
