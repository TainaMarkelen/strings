# convertendo para letras maiúsculas
time = "Íbis Au"
print (time.upper())

# convertendo para letras minúsculas
print (time.lower())

# colocando apenas a primeira letra em maiúscula
print ('anna gosta de banana'.capitalize())
print ('BRASIL' .capitalize())

# removendo espaços em branco no início ou no final da string
print(   'tainamarkelen@gmail.com' .strip())

# contagem de objetos dentro da string
print("anna gosta de banana".count("a"))

# substituindo ojetos string
print("eu torço para o sao paulo".replace("sao paulo", "corinthians"))

# centralizando strings
print('anna gosta de banana'.capitalize().center(80)) # o 80 é a quantidade de caracteres antes da string

'''As funções podem ser chamadas uma atrás da outra'''

# achar coisa dentro da string, devolverá a posição
texto = "Minha terra tem palmeiras onde canta o sabiá"
print(texto.find('m'))
print(texto.find('sa'))
print(texto.find('bom')) # devolverá -1, que indica que essa sílada não se encontra no texto

# comprimento da string
print(len("taina"))

# pegando pedaços da string
fruta = 'amora'
print(fruta[:4]) # printará tudo até a posição 4, sem incluir a posição 4
print(fruta[1:]) # da posição 1 até o final
print(fruta[2:4])

'''Para separar frases em palavras usa-se split() '''

print (float("4.5") + 5)
