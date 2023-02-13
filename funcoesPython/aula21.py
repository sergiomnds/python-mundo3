'''
Continuação falando sobre Interactive Help, docstrings,
argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados
'''
#? A função help para ensinar como usar outras funções,
#? pode ser usado diretamente no Prompt de Comando também.

help(print)
help(input)
print(input.__doc__)

#* DOCSTRINGS: Um manual como é a aquela função,
#* É possível criar para as funções criadas pelo programador. 
def contador (i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param: f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador) #* Retorna o docstring

#! PARAMENTROS OPCIONAIS
#* A função somar() quebraria se não recebecesse um dos parametros,
#* mas isso pode ser evitado, ao determinar que se o parametro n receber um valor a própria função dá um a ele.
def somar(a, b = 0, c = 0): #! Todos podem ser opcionais sem problemas. 
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar(c=3, a=2)

#! ESCOPO DE VARIAVÉIS
#* Invés de usar o escopo global, pode dar valor as variaveis separadamente.
#* Pode se ter a variavel de mesmo nome, em ambiente GLOBAL E LOCAL.
#? No exemplo está usando a variavel 'a' para isso.
def funcao():
    global n1 #! Usando o 'global' ele não cria a variavel local
    n1 = 4
    print(f'N1 dentro {n1}') #* 2
    #! print(n1) -> 4

n1 = 2
funcao()
print(f'N1 fora vale {n1}') #* 2
#! print(n1) -> 4

#! RETORNO DE VALORES - Usando o comando 'return'
#? Invés do print usar o return permite usar as funções de forma mais maleavel.
def somarComReturn(a=0, b=0, c=0):
    s = a + b + c
    return s

resp1 = somarComReturn(3, 2, 5)
resp2 = somarComReturn(2, 2)
resp3 = somarComReturn(6)

print(f'Os resultados foram: {resp1}, {resp2} e {resp3}')
