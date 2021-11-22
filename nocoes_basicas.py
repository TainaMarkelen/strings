# string vazia
print (type(''))

# concatenando strings
print ("15" + str(5))

# a multiplicação em strings é uma repetição
print ("legal!" * 3)

# acessando cada um do elementos
time = "Íbis"
print (time[0]) # assim sucessivamente, até 3
print (time[-1]) # devolverá o último objeto

#comparação entre strings
x = 'teoria'
y = 'prática'
z = 'teoria'

print (x == y)
print (x != y)
print (x == z)
print (x is z)

print (x > y) # isso será dado por um padrão unicod, as palavras que começam com t são maiores que as que começam com p. Caso a primeira letra seja igual, ele vai verificar a segunda letra e assim por diante
print (ord("t"))
print (ord("p"))

# ordem lexicográfica, é dado em ordem alfabética, mas as minúsculas não sempre maiores que as maiúsculas
print (ord('a')) # o código do a minúsculo é 97
print(ord("A")) # 65

# para ignorar essa diferença entre maiúsculas e minúsculas, basta colocar tudo igual, usando lower()
print ('Maçã'.lower() > 'banana'.lower())
print (ord('M'))
print (ord('b'))

a = "gato"
b = "O gato subiu no telhado"
print(b[2:6])
print(b[2:5])