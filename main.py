#crea el tablero vacio
def crear_tablero():
    tablero=[
        [".",".","."],
        [".",".","."],
        [".",".","."]
    ]
    return tablero

#Mostrar tablero
def mostrar_tablero(tablero):
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()
        

#Agregar gato y raton al tablero
def colocar_personajes(tablero):
    tablero[0][0]="G" #Gato arriba a la izquierda 
    tablero[2][2]="R"#Raton a bajo a la derecha
    
    
#Movimiento de piezas
#Encontrar al gato
def encontrar_gato(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "G":
                return i,j
            
        
#Moviemiento del gato
#primer movimiento del gato
"""def mover_gato(tablero,nueva_fila,nueva_columna):
    fila, columna=encontrar_gato(tablero)#1º se llama a la funcion de encontrar gato luego se aññade a fila y columna en su posicion respectiva
    
    tablero[fila][columna]="." #borra la posicion actual
    tablero[nueva_fila][nueva_columna]="G"#Actualiza la posicion"""
#Movimiento del gato actualizado
def mover_gato(tablero,nueva_fila,nueva_columna):
    if not es_movimiento_valido(tablero,nueva_fila,nueva_columna):
        print("Movimiento invalido")
        return #aqui el return es diferente al de los anteriores aqui significa: “salí de la función y no hagas nada más”
    
    fila,columna=encontrar_gato(tablero)
    
    tablero[fila][columna]="."
    tablero[nueva_fila][nueva_columna]="G"
    


#validacion de movimiento
def es_movimiento_valido(tablero,fila,columna):
    if fila<0 or fila>2:
        return False #esto significa que si se cumple el if, retorna falso y se refiere que esta en la fila invalida
    if columna<0 or columna>2:
        return False #lo mismo para este, pero en columna
    return True



#Programa principal
tablero=crear_tablero()#va a la funcion y devuelve la matriz
colocar_personajes(tablero)# agrega las letras en la posicion definida
mostrar_tablero(tablero)#tablero va recibiendo la funcion mostrar_tablero

print("Movimiento del gato")

mover_gato(tablero,0,1)
mostrar_tablero(tablero)

