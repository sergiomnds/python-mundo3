''''
Adicione ao módulo moeda.py criado nos desafios anteriores,
uma função chamada resumo(),que mostre na tela algumas informações
geradas pelas funções que já temos no módulo criado até aqui.
'''
from utilidadesCeV import moeda

preco = float(input('Digite o preço: R$'))
aumento = int(input('Informe a taxa de aumento: '))
reducao = int(input('Informe a taxa de redução: '))

moeda.resumo(preco, aumento, reducao)
