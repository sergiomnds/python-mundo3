
#? Programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#? Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
    'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
    'dezoito', 'dezenove', 'vinte')

while True:
    numeroUsuario = int(input('Informe um número entre 0 e 20: '))
    if 0 <= numeroUsuario <= 20:
        print(f'Você digitou o nº {numeros[numeroUsuario]}!')
    else:
        print(f'O número {numeroUsuario} não está entre 0 e 20.')