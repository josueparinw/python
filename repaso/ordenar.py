import random
import time

inicio = time.time()

lista =[9,2,4,6,1]

for i in range(len(lista)-1):
    print(lista)
    print(" ")

    for j in range(len(lista)-1):

        if lista[j]>lista[j+1]:

            aux = lista[j]

            lista[j]=lista[j+1]
            lista[j+1]=aux

            #lista[j],lista[j+1]=lista[j+1],lista[j]

    print(lista)

