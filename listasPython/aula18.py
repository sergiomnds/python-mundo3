'''
    Continuando a última aula, agora trabalhando listas dentro de outras listas.
'''
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) #? Uso dos [:] para dizer que é uma cópia e não uma ligação
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
