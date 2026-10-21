lista = [5, 6, 9, 1, 2, 7, 8, 4, 3]
derecha =0
izquierda=len(lista)-1
cambio = True
while cambio :
    cambio=False
    for i in range (derecha,izquierda):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            cambio =True
    print(lista)

    for i in range(izquierda,derecha,-1):
        if lista[i-1] > lista[i]:
            lista[i], lista[i-1] = lista[i-1], lista[i]
            cambio = True
    print(lista)
    derecha+=1

print(lista)

