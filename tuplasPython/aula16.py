
#? Trabalhando a 1º das 3 maneiras de usar variáveis compostas em Python - Tuplas. Onde uma variável
#? vai guardar mais de um elemento em seu espaço de memória.

#? Os elementos são indicados pelos indícies [0], [1], etc.
#? O nome é exemplo de uma tupla, já que pode acessar os indíces.
#? Ex.: 'Sergio' -> [0] 'S', [1] 'e', [2] 'r', [3] 'g', [4] 'i', [5] 'o'

#! IMPORTANTE: As tuplas são IMUTÁVEIS!!!
#! Não é possível mudar-las depois de já atribuído os valores.
lanche = 'hamburguer','suco','pizza','pudim' #* Pode ser colocado entre parenteses () ou não.

print(lanche[0]) #* Saída: hamburguer
print(lanche[0:2]) #* ('hamburguer', 'suco')
print(lanche[1:]) #* ('suco','pizza','pudim')
print(lanche[-1]) #* ('pudim')
#! [-2] seria pizza, [-3] seria suco, e por aí vai. É a lista inversa!

print(len(lanche)) #* 4 -> len de lenght

#? Vai printar todas as comidas dentro da variavel composta.
for comida in lanche: #* usando loop com variavel composta.
    print(f'Eu vou comer {comida}')

#? Exemplo de for usando lenght:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
#*Ambos for's tem o mesmo resultado. Mas são estruturados de maneiras diferentes,
#*Cada um tem seu objetivo,  mas o segundo é mais completo.

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

#? Função sorted:
print(sorted(lanche)) #*Saída: ['hamburguer', 'pizza', 'pudim', 'suco']

#?Outras maneiras de usar a tupla:

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c) #* (2, 5, 4, 5, 8, 1, 2)
print(d) #* (5, 8, 1, 2, 2, 5, 4)
#! Prints diferentes, pois as tuplas não somam apenas juntam.

print(c.count(5)) #* 2 -> O '5' aparece 2 vezes
print(c.index(8)) #* 1 -> Mostra a posição da primeira ocorrência do elemento
print(c.index(5, 1)) #* 5 -> Começa a partir da posição 1, e mostra a posição da primeira ocorrência do elemento.

#? Tuplas podem guardar vários tipos diferentes dentro dela.
pessoa = ('Gustavo', 39, 'M', 99.88)

del(pessoa) #!Função para apagar a tupla, ou outras coisas em Python.
#* O comando del(pessoa[0]) NÃO RODA, já que tuplas são imutáveis.