def primeiro_lex(lista):
    menor = 'z'
    
    for primeiro in lista:
        if primeiro <= menor:
            menor = primeiro
           
    return menor

if __name__ == '__main__':
    lista = ['AAAAAA', 'b']
    print(primeiro_lex(lista))