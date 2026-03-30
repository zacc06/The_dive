# =========================
# FUNCIONES
# =========================

# Crear tablero
def crear_tablero():
    return [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]


# Mostrar tablero
def mostrar_tablero(tablero):
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()


# Colocar personajes
def colocar_personajes(tablero):
    tablero[0][0] = "G"
    tablero[2][2] = "R"


# Encontrar gato
def encontrar_gato(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "G":
                return i, j


# Encontrar ratón
def encontrar_raton(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "R":
                return i, j


# Validar movimiento
def es_movimiento_valido(tablero, fila, columna):
    if fila < 0 or fila > 2:
        return False
    if columna < 0 or columna > 2:
        return False
    return True


# Mover gato (SIN prints para minimax)
def mover_gato(tablero, nueva_fila, nueva_columna):
    if not es_movimiento_valido(tablero, nueva_fila, nueva_columna):
        return

    fila, columna = encontrar_gato(tablero)

    tablero[fila][columna] = "."
    tablero[nueva_fila][nueva_columna] = "G"


# Mover ratón (SIN prints)
def mover_raton(tablero, nueva_fila, nueva_columna):
    if not es_movimiento_valido(tablero, nueva_fila, nueva_columna):
        return

    fila, columna = encontrar_raton(tablero)

    # evitar pisar gato
    if tablero[nueva_fila][nueva_columna] == "G":
        return

    tablero[fila][columna] = "."
    tablero[nueva_fila][nueva_columna] = "R"


# Verificar si hay ratón
def hay_raton(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "R":
                return True
    return False


# Movimientos posibles del gato
def movimientos_gato(tablero):
    movimientos = []

    fila, columna = encontrar_gato(tablero)

    posibles = [
        (fila - 1, columna),
        (fila + 1, columna),
        (fila, columna - 1),
        (fila, columna + 1)
    ]

    for nueva_fila, nueva_columna in posibles:
        if es_movimiento_valido(tablero, nueva_fila, nueva_columna):
            movimientos.append((nueva_fila, nueva_columna))

    return movimientos


# Movimientos posibles del ratón
def movimientos_raton(tablero):
    movimientos = []

    fila, columna = encontrar_raton(tablero)

    posibles = [
        (fila - 1, columna),
        (fila + 1, columna),
        (fila, columna - 1),
        (fila, columna + 1)
    ]

    for nueva_fila, nueva_columna in posibles:
        if es_movimiento_valido(tablero, nueva_fila, nueva_columna):
            movimientos.append((nueva_fila, nueva_columna))

    return movimientos


# Copiar tablero
def copiar_tablero(tablero):
    nuevo = []
    for fila in tablero:
        nueva_fila = []
        for elemento in fila:
            nueva_fila.append(elemento)
        nuevo.append(nueva_fila)
    return nuevo


# Evaluar estado
def evaluar(tablero):
    if not hay_raton(tablero):
        return 1  # gana gato
    return 0


# Minimax con profundidad
def minimax(tablero, turno, profundidad):
    resultado = evaluar(tablero)

    if resultado != 0 or profundidad == 0:
        return resultado

    if turno == "G":  # maximiza
        mejor_valor = -999

        for movimiento in movimientos_gato(tablero):
            nuevo_tablero = copiar_tablero(tablero)
            mover_gato(nuevo_tablero, movimiento[0], movimiento[1])

            valor = minimax(nuevo_tablero, "R", profundidad - 1)

            if valor > mejor_valor:
                mejor_valor = valor

        return mejor_valor

    else:  # minimiza
        mejor_valor = 999

        for movimiento in movimientos_raton(tablero):
            nuevo_tablero = copiar_tablero(tablero)
            mover_raton(nuevo_tablero, movimiento[0], movimiento[1])

            valor = minimax(nuevo_tablero, "G", profundidad - 1)

            if valor < mejor_valor:
                mejor_valor = valor

        return mejor_valor


# =========================
# PROGRAMA PRINCIPAL
# =========================

tablero = crear_tablero()
colocar_personajes(tablero)

print("Tablero inicial:")
mostrar_tablero(tablero)

print("Evaluación inicial:")
print(evaluar(tablero))

print("Resultado minimax (turno gato):")
resultado = minimax(tablero, "G", 5)
print(resultado)