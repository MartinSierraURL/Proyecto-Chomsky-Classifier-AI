"""Modulo de funciones extra para el Clasificador Chomsky AI.
Incluye comparacion de dos gramaticas por generacion heuristica de cadenas.
"""

from analizador_gramatica import analizar_gramatica_texto


def generar_cadenas_desde_cfg(gramatica, longitud_max=6, cantidad_max=200):
    """Genera cadenas a partir de una gramatica libre de contexto simple."""
    producciones = gramatica['producciones']
    reglas = {}

    for izq, der in producciones:
        lado_izq = ''.join(izq)
        lado_der = ''.join(der)
        reglas.setdefault(lado_izq, []).append(lado_der)

    inicio = 'S'
    resultados = set()
    pendientes = [inicio]

    while pendientes and len(resultados) < cantidad_max:
        actual = pendientes.pop(0)

        # Si no hay no terminales, agregar al resultado
        if all(not c.isupper() for c in actual):
            if len(actual) <= longitud_max:
                resultados.add(actual)
            continue

        # Expandir el primer no terminal
        for i, ch in enumerate(actual):
            if ch.isupper():
                A = ch
                antes = actual[:i]
                despues = actual[i + 1:]
                for produccion in reglas.get(A, []):
                    nueva = antes + produccion + despues
                    if len(nueva) <= longitud_max:
                        pendientes.append(nueva)
                break

    return sorted(resultados)


def comparar_gramaticas(texto1, texto2, profundidad=5):
    """Compara dos gramaticas generando cadenas hasta cierta longitud."""
    g1 = analizar_gramatica_texto(texto1)
    g2 = analizar_gramatica_texto(texto2)

    cadenas1 = generar_cadenas_desde_cfg(g1, longitud_max=profundidad)
    cadenas2 = generar_cadenas_desde_cfg(g2, longitud_max=profundidad)

    comun = set(cadenas1).intersection(cadenas2)

    resultado = []
    resultado.append("=== COMPARACION DE GRAMATICAS ===")
    resultado.append(f"Longitud maxima analizada: {profundidad}")
    resultado.append(f"Cadenas generadas por G1: {len(cadenas1)}")
    resultado.append(f"Cadenas generadas por G2: {len(cadenas2)}")
    resultado.append(f"Cadenas en comun: {len(comun)}")

    if comun:
        resultado.append("Ejemplos de cadenas comunes: " + ", ".join(list(comun)[:5]))
    else:
        resultado.append("No se encontraron cadenas comunes en esa profundidad.")

    return "\n".join(resultado)
