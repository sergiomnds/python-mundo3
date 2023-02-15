'''
Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.
'''
from utilidadesCeV import moeda

valor = float(input('Digite o valor: '))
print(f'Aumetando 10% de R${moeda.moeda(valor)} temos R${moeda.aumentar(valor, True)}')
print(f'Diminuindo 10% de R${moeda.moeda(valor)} temos R${moeda.diminuir(valor, True)}')
print(f'A metade de R${moeda.moeda(valor)} é igual a R${moeda.metade(valor, True)}')
print(f'O dobro de R${moeda.moeda(valor)} é igual a R${moeda.dobro(valor, True)}')
