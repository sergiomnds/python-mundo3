'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''
import urllib.request

url = 'http://www.pudim.com.br'
try:
    site = urllib.request.urlopen(url)
except:
   print('Não consegui acessar :(')
else:
    print('Consegui acessar!')
    
