'''
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''
def escreva(texto):
    borda = '~'*(len(texto)+4)
    print(borda)
    print(f'{texto}'.center(len(borda)))
    print(borda)
    print()
    
escreva('Sérgio Mendes')
escreva('Python')
escreva('CeV')
