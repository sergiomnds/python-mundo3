'''
    Programa onde o usuário digite uma expressão qualquer que use parênteses.
    Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
parentEsquerda = parentDireita = 0

expressao = str(input('Digite a expressão para ser verificada: '))
parenteses = []
for v in expressao:
    if v =='(':
        parenteses.append(v)
    elif v == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(v)
            break

if len(parenteses) == 0:
    print('Os parênteses estão fechados!')
else:
    print('Há parênteses em aberto!')