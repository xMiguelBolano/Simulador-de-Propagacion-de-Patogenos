import random

# Clase que representa un nodo en el grafo.
class Nodo:
    def __init__(self, nombre, estado="sano"):
        self.estado = estado
        self.nombre = nombre
    
    def __str__(self):
        return f"{self.nombre} ({self.estado})"
        
# Clase que repesenta el grafo.
class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        
    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        self.aristas[nodo] = {}

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.aristas[nodo1][nodo2] = peso
            self.aristas[nodo2][nodo1] = peso

    def obtener_nodos(self):
        return self.nodos
    
    def obtener_aristas(self, nodo):
        return self.aristas[nodo]
    
    def prim(self, nodo_inicial):
        visitados = set()
        visitados.add(nodo_inicial)
        aristas_seleccionadas = []
        
        while len(visitados) < len(self.nodos):
            nodo_actual = None
            arista_minima = None
            peso_minimo = float('inf')
            
            for nodo in visitados:
                for vecino, peso in self.aristas[nodo].items():
                    if vecino not in visitados and peso < peso_minimo:
                        nodo_actual = nodo
                        arista_minima = (nodo, vecino)
                        peso_minimo = peso
            
            if arista_minima:
                aristas_seleccionadas.append(arista_minima)
                visitados.add(arista_minima[1])
        
        return aristas_seleccionadas
    
class Main:
    def __init__(self):
        self.grafo = Grafo()
        nodo_a = Nodo("A", "infectado")
        nodo_b = Nodo("B")
        nodo_c = Nodo("C")
        nodo_d = Nodo("D")
        nodo_e = Nodo("E")
        self.grafo.agregar_nodo(nodo_a)
        self.grafo.agregar_nodo(nodo_b)
        self.grafo.agregar_nodo(nodo_c)
        self.grafo.agregar_nodo(nodo_d)
        self.grafo.agregar_nodo(nodo_e)
        self.grafo.agregar_arista(nodo_a, nodo_b, 5)
        self.grafo.agregar_arista(nodo_a, nodo_c, 3)
        self.grafo.agregar_arista(nodo_b, nodo_d, 7)
        self.grafo.agregar_arista(nodo_c, nodo_d, 2)
        self.grafo.agregar_arista(nodo_c, nodo_e, 4)
        self.grafo.agregar_arista(nodo_d, nodo_e, 1)
        "self.pintar_grafo()"
        self.prim(nodo_a)
    
    def pintar_grafo(self):
        for nodo in self.grafo.obtener_nodos():
            print(f"Nodo {nodo}:")
            for vecino, peso in self.grafo.aristas[nodo].items():
                print(f"  -> Nodo {vecino}, Peso: {peso}")
            print()
    
    def prim(self, nodo_inicial):
        aristas_seleccionadas = self.grafo.prim(nodo_inicial)
        print("Aristas seleccionadas:")
        for arista in aristas_seleccionadas:
            print(f"{arista[0]} - {arista[1]} : {self.grafo.aristas[arista[0]][arista[1]]}")
    
        


if __name__ == "__main__":
    simulador = Main()