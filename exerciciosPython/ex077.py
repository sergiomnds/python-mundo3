
#? Programa que tenha uma tupla com várias palavras (não usar acentos).
#? Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

listaPalavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
    'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR')

for c in listaPalavras:
    print(f'\n{c} tem as vogais: ', end='')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')