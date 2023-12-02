import random

# Clase que representa un nodo en el grafo.
class Nodo:
    def __init__(self, nombre, estado="sano"):
        self.estado = estado
        self.nombre = nombre
    
    def __str__(self):
        return f"{self.nombre} ({self.estado})"
    
    def getEstado(self):
        return self.estado
        
# Clase que repesenta el grafo.
class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        self.probabilidad_infeccion = 0
        self.Arista = 0
    
    def porcentaje_infeccion(self, probabilidad):
        self.probabilidad = probabilidad
        self.probabilidad_infeccion = float(probabilidad.strip('%'))
     
    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        self.aristas[nodo] = {}

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.aristas[nodo1][nodo2] = peso
            self.aristas[nodo2][nodo1] = peso
            self.Arista += 1

    def obtener_nodos(self):
        return self.nodos
    
    def obtener_aristas(self, nodo):
        return self.aristas[nodo]
    
    def prim(self, nodo_inicial):
        visitados = set()
        visitados.add(nodo_inicial)
        aristas_seleccionadas = []
        cont = 0
        
        while cont <= self.Arista:
            nodo_actual = None
            arista_minima = None
            peso_minimo = float('inf')
            
            for nodo in visitados:
                for vecino, peso in self.aristas[nodo].items():
                    infeccion = random.randint(0, 100)
                    if vecino not in visitados and peso < peso_minimo and infeccion <= self.probabilidad_infeccion:
                        vecino.estado = "infectado"
                        nodo_actual = nodo
                        arista_minima = (nodo, vecino)
                        peso_minimo = peso
            
            if arista_minima:
                visitados.add(arista_minima[1])
                aristas_seleccionadas.append(arista_minima)
                
            cont += 1
        
        return aristas_seleccionadas
    
class Main:
    def __init__(self):
        # Creando nodos
        self.grafo = Grafo()
        nodo_a = Nodo("A", "infectado")
        nodo_b = Nodo("B")
        nodo_c = Nodo("C")
        nodo_d = Nodo("D")
        nodo_e = Nodo("E")
        nodo_f = Nodo("F")
        
        # Agregando nodos al grafo y creando aristas
        self.grafo.agregar_nodo(nodo_a)
        self.grafo.agregar_nodo(nodo_b)
        self.grafo.agregar_nodo(nodo_c)
        self.grafo.agregar_nodo(nodo_d)
        self.grafo.agregar_nodo(nodo_e)
        self.grafo.agregar_nodo(nodo_f) # Nodo aislado
        self.grafo.agregar_arista(nodo_a, nodo_b, 2)
        self.grafo.agregar_arista(nodo_a, nodo_d, 7)
        self.grafo.agregar_arista(nodo_a, nodo_e, 5)
        self.grafo.agregar_arista(nodo_b, nodo_c, 4)
        
        #Probabilidad de infección
        self.grafo.porcentaje_infeccion('10%')
        
        print("Simulación")
        # Propagación del patógeno
        self.prim(nodo_a)
    
    def prim(self, nodo_inicial):
        aristas_seleccionadas = self.grafo.prim(nodo_inicial)
        pesoTotal = 0
        print("Aristas seleccionadas:")
        for arista in aristas_seleccionadas:
            print(f"{arista[0]} - {arista[1]} : {self.grafo.aristas[arista[0]][arista[1]]}")
            pesoTotal += self.grafo.aristas[arista[0]][arista[1]]
            
        print(f"Peso total: {pesoTotal}")
    
        


if __name__ == "__main__":
    simulador = Main()