def leiaDinheiro(texto):
    preco = str(input(texto)).strip()
    while True:
        if preco.isalpha():
            print(f'\033[0;31mERR: "{preco}" não aceito!\033[m')
            preco = str(input(texto))

        if preco == '':
            print(f'\033[0;31mERR: "{preco}" não aceito!\033[m')
            preco = str(input(texto))

        if preco.isnumeric() is True:
            break

        if ',' in preco:
            preco = preco.replace(',','.')
            if is_number(preco) is False:
                print(f'\033[0;31mERR: "{preco}" não aceito!\033[m')
                preco = str(input(texto))
            else:
                break
    return float(preco)

def is_number(string):
    '''
    Verifica se o valor é numérico,
    usado invés de isnumeric(), porque essa
    função não funciona com valores float.
    '''
    try:
        float(string)
        return True
    except ValueError:
        return False
