def aumentar(preco):
    valorAumentado = preco + (preco*0.1)
    return valorAumentado

def diminuir(preco):
    valorDiminuido = preco - (preco*0.1)
    return valorDiminuido
    
def dobro(preco):
    valorDobrado = preco * 2
    return valorDobrado
    
def metade(preco):
    valorMetade = preco / 2
    return valorMetade

def moeda(valor):
    formatado = round(valor, 2)
    return f'{formatado:.2f}'.replace('.',',')
