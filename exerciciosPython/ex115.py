'''
Criar um menu em Python, usando modularização. Fazer acesso a arquivos usando o Python.
'''
from lib.cadastro import *

while True:
    menu('MENU PRINCIPAL')
    
    opcao = validarOpcao('Sua Opção: ')

    if Opcoes(opcao) == Opcoes.VISUALIZAR:
        visualizar()
        
    elif Opcoes(opcao) == Opcoes.CADASTRAR:
        print('-'*40)
        cadastrar()
    
    elif Opcoes(opcao) == Opcoes.SAIR:
        print('Saindo! Volte Sempre!')
        break
    