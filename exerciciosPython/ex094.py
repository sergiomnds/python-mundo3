'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
listaPessoas = []
pessoa = {}
totalIdade = 0
mulheres = []
listaAcimaMedia = []
while True:
    pessoa['Nome'] = str(input('Nome da Pessoa: ')).upper()
    pessoa['Sexo'] = str(input('Sexo (M ou F): ')).upper()[0]
    pessoa['Idade'] = int(input(f'Idade de {pessoa["Nome"]}: '))
    totalIdade += pessoa['Idade']
    listaPessoas.append(pessoa.copy())
    
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])

    resposta = str(input('Deseja continuar? [S/N]: '))
    if resposta in 'Nn':
        break

media = totalIdade / len(listaPessoas)

print('='*20)
print(f'Qnt. de pessoas cadastradas: {len(listaPessoas)}')
print(f'Média de Idade: {media}')
print('As mulheres são: ',end='')
for k, m in enumerate(mulheres):
    if k == (len(mulheres)) - 1:
        print(m)
    else:
        print(m, end=', ')
print('As pessoas que estão acima da média são: ')
for p in listaPessoas:
    if p['Idade'] > media:
        print(f'{p["Nome"]} com {p["Idade"]} anos')
   