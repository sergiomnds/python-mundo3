'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
'''
from utilidadesCeV import moeda

valor = float(input('Digite o valor: '))
print(f'Aumetando 10% de R${moeda.moeda(valor)} temos R${moeda.moeda(moeda.aumentar(valor))}')
print(f'Diminuindo 10% de R${moeda.moeda(valor)} temos R${moeda.moeda(moeda.diminuir(valor))}')
print(f'A metade de R${moeda.moeda(valor)} é igual a R${moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de R${moeda.moeda(valor)} é igual a R${moeda.moeda(moeda.dobro(valor))}')
