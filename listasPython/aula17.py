
# #? A principal diferença entre as tuplas e listas é que as listas MUTAVEIS.
# #* Para ter uma lista no Python, coloca os dados em [ ], invés de ( ) como na tupla.
# alimentos = ['hamburguer','suco','pizza','pudim']
# alimentos[3] = 'picole'

# print(alimentos) #* ['hamburguer', 'suco', 'pizza', 'picole']

# #! Para adicionar dados que ultrapassam o tamanho original da lista usa o comando 'append()'
# alimentos.append('cookie') #* Assim 'cookie' foi adicionado a ultima posição [4].

# #! Caso queira escolher, onde o novo dado será alocado usa 'insert()'.
# alimentos.insert(0, 'cachorro quente') #* Esse comando empurra os outros dados para as outras posições, não substitue nenhum.

# #? Existem 3 maneiras diferentes para excluir um dado de uma lista:
# del alimentos[3] #* Comando del, informando o índice do dado na lista.
# alimentos.pop(3) #* Comando pop(), pode ser usada para excluir informando o índice.
#                 #*Porém, é mais comum para excluir o último item da lista sem precisar informar nada.
# alimentos.remove('pizza') #* Remove o dado, mas aqui ele é informado pelo seu valor.

# #! Ao remover um dado, os índices são refeitos automaticamente.
# #! [4] Picolé vai para [3]

# #? Pode criar uma lista com o método list()
# valores = list(range(4,11)) #*Cria uma lista [4,5,6,7,8,9,10] com os índices de 0 a 6.

# #* Outros comandos já conhecidos, também se aplicam as listas.
# numeros = [8, 2, 5, 4, 9, 3, 0]
# numeros.sort()
# numeros.sort(reverse=True)
# len(numeros)

#?EXEMPLOS DA AULA
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop() #num.pop(2)
num.remove(2) #* Primeiro aparição do dado - 2
if 4 in num:
    num.remove(4)
else:
    print('Não foi encontrado o nº 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

# valores2 = []
# valores2.append(5)
# valores2.append(9)
# valores2.append(4)
valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores2):
    # print(f'{v}...', end='')
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7,]
c = a[:] #* Cópia dos valores da lista a.
b = a #* Uma LIGAÇÃO e não uma CÓPIA.
b[2] = 8 #!AO IGUALAR LISTAS, ELAS FICAM LIGADAS. A MUDANÇA EM UMA TAMBÉM SERÁ APLICADA NA OUTRA!
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')