'''
Como usar o try except e fazer o tratamento de erros em Python.
'''

#? Quando um erro acontece e ele não é sintático, damos o nome de exceção.
#? Existe vários tipos de exceção: NameError, ValueError, etc.

#! Os comandos são:
#* try: Tentar oq tiver dentro desse bloco
#* except: Se dê erro oq fazer
#* else: Se der CERTO oq fazer
#* finally: Fazer independente
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except Exception as erro: 
#     print('Tivemos um problema!')
#     print(f'O problema foi {erro.__class__}') #? Pode ser informado o tipo de erro, além de guardar em uma variável
#     print(f'O erro encontrado foi {erro.__cause__}')
except (ValueError, TypeError):
    print('Tivemoes problema com o tipo de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir por 0')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
