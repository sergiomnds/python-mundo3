
#? Ex 107
def aumentar(preco, taxa = 10, formatacao = False):
    valorAumentado = preco + (preco*(taxa)/100)
    if formatacao: #? Ex 109
        return moeda(valorAumentado)
    else:
        return valorAumentado

#? Ex 107
def diminuir(preco, taxa = 10, formatacao = False):
    valorDiminuido = preco - (preco*(taxa)/100)
    if formatacao: #? Ex 109
        return moeda(valorDiminuido)
    else:
        return valorDiminuido

#? Ex 107  
def dobro(preco, formatacao = False):
    valorDobrado = preco * 2
    if formatacao: #? Ex 109
        return moeda(valorDobrado)
    else:
        return valorDobrado

#? Ex 107
def metade(preco, formatacao = False):
    valorMetade = preco / 2
    if formatacao: #? Ex 109
        return moeda(valorMetade)
    else:
        return valorMetade

#? Ex 108
def moeda(valor): #? Ex 109
    formatado = round(valor, 2)
    return f'{formatado:.2f}'.replace('.',',')

#? Ex 110
def resumo(valor, taxaAumento, taxaDiminuir):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \tR${moeda(valor)}')
    print(f'Dobro do preço: \tR${dobro(valor, True)}')
    print(f'Metade do preço: \tR${dobro(valor, True)}')
    print(f'{taxaAumento}% de aumento: \tR${aumentar(valor, taxaAumento, True)}')
    if taxaDiminuir < 10:
        print(f'{taxaDiminuir}% de redução: \t\tR${diminuir(valor, taxaDiminuir, True)}')
    elif 10 <= taxaDiminuir:
        print(f'{taxaDiminuir}% de redução: \tR${diminuir(valor, taxaDiminuir, True)}')
    print('-'*30)
