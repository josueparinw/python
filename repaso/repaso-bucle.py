#Pregunta al sistema cuántos alumnos tiene una clase, y rellena una lista con
#los nombres de los alumnos. Ordenad la lista por orden alfabético.
#-> sort, búscalo en internet.
#Ahora, pídele al usuario que entre en el sistema escribiendo su nombre (el
#nombre de un alumno en minúsculas seguido inmediatamente de su número de lista
#que le corresponda cuando ya esté ordenada alfabéticamente. El número de lista
#empieza a contar en 1.) Cualquiera que escriba el nombre y el numero de lista
#de un alumno existente y que coincida puede entrar. Tiene 3 intentos para acertar,
#si se pasa, se acaba el programa. Si acierta, también.

nombres_alumnos=["Juan","ana","miguel","manuela","jose","pepe"]
ordenado = sorted( nombres_alumnos ,key=str.lower)
intentos = 0
encontrado =False

while  not encontrado and intentos <3:
    contador = 0
    nombre = input("ingrese un nombre:")
    num = int(input("ingrese un numero de lista:"))
    for i in ordenado:
        contador +=1
        if nombre.lower() == i.lower() and contador==num:
            print(f"encontrado : {contador}: {i}")
            encontrado=True

    if not encontrado:
        print("gay")
        intentos +=1


if intentos==3:
    print("se acabaron tus intentos")