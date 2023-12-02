import random

# Clase que representa un nodo en el grafo.
class Nodo:
    # Método constructor de la clase Nodo.
    def __init__(self, nombre, estado="sano"):
        self.estado = estado
        self.nombre = nombre
    
    # Método que retorna el nombre del nodo y su estado.
    def __str__(self):
        return f"{self.nombre} ({self.estado})"
        
# Clase que repesenta el grafo.
class Grafo:
    # Método constructor de la clase Grafo.
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        self.probabilidad_infeccion = 0
        self.Arista = 0
    
    # Método para definir el porcentaje de infección del patógeno.
    def porcentaje_infeccion(self, probabilidad):
        self.probabilidad = probabilidad
        self.probabilidad_infeccion = float(probabilidad.strip('%'))
    
    # Método para agrega un nodo al grafo.
    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)
        self.aristas[nodo] = {}

    # Método para agregar una arista al grafo.
    def agregar_arista(self, nodo1, nodo2, peso):
        # Si el nodo1 y nodo2 están en el grafo, se agrega la arista.
        if nodo1 in self.nodos and nodo2 in self.nodos:
            self.aristas[nodo1][nodo2] = peso
            self.aristas[nodo2][nodo1] = peso
            self.Arista += 1

    # Método para obtener los nodos del grafo.
    def obtener_nodos(self):
        return self.nodos
    
    # Método para obtener las aristas del grafo.
    def obtener_aristas(self, nodo):
        return self.aristas[nodo]
    
    # Algoritmo de Prim
    def prim(self, nodo_inicial):
        visitados = set() # Conjunto de nodos visitados
        visitados.add(nodo_inicial) # Agregando el nodo inicial al conjunto de nodos visitados
        aristas_seleccionadas = [] # Lista de aristas seleccionadas
        cont = 0
        
        # Se recorre el grafo hasta que no queden aristas por recorrer
        while cont <= self.Arista:
            nodo_actual = None
            arista_minima = None
            peso_minimo = float('inf') # Peso mínimo de la arista
            
            # Se visitan los nodos empezando desde el nodo inicial (infectado)
            for nodo in visitados:
                
                # Se recorren los vecinos de cada nodo visitado
                for vecino, peso in self.aristas[nodo].items():
                    infeccion = random.randint(0, 100) # Se genera un número aleatorio para simular la infección del patógeno
                    
                    # Si el vecino no está en el conjunto de nodos visitados y el peso de la arista es menor al peso mínimo y la infección es menor o igual a la probabilidad de infección, se infecta el nodo
                    if vecino not in visitados and peso < peso_minimo and infeccion <= self.probabilidad_infeccion:
                        vecino.estado = "infectado"
                        nodo_actual = nodo
                        arista_minima = (nodo, vecino)
                        peso_minimo = peso
            
            # Si la arista mínima no es None, se agrega al conjunto de nodos visitados y a la lista de aristas seleccionadas
            if arista_minima:
                visitados.add(arista_minima[1])
                aristas_seleccionadas.append(arista_minima)
                
            cont += 1
        
        return aristas_seleccionadas
    
class Main:
    def __init__(self):
        # Creando el grafo y los nodos
        self.grafo = Grafo()
        nodo_a = Nodo("A", "infectado") # Nodo inicial infectado
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
        
        # Probabilidad de infección del patógeno
        self.grafo.porcentaje_infeccion('10%')
        
        # Sumlando la propagación del patógeno
        self.prim(nodo_a)
    
    # Pinta el grafo de los nodos infectados
    def prim(self, nodo_inicial):
        aristas_seleccionadas = self.grafo.prim(nodo_inicial)
        pesoTotal = 0
        
        # Si el tamaño de la lista es 0, significa que no se propagó el patógeno, quedando el nodo inicial como único infectado
        if len(aristas_seleccionadas) == 0:
            print("No se propagó el patógeno")
            print(f"Único infectado: {nodo_inicial}")
            return
        
        # Si el tamaño de la lista es mayor a 0, significa que se propagó el patógeno
        else: 
            print("Camino recorrido por el patógeno:")
            # Imprime las aristas seleccionadas, del camino recorrido por el patógeno con los nodos que infecto
            for arista in aristas_seleccionadas:
                print(f"{arista[0]} - {arista[1]} : {self.grafo.aristas[arista[0]][arista[1]]}")
                pesoTotal += self.grafo.aristas[arista[0]][arista[1]]
            
            print(f"Costo que tuvo el camino del patógeno al infectar: {pesoTotal}")
            
            # Imprime los nodos infectados
            print("Nodos infectados:")
            for nodo in self.grafo.nodos:
                if nodo.estado == "infectado":
                    print(nodo)
    
# Se inicia el simulador
if __name__ == "__main__":
    simulador = Main()