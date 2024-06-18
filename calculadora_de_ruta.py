import heapq

cant_filas = int(input("Ingrese la cantidad de filas para la matriz: "))
cant_columnas = int(input("Ingrese la cantidad de columnas para la matriz: "))

matriz = [] # Inicializa una matriz vacía
for fila in range(cant_filas): # Recorre por filas
    elemento = [] # Cada elemento de la matriz es una lista
    for columna in range(cant_columnas): # Recorre por columnas
        elemento.append(0) # Agrega un valor a la primera fila (lista)
    matriz.append(elemento) # Agrega la lista a la matriz

def mostrar_matriz(matriz):
    # for fila in matriz:
    #     print(fila)
    for fila in matriz:
        print(" ".join(map(str, fila)))

mostrar_matriz(matriz)

def ingresar_coordenadas(): # Función para ingresar coordenadas del punto de partida y llegada
    x = int(input("Ingrese la fila: "))
    y = int(input("Ingrese la columna: "))

    if existen_coordenadas(x, y, cant_filas, cant_columnas): # Llama a la función validadora
        return (x, y) # Retorna los valores de las coordenadas (fila,columna)
    else:
        print("Coordenadas inválidas. Intente nuevamente.") # Mensaje de error
        return ingresar_coordenadas() # La función se llama a sí misma (recursividad)
    
def existen_coordenadas(x, y, cant_filas, cant_columnas): # Valida las coordenadas
    return 0 <= x < cant_filas and 0 <= y < cant_columnas # Retorna verdadero o falso según exista la coordenada

def colocar_obstaculo():
    while True:
        respuesta = input("Desea colocar un obstaculo? S/N: ")
        if respuesta.upper() == "S":
            while True:
                tipo = int(input(''' Elija el tipo de bloqueo:
                    1: Edificios u obstáculos que no se pueden atravesar.
                    2: Agua u otros obstáculos que requieren una ruta alternativa.
                    3: Áreas bloqueadas temporalmente debido a construcciones o eventos especiales.: '''))
                if tipo == 1 or tipo == 2 or tipo == 3:
                    break
                else:
                    print("Opción inválida")
            coordenada_obstaculo = ingresar_coordenadas()
            matriz[coordenada_obstaculo[0]][coordenada_obstaculo[1]] = tipo 
        elif respuesta.upper() == "N":
            break
        else:
            print("Debe responder con 'S' o 'N'")

colocar_obstaculo()

print("\nElija el punto de partida")
punto_de_partida = ingresar_coordenadas()
print("\nElija el punto de llegada")
punto_de_llegada = ingresar_coordenadas()

matriz[punto_de_partida[0]][punto_de_partida[1]] = "I"
matriz[punto_de_llegada[0]][punto_de_llegada[1]] = "F"

print("\nMapa original")
mostrar_matriz(matriz)

def distancia_Manhattan(punto_de_partida, punto_de_llegada):
    return abs(punto_de_partida[0] - punto_de_llegada[0]) + abs(punto_de_partida[1] - punto_de_llegada[1])

def algoritmo_A_estrella():
    nodos_por_explorar = []
    # Agrego el nodo inicial a la lista de nodos por explorar, con orden de prioridad
    heapq.heappush(nodos_por_explorar, (0, punto_de_partida))
    nodos_cerrados_explorados = []
    predecesores = {}
    # Al no haber dado paso para llegar al punto de partida, el costo es 0
    costo_g = {punto_de_partida: 0}
    # f(n) = g(n) + h(nodo_inicial, nodo_final)
    costo_f = {punto_de_partida: distancia_Manhattan(punto_de_partida, punto_de_llegada)}

    while nodos_por_explorar: # Mientras hayan nodos sin explorar
        # Elimino el primer elemento (tupla) de la cola, y a la vez guardo sus valores en costo y nodo_actual respectivamente
        costo, nodo_actual = heapq.heappop(nodos_por_explorar)
        if nodo_actual == punto_de_llegada: # Significa que llegué al objetivo
            # Lista vacía para la ruta
            ruta = []
            while nodo_actual in predecesores: # Cuando el predecesor sea el punto de partida, termina el bucle
                ruta.append(nodo_actual) # Agrego el nodo actual a la ruta
                nodo_actual = predecesores[nodo_actual] # El nodo actual pasa a ser el predecesor
            ruta.append(punto_de_partida) # Agrego el punto de partida a la ruta
            return ruta[::-1] # retornar la lista pero con orden inverso
    
        nodos_cerrados_explorados.append(nodo_actual)

        for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
            nodo_vecino = (nodo_actual[0] + x, nodo_actual[1] + y)
            # No debe estar fuera del mapa
            if not (0 <= nodo_vecino[0] < cant_filas and 0 <= nodo_vecino[1] < cant_columnas):
                continue
            # No debe ser un obstáculo
            if matriz[nodo_vecino[0]][nodo_vecino[1]] in [1,2,3]:
                continue
            # No debe estar en la lista de nodos explorados
            if nodo_vecino in nodos_cerrados_explorados:
                continue
            
            # Sumamos 1 porque damos un paso más para llegar hasta el nodo actual
            costo_g_vecino = costo_g[nodo_actual] + 1

            # Si todavía no guardé la cantidad de pasos para llegar hasta este nodo
            # O encontré un camino en el que doy menos pasos

            if costo_g_vecino not in costo_g or costo_g_vecino < costo_g[nodo_vecino]:
                
                predecesores[nodo_vecino] = nodo_actual # El nodo actual es predecesor del nodo vecino
                costo_g[nodo_vecino] = costo_g_vecino # Guardo la cantidad de pasos mínima para llegar hasta ese nodo
                costo_f[nodo_vecino] = costo_g_vecino + distancia_Manhattan(nodo_vecino, punto_de_llegada) # Guardo el costo total
                # Agrego el nodo a la lista de nodos por explorar
                heapq.heappush(nodos_por_explorar, (costo_f[nodo_vecino], nodo_vecino))

    return []

ruta_encontrada = algoritmo_A_estrella()

if ruta_encontrada == []:
    print("\nNo encontré una ruta para llegar a tu destino")
else:
    print(ruta_encontrada)
    for elemento in ruta_encontrada:
        matriz[elemento[0]][elemento[1]] =  "*"

    print("\nRuta Encontrada")
    mostrar_matriz(matriz)