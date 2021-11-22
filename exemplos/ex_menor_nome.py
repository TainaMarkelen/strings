def menor_nome(nomes):
    import sys
    menor_tam = sys. maxsize
    atual_local = 0
    menor_nome = ''
    
    for cap in nomes:
        nomes[atual_local] = cap.strip()
        atual_local += 1
        
    for i in nomes:
        if len(i) < menor_tam:
            menor_tam = len(i)
            menor_nome = i.capitalize()
            
    return menor_nome

if __name__ == '__main__':
    nomes = [" ana", "caio", "   roberto", " juli", "au"]
    print (menor_nome(nomes))

            
    