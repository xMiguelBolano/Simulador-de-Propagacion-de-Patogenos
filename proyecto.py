import random

#   Clase que representa un nodo en el grafo.
class Nodo:
    def __init__(self, nombre, estado="sano"):
        #   estado: Estado del nodo. Por defecto es "sano".
        self.estado = estado
        self.nombre = nombre
    
    def __str__(self):
        return f"{self.nombre} ({self.estado})"
        
#   Clase que repesenta el grafo.
class Grafo:
    def __init__(self):
        #   nodos: Lista de nodos en el grafo.
        self.nodos = set()
        self.aristas = {}
        
    #   Agrega un nodo al grafo.
    def agregar_nodo(self, nodo):
        #   nodo: Nodo a agregar al grafo.
        self.nodos.add(nodo)
        self.aristas[nodo] = {}

    #   Agrega una arista entre dos nodos en el grafo.
    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.aristas[nodo1][nodo2] = peso
            self.aristas[nodo2][nodo1] = peso

    #   Obtiene la lista de nodos en el grafo.
    def obtener_nodos(self):
        return self.nodos
    
class Main:
    def __init__(self, num_infectados_iniciales=1, num_pasos_tiempo=5):
        #   num_infectados_iniciales: Número de nodos infectados inicialmente. Por defecto es 1.
        #   num_pasos_tiempo: Número de pasos de tiempo a simular. Por defecto es 5.
        
        self.grafo = Grafo()
        # Creando nodos
        nodo_a = Nodo("A", "infectado")
        nodo_b = Nodo("B")
        nodo_c = Nodo("C")
        nodo_d = Nodo("D")
        nodo_e = Nodo("E")
        # Agregando Nodos
        self.grafo.agregar_nodo(nodo_a)
        self.grafo.agregar_nodo(nodo_b)
        self.grafo.agregar_nodo(nodo_c)
        self.grafo.agregar_nodo(nodo_d)
        self.grafo.agregar_nodo(nodo_e)
        # Agregando Aristas
        self.grafo.agregar_arista(nodo_a, nodo_b, 5)
        self.grafo.agregar_arista(nodo_a, nodo_c, 3)
        self.grafo.agregar_arista(nodo_b, nodo_d, 7)
        self.grafo.agregar_arista(nodo_c, nodo_d, 2)
        self.grafo.agregar_arista(nodo_c, nodo_e, 4)
        self.grafo.agregar_arista(nodo_d, nodo_e, 1)
    
        self.pintar_grafo()
        "self.simular_propagacion(num_pasos_tiempo, num_infectados_iniciales)"
    
    # Pinta el grafo original 
    def pintar_grafo(self):
        for nodo in self.grafo.obtener_nodos():
            print(f"Nodo {nodo}:")
            for vecino, peso in self.grafo.aristas[nodo].items():
                print(f"  -> Nodo {vecino}, Peso: {peso}")
            print()
    
    #   Simula la propagación de la enfermedad en el grafo.
    def simular_propagacion(self, num_pasos_tiempo, num_infectados_iniciales):
        poblacion = self.grafo.obtener_nodos()
        
        
        #   num_pasos_tiempo: Número de pasos de tiempo a simular.
        for i in range(num_pasos_tiempo):
            print(f"Paso de tiempo {i}")
            self.grafo.prim()

#   Ejecuta el simulador.
if __name__ == "__main__":
    simulador = Main()