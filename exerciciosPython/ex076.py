
# ? Uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# ? No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Bolacha Maria', 9.90,
            'Miojo', 4.50,
            'Salsicha', 22.35,
            'Arroz', 7.80,
            'Feijão', 9.20,
            'Cream Cracker', 1.50)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for index in enumerate(produtos):
    if index % 2 == 0:
        print(f'{produtos[index]:.<30}', end='')
    elif index % 2 == 1:
        print(f'R${produtos[index]:>5.2f}')
print('-'*40)
