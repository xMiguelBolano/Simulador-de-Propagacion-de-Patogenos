import random

#   Clase que representa un nodo en el grafo.
class Nodo:
    def __init__(self, id, estado="sano"):
        
        #   id: Identificador único del nodo.
        #   estado: Estado del nodo. Por defecto es "sano".
        self.id = id
        self.estado = estado
        self.vecinos = []

#   Clase que repesenta el grafo.
class Grafo:
    def __init__(self):

        #   nodos: Lista de nodos en el grafo.
        self.nodos = []

    #   Agrega un nodo al grafo.
    def agregar_nodo(self, nodo):
        
        #   nodo: Nodo a agregar al grafo.
        self.nodos.append(nodo)

    #   Agrega una arista entre dos nodos en el grafo.
    def agregar_arista(self, nodo1, nodo2):
        nodo1.vecinos.append(nodo2)
        nodo2.vecinos.append(nodo1)

    #   Obtiene la lista de nodos en el grafo.
    def obtener_nodos(self):
        return self.nodos

    #   Implementación del algoritmo de Prim para encontrar un árbol de expansión mínima.
    def prim(self):
        
        #   Imprime el estado de cada nodo y sus vecinos.
        for nodo in self.nodos:
            vecinos = [vecino.id for vecino in nodo.vecinos]
            print(f"Nodo {nodo.id}: Estado: {nodo.estado}, Vecinos: {vecinos}")

#   Clase principal que simula la propagación de una enfermedad en un grafo.
class Main:
    def __init__(self, num_nodos=4, probabilidad_conexion=0.3, num_infectados_iniciales=1, num_pasos_tiempo=5):
        #   num_nodos: Número de nodos en el grafo. Por defecto es 4.
        #    probabilidad_conexion: Probabilidad de conexión entre nodos. Por defecto es 0.3.
        #    num_infectados_iniciales: Número de nodos infectados inicialmente. Por defecto es 1.
        #    num_pasos_tiempo: Número de pasos de tiempo a simular. Por defecto es 5.

        self.grafo = Grafo()
        self.crear_poblacion(num_nodos, probabilidad_conexion, num_infectados_iniciales)
        self.simular_propagacion(num_pasos_tiempo)

    #  Crea la población de nodos en el grafo.
    def crear_poblacion(self, num_nodos, probabilidad_conexion, num_infectados_iniciales):
        
        #    num_nodos: Número de nodos en el grafo.
        #    probabilidad_conexion: Probabilidad de conexión entre nodos.
        #    num_infectados_iniciales: Número de nodos infectados inicialmente.
        poblacion = [Nodo(id=i) for i in range(num_nodos)]

        #   Conectar nodos con cierta probabilidad
        for nodo1 in poblacion:
            for nodo2 in poblacion:
                if nodo1 != nodo2 and random.random() < probabilidad_conexion:
                    self.grafo.agregar_arista(nodo1, nodo2)

        #   Inicializar nodos infectados iniciales
        infectados_iniciales = random.sample(poblacion, num_infectados_iniciales)
        for nodo in infectados_iniciales:
            nodo.estado = 'infectado'

        #   Agregar nodos al grafo
        for nodo in poblacion:
            self.grafo.agregar_nodo(nodo)

    #   Simula la propagación de la enfermedad en el grafo durante un número dado de pasos de tiempo.
    def simular_propagacion(self, num_pasos_tiempo):

        #   num_pasos_tiempo: Número de pasos de tiempo a simular.
        for paso in range(num_pasos_tiempo):
            print(f"\nPaso de Tiempo {paso + 1}:")
            self.grafo.prim()

            for nodo in self.grafo.obtener_nodos():
                if nodo.estado == 'infectado':
                    for vecino in nodo.vecinos:
                        if vecino.estado == 'sano' and random.random() < 0.3:
                            vecino.estado = 'infectado'

if __name__ == "__main__":
    simulador = Main()