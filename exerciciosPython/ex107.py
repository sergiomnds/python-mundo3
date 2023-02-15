import moeda

valor = float(input('Digite o valor: '))
print(f'Aumetando 10% de R${valor} temos R${moeda.aumentar(valor)}')
print(f'Diminuindo 10% de R${valor} temos R${moeda.diminuir(valor)}')
print(f'A metade de R${valor} é igual a R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é igual a R${moeda.dobro(valor)}')
