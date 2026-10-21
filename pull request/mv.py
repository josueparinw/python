lista=[12,20,30,45,1,2,5,100]

#print(lista[-3:] + lista[:-3])  izquierda
#print(lista[3:] + lista[:3])  derecha

def mover (lista,numero,posicion):
    if numero<len(lista) and posicion=="derecha":
        return print(lista[numero:] + lista[:numero])

    elif numero<len(lista) and posicion=="izquierda":
        return print(lista[-numero:] + lista[:-numero])
    else:
       return print("limite de rango de la lista")


mover(lista,5,"izquierda")