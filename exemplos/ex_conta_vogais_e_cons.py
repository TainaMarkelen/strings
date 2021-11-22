# função que retorna a quantidade de vogais ou consoantes, para retornar a quantidade de consoantes basta inserir no segundo parâmetro qualquer outra palavra que não seja "vogais"

def conta_letras(frase, contar="vogais"):
    pos = 0
    frase.lower().strip()
    quantidade = 0
    
    while pos < len(frase):
        if contar == "vogais":
            if frase[pos] == 'a' or frase[pos] == 'e' or frase[pos] == 'i' or frase[pos] == 'o' or frase[pos] == 'u':
                quantidade += 1
            pos += 1
        else:
            if frase[pos] != 'a' and frase[pos] != 'e' and frase[pos] != 'i' and frase[pos] != 'o' and frase[pos] != 'u' and ord(frase[pos]) >= 97 and ord(frase[pos]) <= 122:
                quantidade += 1
            pos += 1
            
    return quantidade

if __name__ == '__main__':
    print(conta_letras('programamos em python', 'vogais'))