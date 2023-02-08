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
while True:
    pessoa['Nome'] = str(input('Nome da Pessoa: '))
    pessoa['Sexo'] = str(input('Sexo (M ou F): '))
    pessoa['Idade'] = int(input(f'Idade de {pessoa["Nome"]}: '))
    totalIdade += pessoa['Idade']
    listaPessoas.append(pessoa.copy())
    
    resposta = str(input('Deseja continuar? [S/N]: '))
    if resposta in 'Nn':
        break

media = totalIdade / len(listaPessoas)
   
print(f'Qnt. de pessoas cadastradas: {len(listaPessoas)}')
print(f'Média de Idade: {media}')
