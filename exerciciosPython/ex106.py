'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''
def manual(funcaoModulo):
    apresentacao = f'Acessando o manual do comando: {funcaoModulo}'
    borda = '~'*(len(apresentacao)+4)
    print(f'\033[0;30;44m{borda}')
    print(f'{apresentacao}'.center(len(borda)))
    print(f'{borda}\33[m')
    print(help(funcaoModulo))

titulo = 'Sistema de Ajuda PyHelp'
borda = '~'*(len(titulo)+4)
print(f'\033[0;30;41m{borda}')
print(f'{titulo}'.center(len(borda)))
print(borda)

ajuda = str(input('\033[mFunção ou Biblioteca (FIM para fechar) -> '))
while ajuda not in 'FIMfim':
    manual(ajuda)
    ajuda = str(input('\033[mFunção ou Biblioteca (FIM para fechar) -> '))
despedida = 'Até Logo!'
borda = '~'*(len(despedida)+4)
print(f'\033[0;30;41m{borda}')
print(f'{despedida}'.center(len(borda)))
print(f'{borda}\33[m')
