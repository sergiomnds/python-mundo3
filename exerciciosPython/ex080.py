
#? Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#? já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

listaValores = []

valor = int(input('Digite um valor: '))
listaValores.append(valor)

for c in range(0, 4):
    valor = int(input('Digite um valor: '))
    if valor >= max(listaValores):
        listaValores.append(valor)
    elif valor <= min(listaValores):
        listaValores.insert(0, valor)
    else:
        for p, v in enumerate(listaValores):
            if valor >= v:
                listaValores.insert(p + 1, valor)
                break
            elif valor <= v:
                listaValores.insert(p - 1, valor)
                break

print(listaValores)
