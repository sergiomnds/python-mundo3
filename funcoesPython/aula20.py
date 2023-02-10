'''
Aula sobre funções 'personalizadas' utilizando "def"
'''
#! Ao usar def é possível automatizar códigos repetitivos, ao criar as funções e definir
#! nelas o que será feito, utilizando parâmetros ou não.
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

titulo(' CURSO EM VÍDEO ')

#? Invés de fazer assim:
# a = 4
# b = 5
# s = a + b
# print(s)
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(4, 5)
#* Pode ao chamar a função referenciar o parametro
soma(a = 8, b = 9)
soma(b = 2, a = 1)

#? Normalmente é necessário informar mesma quantidade de parâmentros e valores
#? mas no Python é possível usar de (des)empacotamento para usar de forma variável
def contador (*num):
    for valor in num:
        print(valor, end=' ')
    print()

    tam = len(num)
    print(f'Recebi os valores {num} e foram {tam} no total.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#? Funções utilizando LISTAS
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
