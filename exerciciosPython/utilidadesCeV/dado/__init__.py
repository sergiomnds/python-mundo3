def leiaDinheiro(texto):
    preco = str(input(texto))
    if ',' in preco:
        return preco.replace(',','.')