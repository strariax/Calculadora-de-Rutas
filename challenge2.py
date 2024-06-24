import heapq

class Mapa:

    # Atributos de instancia: filas y columnas

    def __init__(self, filas, columnas, punto_de_partida, punto_de_llegada):
        self.filas = filas
        self.columnas = columnas
        self.punto_de_partida = punto_de_partida
        self.punto_de_llegada = punto_de_llegada
        self.matriz = self.cargar_matriz()

    # Método para inicializar la matriz con ceros

    def cargar_matriz(self):
        matriz = []
        for fila in range(self.filas):
            elemento = []
            for columna in range(self.columnas):
                elemento.append(0)
            matriz.append(elemento)
        return matriz

    # Método para mostrar la matriz

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(" ".join(map(str, fila)))
    
    # Validar que las coordenadas estén dentro de la matriz

    def validar_posicion(self, x, y):
        return 0 <= x < self.filas and 0 <= y < self.columnas
    
    # Método para agregar obstáculos a la matriz

    def agregar_obstaculos(self):
        while True:
            tipo = int(input(''' Elija el tipo de bloqueo:
                        1: Edificios u obstáculos que no se pueden atravesar.
                        2: Agua u otros obstáculos que requieren una ruta alternativa.
                        3: Áreas bloqueadas temporalmente debido a construcciones o eventos especiales.: '''))
            if tipo in [1,2,3]:
                break
            else:
                print("Opción Inválida")
        posicion_obstaculo = elegir_posicion()
        self.matriz[posicion_obstaculo[0]][posicion_obstaculo[1]] = tipo

    # Método para verificar si la matriz tiene obstáculos

    def verificar_obstaculos(self):
        tiene_obstaculos = False
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.matriz[fila][columna] in [1,2,3]:
                    tiene_obstaculos = True
        return tiene_obstaculos

    # Método para quitar obstáculos

    def quitar_obstaculos(self):
        print("\nIngrese la posición del obstáculo que desea eliminar")
        obstaculo_a_eliminar = elegir_posicion()
        if self.matriz[obstaculo_a_eliminar[0]][obstaculo_a_eliminar[1]] in [1,2,3]:
            self.matriz[obstaculo_a_eliminar[0]][obstaculo_a_eliminar[1]] = 0
        else:
            print(f"No hay obstáculo en la posición {obstaculo_a_eliminar}")


class Algoritmo_A_Estrella(Mapa):
    
    def distancia_manhattan(self, punto1, punto2):
        return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])

    def busqueda(self):
        
        nodos_por_explorar = []
        # Agrego el nodo inicial a la lista de nodos por explorar, con orden de prioridad
        heapq.heappush(nodos_por_explorar, (0, self.punto_de_partida))
        nodos_cerrados_explorados = []
        predecesores = {}
        # Al no haber dado paso para llegar al punto de partida, el costo es 0
        costo_g = {self.punto_de_partida: 0}
        # f(n) = g(n) + h(nodo_inicial, nodo_final)
        costo_f = {self.punto_de_partida: self.distancia_manhattan(self.punto_de_partida, self.punto_de_llegada)}

        while nodos_por_explorar: # Mientras hayan nodos sin explorar
            # Elimino el primer elemento (tupla) de la cola, y a la vez guardo sus valores en costo y nodo_actual respectivamente
            costo, nodo_actual = heapq.heappop(nodos_por_explorar)
            if nodo_actual == self.punto_de_llegada: # Significa que llegué al objetivo
                return self.reconstruir_camino(predecesores, nodo_actual)
        
            nodos_cerrados_explorados.append(nodo_actual)

            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                nodo_vecino = (nodo_actual[0] + x, nodo_actual[1] + y)
                # No debe estar fuera del mapa
                if not (self.validar_posicion(nodo_vecino[0], nodo_vecino[1])):
                    continue
                # No debe ser un obstáculo
                if self.matriz[nodo_vecino[0]][nodo_vecino[1]] in [1,2,3]:
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
                    costo_f[nodo_vecino] = costo_g_vecino + self.distancia_manhattan(nodo_vecino, self.punto_de_llegada) # Guardo el costo total
                    # Agrego el nodo a la lista de nodos por explorar
                    heapq.heappush(nodos_por_explorar, (costo_f[nodo_vecino], nodo_vecino))
        
        return []

    def reconstruir_camino(self, predecesores, nodo_actual):
        ruta = []
        while nodo_actual in predecesores: # Cuando el predecesor sea el punto de partida, termina el bucle
            ruta.append(nodo_actual) # Agrego el nodo actual a la ruta
            nodo_actual = predecesores[nodo_actual] # El nodo actual pasa a ser el predecesor
        ruta.append(self.punto_de_partida) # Agrego el punto de partida a la ruta
        return ruta[::-1] # retornar la lista pero con orden inverso
        
    
# Validar la respuesta del usuario

def validar_respuesta(respuesta_usuario):
    return respuesta_usuario in ['S', 'N']

# Ingresar coordenadas

def elegir_posicion():
    while True:
        x = int(input("\nIngrese la fila: "))
        y = int(input("Ingrese la columna: "))

        if matriz.validar_posicion(x, y):
            return (x, y)
        else:
            print("Posición Inválida")

matriz = Algoritmo_A_Estrella(4,4, (0,0), (3,3)) # Crea el objeto matriz, al que pasamos la clase Mapa, definimos las dimensiones, y los puntos de partida y llegada
matriz.mostrar_matriz() # usamos el método para mostrar la matriz

while True:
    respuesta = input("\nDesea agregar un obstáculo? S/N: ").upper()
    if validar_respuesta(respuesta):
        if respuesta == 'S':
            matriz.agregar_obstaculos()
        else:
            break
    else:
        print("Debe responder con 'S' o 'N'")


if matriz.verificar_obstaculos():

    print("\nMapa con obstáculos:")
    matriz.mostrar_matriz()

    while True:
        respuesta = input("\nDesea quitar un obstáculo? S/N: ").upper()
        if validar_respuesta(respuesta):
            if respuesta == 'S':
                matriz.quitar_obstaculos()
                print("\nMapa modificado:")
                matriz.mostrar_matriz()
            else:
                break

            if not(matriz.verificar_obstaculos()):
                break
        else:
            print("Debe responder con 'S' o 'N'")

camino_resuelto = matriz.busqueda()

if camino_resuelto:
    for posicion in camino_resuelto:
        matriz.matriz[posicion[0]][posicion[1]] = "*"
    print("\nRuta encontrada")
    matriz.mostrar_matriz()
else:
    print("\nNo se ha encontrado camino hasta su destino")