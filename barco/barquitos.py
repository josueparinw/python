import random
tamanos = [4, 3, 2, 2, 1, 1]
barcos = ["🛳️", "🚢", "⛴️", "🛥️", "🚤", "⛵"]
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def crearTablero(n):
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append("🌊")
        tablero.append(fila)
    return tablero

def imprimirTablero(tablero): #plantilla
    print("   ", end="")
    for j in range(len(tablero)):
        print(j + 1, end="    ")
    print()
    for i in range(len(tablero)):
        print(letras[i], end=" ")
        for j in range(len(tablero)):
            print(tablero[i][j], end="   ")
        print()

def pedirCoordenada(tablero):
    n = len(tablero)
    valida = False

    while not valida:
        coor = input("Introduce coordenada, ej: A1:").upper()
        if len(coor) >= 2:
            letra = coor[0]
            numero = coor[1:]
            if letra in letras[:n] and numero.isdigit():
                numero = int(numero)
                if numero >= 1 and numero <= n:
                    valida = True
        if not valida:
            print("Coordenada incorrecta, intenta otra vez")

    fila = letras.index(letra)
    columna = numero - 1
    return fila, columna

def pedirDireccion():
    direccion = input("Dirección horizontal o vertical:").lower()
    while direccion != "horizontal" and direccion != "vertical":
        direccion = input("Dirección incorrecta (horizontal o vertical):").lower()
    return direccion

def comprobarPosicion(tablero, fila, columna, tamano, direccion):
    n = len(tablero)

    for k in range(tamano):
        if direccion == "horizontal":
            i = fila
            j = columna + k
        else:
            i = fila + k
            j = columna
        if i >= n or j >= n:
            return False
        if tablero[i][j] != "🌊":
            return False
    return True

def colocarBarco(tablero, fila, columna, tamano, direccion, simbolo):
    for k in range(tamano):
        if direccion == "horizontal":
            tablero[fila][columna + k] = simbolo
        else:
            tablero[fila + k][columna] = simbolo

def posicionarBarcos(tablero):
    for i in range(len(tamanos)):
        tamano = tamanos[i]
        simbolo = barcos[i]
        colocado = False
        while not colocado:
            print("\nColoca el barco de tamaño", tamano)
            imprimirTablero(tablero)
            fila, columna = pedirCoordenada(tablero)
            if tamano == 1:
                direccion = "horizontal"
            else:
                direccion = pedirDireccion()

            if comprobarPosicion(tablero, fila, columna, tamano, direccion):
                colocarBarco(tablero, fila, columna, tamano, direccion, simbolo)
                colocado = True
            else:
                print("El barco no cabe o está encima de otro")

    print("\nBarcos colocados en tu tablero:")
    imprimirTablero(tablero)

def posicionarBarcosMaquina(tablero):
    n = len(tablero)

    for i in range(len(tamanos)):
        tamano = tamanos[i]
        simbolo = barcos[i]
        colocado = False

        while not colocado:
            fila = random.randint(0, n - 1)
            columna = random.randint(0, n - 1)
            direccion = random.choice(["horizontal", "vertical"])

            if comprobarPosicion(tablero, fila, columna, tamano, direccion):
                colocarBarco(tablero, fila, columna, tamano, direccion, simbolo)
                colocado = True


def pedirDisparo(tableroMostrado):
    fila, columna = pedirCoordenada(tableroMostrado)

    while tableroMostrado[fila][columna] != "🌊":
        print("Ya disparaste ahí")
        fila, columna = pedirCoordenada(tableroMostrado)

    return fila, columna


def disparar(tablero, tableroMostrado, fila, columna):
    # Si es agua
    if tablero[fila][columna] == "🌊":
        tablero[fila][columna] = "💨"
        tableroMostrado[fila][columna] = "💨"
        return "Agua"

    simbolo = tablero[fila][columna]
    tablero[fila][columna] = "💥"
    tableroMostrado[fila][columna] = "💥"

    quedan = False
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == simbolo:
                quedan = True

    if quedan:
        return "Tocado"
    else:
        return "Hundido"


def quedanBarcos(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] in barcos:
                return True
    return False

def añadirVecinas(tableroMostrado, fila, columna, pendientes):
    n = len(tableroMostrado)

    vecinas = [
        (fila - 1, columna),
        (fila + 1, columna),
        (fila, columna - 1),
        (fila, columna + 1)
    ]

    for vecina in vecinas:
        i = vecina[0]
        j = vecina[1]

        if i >= 0 and i < n and j >= 0 and j < n:
            if tableroMostrado[i][j] == "🌊" and vecina not in pendientes:
                pendientes.append(vecina)


def disparoMaquina(tablero, tableroMostrado, pendientes):
    n = len(tablero)

    if len(pendientes) > 0:
        fila, columna = pendientes.pop(0)
    else:
        fila = random.randint(0, n - 1)
        columna = random.randint(0, n - 1)
        while tableroMostrado[fila][columna] != "🌊":
            fila = random.randint(0, n - 1)
            columna = random.randint(0, n - 1)

    print("La Maquina dispara a", letras[fila] + str(columna + 1))

    resultado = disparar(tablero, tableroMostrado, fila, columna)
    print("Resultado:", resultado)

    if resultado == "Tocado":
        añadirVecinas(tableroMostrado, fila, columna, pendientes)
    elif resultado == "Hundido":
        pendientes.clear()


def pedirTamano():
    n = input("De que tamaño quieres el tablero? 6 a 26: ")
    while not n.isdigit() or int(n) < 6 or int(n) > 26:
        n = input("Tamaño incorrecto 6 a 26: ")
    return int(n)


def jugar():
    n = pedirTamano()

    tableroUsuario = crearTablero(n)
    tableroMaquina = crearTablero(n)

    mostradoUsuario = crearTablero(n)
    mostradoMaquina = crearTablero(n)

    pendientes = []

    print("\n******** HUNDIR LA FLOTA ********")

    posicionarBarcos(tableroUsuario)
    posicionarBarcosMaquina(tableroMaquina)

    while quedanBarcos(tableroUsuario) and quedanBarcos(tableroMaquina):
        print("\n******** TURNO USUARIO ********")
        print("Tablero de la maquina:")
        imprimirTablero(mostradoMaquina)

        fila, columna = pedirDisparo(mostradoMaquina)
        resultado = disparar(tableroMaquina, mostradoMaquina, fila, columna)
        print("Resultado:", resultado)

        if quedanBarcos(tableroMaquina):
            print("\n******** TURNO MAQUINA ********")
            disparoMaquina(tableroUsuario, mostradoUsuario, pendientes)

            print("\nTu tablero:")
            imprimirTablero(tableroUsuario)

    if quedanBarcos(tableroUsuario):
        print("\n¡LE GANASTE A LA MAQUINA!")
    else:
        print("\nHAS PERDIDO")
        print("Tablero de la Maquina:")
        imprimirTablero(tableroMaquina)


jugar()
print("fin xd")
