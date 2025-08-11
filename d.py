import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

# =========================
# Simulación del contagio
# =========================
def simular_contagio(G, prob_infeccion, nodo_inicial):
    estados = {n: "sano" for n in G.nodes}
    estados[nodo_inicial] = "infectado"
    
    pasos = [estados.copy()]
    visitados = set([nodo_inicial])

    for _ in range(len(G.edges) + 1):
        arista_minima = None
        peso_minimo = float("inf")

        for nodo in visitados:
            for vecino, datos in G[nodo].items():
                peso = datos["weight"]
                infeccion = random.randint(0, 100)
                if vecino not in visitados and peso < peso_minimo and infeccion <= prob_infeccion:
                    estados[vecino] = "infectado"
                    arista_minima = (nodo, vecino)
                    peso_minimo = peso
        
        if arista_minima:
            visitados.add(arista_minima[1])
        
        pasos.append(estados.copy())

    return pasos

# =========================
# Función para dibujar el grafo
# =========================
def dibujar_grafo(G, estados):
    colores = ["red" if estados[n] == "infectado" else "green" for n in G.nodes]
    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color=colores, edge_color="gray", ax=ax)
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    return fig

# =========================
# App con Streamlit
# =========================
st.title("Simulador de Contagio en Grafos - Conexiones Personalizadas")

# Parámetros
nodos_lista = list("ABCDEFGHIJ")
prob_infeccion = st.slider("Probabilidad de infección (%)", 0, 100, 40)
nodo_inicial = st.selectbox("Nodo inicial infectado", nodos_lista)

# Selección de aristas
st.subheader("Selecciona las conexiones y sus pesos")
pares_posibles = list(itertools.combinations(nodos_lista, 2))
nodos_conectados = []

for n1, n2 in pares_posibles:
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        conectado = st.checkbox(f"{n1} - {n2}", key=f"{n1}{n2}")
    if conectado:
        with col2:
            peso = st.number_input(f"Peso {n1}-{n2}", min_value=1, max_value=10, value=1, key=f"peso_{n1}{n2}")
        nodos_conectados.append((n1, n2, peso))

# Construcción del grafo
G = nx.Graph()
G.add_nodes_from(nodos_lista)
for n1, n2, peso in nodos_conectados:
    G.add_edge(n1, n2, weight=peso)

# Simulación
if len(G.edges) > 0:
    pasos = simular_contagio(G, prob_infeccion, nodo_inicial)
    paso_elegido = st.slider("Paso de tiempo", 0, len(pasos) - 1, 0)
    st.write(f"**Paso {paso_elegido}**")
    fig = dibujar_grafo(G, pasos[paso_elegido])
    st.pyplot(fig)

    infectados = [n for n, estado in pasos[paso_elegido].items() if estado == "infectado"]
    st.write("**Nodos infectados:**", ", ".join(infectados))
else:
    st.warning("⚠️ No has creado ninguna conexión entre nodos.")





######################################################################

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

# =========================
# Estilos
# =========================
st.markdown("""
<style>
.titulo-centrado {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# =========================
# Simulación del contagio
# =========================
def simular_contagio(G, prob_infeccion, nodo_inicial):
    estados = {n: "sano" for n in G.nodes}
    estados[nodo_inicial] = "infectado"
    
    pasos = []
    pasos.append(estados.copy())

    visitados = set([nodo_inicial])
    aristas_totales = list(G.edges(data=True))

    for _ in range(len(G.edges) + 1):
        arista_minima = None
        peso_minimo = float("inf")

        for nodo in visitados:
            for vecino, datos in G[nodo].items():
                peso = datos["weight"]
                infeccion = random.randint(0, 100)
                if vecino not in visitados and peso < peso_minimo and infeccion <= prob_infeccion:
                    estados[vecino] = "infectado"
                    arista_minima = (nodo, vecino)
                    peso_minimo = peso
        
        if arista_minima:
            visitados.add(arista_minima[1])
        
        pasos.append(estados.copy())

    return pasos

# =========================
# Función para dibujar el grafo
# =========================
def dibujar_grafo(G, estados):
    colores = ["red" if estados[n] == "infectado" else "green" for n in G.nodes]
    pos = nx.spring_layout(G, seed=42)  # disposición fija para que no cambie
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color=colores, edge_color="gray", ax=ax)
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    return fig

# =========================
# App con Streamlit
# =========================
st.markdown("<h1 class='titulo-centrado'>Simulador de Contagio</h1>", unsafe_allow_html=True)

st.set_page_config(layout="wide")
col1, col2 = st.columns([2, 1])

with col2:
    st.subheader("Configuración del Grafo")

    # Parámetros
    nodos_lista = list("ABCDEFGHIJ")
    

    prob_infeccion = st.slider("Probabilidad de infección (%)", 0, 100, 40)
    nodo_inicial = st.selectbox("Nodo inicial infectado", nodos_lista)

    nodos_conectados = [("A", "H", 2), ("A", "E", 4), ("A", "F", 5), ("A", "B", 3),
                        ("F", "G", 4), ("F", "D", 1), ("D", "C", 3), ("B", "J", 3)]

    # Construcción del grafo
    G = nx.Graph()
    G.add_nodes_from(nodos_lista)
    for n1, n2, peso in nodos_conectados:
        G.add_edge(n1, n2, weight=peso)

    # Simulación
    pasos = simular_contagio(G, prob_infeccion, nodo_inicial)

    # Mostrar pasos
    paso_elegido = st.slider("Paso de tiempo", 0, len(pasos) - 1, 0)
    st.write(f"**Paso {paso_elegido}**")

with col1:
    st.subheader("Grafo")
    fig = dibujar_grafo(G, pasos[paso_elegido])
    st.pyplot(fig)

    # Mostrar lista de infectados
    infectados = [n for n, estado in pasos[paso_elegido].items() if estado == "infectado"]
    st.write("**Nodos infectados:**", ", ".join(infectados))
