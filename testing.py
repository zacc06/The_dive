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
"""def mover_gato(tablero,nueva_fila,nueva_columna):
    if not es_movimiento_valido(tablero,nueva_fila,nueva_columna):
        print("Movimiento invalido")
        return #aqui el return es diferente al de los anteriores aqui significa: “salí de la función y no hagas nada más”
    
    fila,columna=encontrar_gato(tablero)
    
    tablero[fila][columna]="."  
    tablero[nueva_fila][nueva_columna]="G"""
    
    
#Movimiento del gato actualizado
def mover_gato(tablero,nueva_fila,nueva_columna):
    if not es_movimiento_valido(tablero,nueva_fila,nueva_columna):
        print("Movimiento invalido")
        return #aqui el return es diferente al de los anteriores aqui significa: “salí de la función y no hagas nada más”
    
    fila,columna=encontrar_gato(tablero)
    
    #Nuevo: Verificar si hay raton
    if tablero[nueva_fila][nueva_columna]=="R":#pregunta: ¿En esa posicion esta el raton?
        print("¡El gato atrapo al raton!")
    
    tablero[fila][columna]="."#esto es lo que queda de cuando avanzo
    tablero[nueva_fila][nueva_columna]="G"#esto es lo que queda de cuando avanzo
    


#validacion de movimiento
def es_movimiento_valido(tablero,fila,columna):
    if fila<0 or fila>2:
        return False #esto significa que si se cumple el if, retorna falso y se refiere que esta en la fila invalida
    if columna<0 or columna>2:
        return False #lo mismo para este, pero en columna
    return True


#Funcion igual a la del gato
#Detectar ratón
def encontrar_raton(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j]=="R":
                return i,j
            
            
#Funcion para mover al raton
def mover_raton(tablero,nueva_fila,nueva_columna):
    if not es_movimiento_valido(tablero,nueva_fila,nueva_columna):
        print("¡Movimiento invalido")
        return
    
    fila,columna=encontrar_raton(tablero)
    
    #Evitar que el raton se mueva encima del gato
    if tablero[nueva_fila][nueva_columna]=="G":
        print("¡El raton fue atrapado!")
        return
    tablero[fila][columna]="."#esto es lo que queda de cuando avanzo
    tablero[nueva_fila][nueva_columna]="R"#esta es la nueva posicion
    
    
#Funcion para verificar si existe elraton
def hay_raton(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "R":
                return True
    return False


#Funcion movimientos del gato, devuelve todas las posiciones en que el gato pueda moverse
def movimientos_gato(tablero):
    movimientos=[]
    
    fila,columna = encontrar_gato(tablero)
    
    posibles=[
        (fila -1,columna), #arriba
        (fila +1,columna), #abajo
        (fila, columna -1),#izquierda
        (fila,columna +1)#derecha
    ]
    
    for nueva_fila, nueva_columna in posibles:#concepto de desempaquetado
        if es_movimiento_valido(tablero,nueva_fila,nueva_columna):#verififica que no salga del tablero
            movimientos.append((nueva_fila,nueva_columna))
    
    return movimientos

#Funcion moviemientos del raton, lo msimo que el gato
def movimientos_raton(tablero):
    
    movimientos=[]
    
    fila,columna=encontrar_raton(tablero)
    
    posibles= [
        (fila-1, columna),
        (fila+1, columna),
        (fila,columna-1),
        (fila,columna+1)
    ]
    
    for nueva_fila, nueva_columna in posibles:
        if es_movimiento_valido(tablero,nueva_fila,nueva_columna):
            movimientos.append((nueva_fila,nueva_columna))
    return movimientos

        

#Funcion para copiar tablero
#Recibe un tablero y va a devolver una copia independiente
def copiar_tablero(tablero):
    nuevo=[] #aqui se construye el nuevo tablero
    for fila in tablero:
        nueva_fila=[] #aqui se alamecenaran las filas del tablero actual
        for elemento in fila:
            nueva_fila.append(elemento)
        nuevo.append(nueva_fila)
        
    return nuevo



#funcion para evaluar quien gana
def evaluar(tablero):
    if not hay_raton(tablero):
        return 1  #gana el gato
    return 0 # el juego continua


#Implementacion del minimax
def minimax(tablero,turno):
    #caso base
    resultado=evaluar(tablero)
    if resultado != 0:
        return resultado
    
    if turno == "G": #Gati maximiza
        mejor_valor= -999
        
        for movimiento in  movimientos_gato(tablero):
            nuevo_tablero=copiar_tablero(tablero)
            mover_gato(nuevo_tablero,movimiento[0], movimiento[1])
            
            valor= minimax(nuevo_tablero, "R")
            
            if valor>mejor_valor:
                mejor_valor=valor
                
        return mejor_valor
    
    else: #Raton minimiza
        mejor_valor=999
        
        for movimiento in movimientos_raton(tablero): #Luego hacemos del raton
            nuevo_tablero= copiar_tablero(tablero)
            mover_raton(nuevo_tablero,movimiento[0],movimiento[1])
            
            valor=minimax(nuevo_tablero,"G")
            
            if valor<mejor_valor:
                mejor_valor=valor
                
        return mejor_valor
        


#Programa principal
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
"""def mover_gato(tablero,nueva_fila,nueva_columna):
    if not es_movimiento_valido(tablero,nueva_fila,nueva_columna):
        print("Movimiento invalido")
        return #aqui el return es diferente al de los anteriores aqui significa: “salí de la función y no hagas nada más”
    
    fila,columna=encontrar_gato(tablero)
    
    tablero[fila][columna]="."  
    tablero[nueva_fila][nueva_columna]="G"""
    
    
#Movimiento del gato actualizado
def mover_gato(tablero,nueva_fila,nueva_columna):
    if not es_movimiento_valido(tablero,nueva_fila,nueva_columna):
        print("Movimiento invalido")
        return #aqui el return es diferente al de los anteriores aqui significa: “salí de la función y no hagas nada más”
    
    fila,columna=encontrar_gato(tablero)
    
    #Nuevo: Verificar si hay raton
    if tablero[nueva_fila][nueva_columna]=="R":#pregunta: ¿En esa posicion esta el raton?
        print("¡El gato atrapo al raton!")
    
    tablero[fila][columna]="."#esto es lo que queda de cuando avanzo
    tablero[nueva_fila][nueva_columna]="G"#esto es lo que queda de cuando avanzo
    


#validacion de movimiento
def es_movimiento_valido(tablero,fila,columna):
    if fila<0 or fila>2:
        return False #esto significa que si se cumple el if, retorna falso y se refiere que esta en la fila invalida
    if columna<0 or columna>2:
        return False #lo mismo para este, pero en columna
    return True


#Funcion igual a la del gato
#Detectar ratón
def encontrar_raton(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j]=="R":
                return i,j
            
            
#Funcion para mover al raton
def mover_raton(tablero,nueva_fila,nueva_columna):
    if not es_movimiento_valido(tablero,nueva_fila,nueva_columna):
        print("¡Movimiento invalido")
        return
    
    fila,columna=encontrar_raton(tablero)
    
    #Evitar que el raton se mueva encima del gato
    if tablero[nueva_fila][nueva_columna]=="G":
        print("¡El raton fue atrapado!")
        return
    tablero[fila][columna]="."#esto es lo que queda de cuando avanzo
    tablero[nueva_fila][nueva_columna]="R"#esta es la nueva posicion
    
    
#Funcion para verificar si existe elraton
def hay_raton(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "R":
                return True
    return False


#Funcion movimientos del gato, devuelve todas las posiciones en que el gato pueda moverse
def movimientos_gato(tablero):
    movimientos=[]
    
    fila,columna = encontrar_gato(tablero)
    
    posibles=[
        (fila -1,columna), #arriba
        (fila +1,columna), #abajo
        (fila, columna -1),#izquierda
        (fila,columna +1)#derecha
    ]
    
    for nueva_fila, nueva_columna in posibles:#concepto de desempaquetado
        if es_movimiento_valido(tablero,nueva_fila,nueva_columna):#verififica que no salga del tablero
            movimientos.append((nueva_fila,nueva_columna))
    
    return movimientos

#Funcion moviemientos del raton, lo msimo que el gato
def movimientos_raton(tablero):
    
    movimientos=[]
    
    fila,columna=encontrar_raton(tablero)
    
    posibles= [
        (fila-1, columna),
        (fila+1, columna),
        (fila,columna-1),
        (fila,columna+1)
    ]
    
    for nueva_fila, nueva_columna in posibles:
        if es_movimiento_valido(tablero,nueva_fila,nueva_columna):
            movimientos.append((nueva_fila,nueva_columna))
    return movimientos

        

#Funcion para copiar tablero
#Recibe un tablero y va a devolver una copia independiente
def copiar_tablero(tablero):
    nuevo=[] #aqui se construye el nuevo tablero
    for fila in tablero:
        nueva_fila=[] #aqui se alamecenaran las filas del tablero actual
        for elemento in fila:
            nueva_fila.append(elemento)
        nuevo.append(nueva_fila)
        
    return nuevo



#funcion para evaluar quien gana
def evaluar(tablero):
    if not hay_raton(tablero):
        return 1  #gana el gato
    return 0 # el juego continua


#Implementacion del minimax
def minimax(tablero,turno,profundidad):
    #caso base
    resultado=evaluar(tablero)
    if resultado != 0 or profundidad==0:
        return resultado
    
    if turno == "G": #Gati maximiza
        mejor_valor= -999
        
        for movimiento in  movimientos_gato(tablero):
            nuevo_tablero=copiar_tablero(tablero)
            mover_gato(nuevo_tablero,movimiento[0], movimiento[1])
            
            valor= minimax(nuevo_tablero, "R", profundidad-1)
            
            if valor>mejor_valor:
                mejor_valor=valor
                
        return mejor_valor
    
    else: #Raton minimiza
        mejor_valor=999
        
        for movimiento in movimientos_raton(tablero): #Luego hacemos del raton
            nuevo_tablero= copiar_tablero(tablero)
            mover_raton(nuevo_tablero,movimiento[0],movimiento[1])
            
            valor=minimax(nuevo_tablero,"G", profundidad-1)
            
            if valor<mejor_valor:
                mejor_valor=valor
                
        return mejor_valor
        







#Programa principal
tablero = crear_tablero()
colocar_personajes(tablero)

mostrar_tablero(tablero)

print("Evaluacion inicial:")
print(evaluar(tablero))

print("Resultado minimax (turno gato):")
resultado = minimax(tablero, "G", 5)
print(resultado)
"""tablero=crear_tablero()#va a la funcion y devuelve la matriz
colocar_personajes(tablero)# agrega las letras en la posicion definida

turno="G"

mostrar_tablero(tablero)#tablero va recibiendo la funcion mostrar_tablero

#Logica de los turnos
if turno =="G":
    mover_gato(tablero,0,1)
    raton="R"
else:
    mover_raton(tablero,2,1)
    turno="G"

mostrar_tablero(tablero)


print("Movimiento del Gato")
mover_gato(tablero,1,0)
mostrar_tablero(tablero)

print("Movimiento del Raton")
mover_raton(tablero,2,1)
mostrar_tablero(tablero)

movs=movimientos_gato(tablero)
print(movs)

copia=copiar_tablero(tablero)
copia[0][0]="X"
print(copia)

print(evaluar(tablero))"""