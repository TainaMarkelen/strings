def maiusculas(frase):
    string = ''
    pos = 0
    tamanho = len(frase) - 1
    
    while pos <= tamanho:
        if ord(frase[pos]) >= 65 and ord(frase[pos]) <= 90:
            string += frase[pos]
        pos += 1
        
    return string

if __name__ == '__main__':
    frase = "Programamos em Python 3.E"
    print (maiusculas(frase))