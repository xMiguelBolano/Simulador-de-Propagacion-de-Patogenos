import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools
import time

# =========================
# Estilos
# =========================
st.markdown("""
<style>
.titulo {
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
    peso_total = 0

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
            peso_total += peso_minimo
        
        pasos.append(estados.copy())

    return pasos, peso_total


# =========================
# Layout fijo global
# =========================
NODOS = list("ABCDEFGHIJ")
POSICIONES = nx.spring_layout(NODOS, seed=242)

# =========================
# Función para dibujar el grafo
# =========================
def dibujar_grafo(G, estados):
    colores = ["red" if estados[n] == "infectado" else "green" for n in G.nodes]
    
    fig, ax = plt.subplots()
    nx.draw(
        G, POSICIONES, with_labels=True, node_color=colores,
        edge_color="gray", ax=ax
    )
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, POSICIONES, edge_labels=etiquetas)
    return fig

# =========================
# App con Streamlit
# =========================
st.set_page_config(layout="wide")
st.markdown("<h1 class='titulo'>Simulador de Contagio</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col2:
    st.subheader("Configuración del Grafo")

    # Parámetros
    prob_infeccion = st.slider("Probabilidad de infección (%)", 0, 100, 40)
    nodo_inicial = st.selectbox("Nodo inicial infectado", NODOS)

    # Selección de aristas
    st.subheader("Selecciona las conexiones y sus pesos")
    pares_posibles = list(itertools.combinations(NODOS, 2))
    nodos_conectados = []

    # Crear 3 columnas globales
    col_a, col_b, col_c = st.columns(3)
    columnas = [col_a, col_b, col_c]

    for idx, (n1, n2) in enumerate(pares_posibles):
        col = columnas[idx % 3]
        with col:
            conectado = st.checkbox(f"{n1} -- {n2}", key=f"{n1}{n2}")
            if conectado:
                peso = st.number_input(
                    f"Peso {n1}-{n2}", 
                    min_value=1, 
                    max_value=10, 
                    value=1, 
                    key=f"peso_{n1}{n2}"
                )
                nodos_conectados.append((n1, n2, peso))

            
    # Construcción del grafo
    G = nx.Graph()
    G.add_nodes_from(NODOS)
    for n1, n2, peso in nodos_conectados:
        G.add_edge(n1, n2, weight=peso)

with col1:
    # Guardar simulación en session_state
    if "simulacion" not in st.session_state or st.button("🔄 Re-simular"):
        if len(G.edges) > 0:
            pasos, peso_total = simular_contagio(G, prob_infeccion, nodo_inicial)
            st.session_state.simulacion = pasos
            st.session_state.peso_total = peso_total
        else:
            st.session_state.simulacion = None
            st.session_state.peso_total = 0


    # Control de animación
    auto_play = st.checkbox("▶️ Reproducir automáticamente", value=False)
    if auto_play:
        velocidad = st.slider("Velocidad (segundos por día)", 0.1, 2.0, 0.5, step=0.1)

    if st.session_state.get("simulacion"):
        pasos = st.session_state.simulacion

        if auto_play:
            placeholder = st.empty()
            for dia, estado in enumerate(pasos):
                with placeholder.container():
                    st.write(f"**Día {dia}**")
                    fig = dibujar_grafo(G, estado)
                    st.pyplot(fig)
                    infectados = [n for n, e in estado.items() if e == "infectado"]
                    st.write("**Nodos infectados:**", ", ".join(infectados))
                time.sleep(velocidad)
        else:
            paso_elegido = st.slider(f"Días de propagación (max {len(pasos)-1})", 0, len(pasos) - 1, 0)
            st.write(f"**Día {paso_elegido}**")
            fig = dibujar_grafo(G, pasos[paso_elegido])
            st.pyplot(fig)

            infectados = [n for n, estado in pasos[paso_elegido].items() if estado == "infectado"]
            st.write("**Nodos infectados:**", ", ".join(infectados))

        st.write("**Peso total recorrido por el patógeno:**", st.session_state.peso_total)
    else:
        st.warning("⚠️ No has creado ninguna conexión entre nodos.")
