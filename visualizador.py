"""Modulo para mostrar o visualizar gramaticas.
Si esta instalada la libreria graphviz, genera una imagen con las producciones.
"""

try:
    import graphviz
    DISPONIBLE_GRAPHVIZ = True
except Exception:
    DISPONIBLE_GRAPHVIZ = False


def visualizar_gramatica(gramatica):
    """Muestra las producciones de la gramatica y genera imagen si es posible."""
    producciones = gramatica['producciones']

    print("\n=== PRODUCCIONES DE LA GRAMATICA ===")
    for izq, der in producciones:
        lado_izq = ''.join(izq)
        lado_der = ''.join(der) if der else 'ε'
        print(f"{lado_izq} -> {lado_der}")

    if DISPONIBLE_GRAPHVIZ:
        try:
            dot = graphviz.Digraph('gramatica')
            for i, (izq, der) in enumerate(producciones):
                nodo_izq = ''.join(izq)
                nodo_der = ''.join(der) if der else 'ε'
                dot.node(f"L{i}", nodo_izq)
                dot.node(f"R{i}", nodo_der)
                dot.edge(f"L{i}", f"R{i}")
            salida = "gramatica_diagrama"
            dot.render(salida, format="png", cleanup=True)
            print(f"\nImagen generada con exito: {salida}.png")
        except Exception as e:
            print("Error generando imagen con graphviz:", e)
    else:
        print("\n(Visualizacion grafica no disponible: instala la libreria 'graphviz' para generar imagenes)")
