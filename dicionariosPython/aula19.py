'''
    1º Aula sobre Dicionários em Python, o 3º tipo de variável complexa.
'''
pessoas = {'Nome': 'Sergio', 'Sexo': 'M', 'Idade': 20}

print(pessoas)
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')

print(pessoas.keys()) #* dict_keys(['Nome', 'Sexo', 'Idade'])
print(pessoas.values()) #* dict_values(['Sergio', 'M', 20])
print(pessoas.items()) #* dict_items([('Nome', 'Sergio'), ('Sexo', 'M'), ('Idade', 20)])

del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil) #* [{'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}, {'UF': 'São Paulo', 'Sigla': 'SP'}]
print(brasil[0]['UF']) #* Rio de Janeiro
print(brasil[1]['Sigla']) #* SP

estado = dict()
brasil2 = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil2.append(estado.copy()) #! Invés de estado[:], usa esse método interno dos dicionários
print(brasil2)

for e in brasil2:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v} ')

    for v in e.values():
        print(v, end=' ')
    print()
