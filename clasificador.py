"""Modulo de clasificacion segun la Jerarquia de Chomsky.
Devuelve (numero_tipo, detalles)
"""

def es_lineal_derecha(producciones):
    """Verifica si todas las producciones son del tipo A -> aB o A -> a"""
    for izq, der in producciones:
        if len(izq) != 1 or not izq[0].isupper():
            return False

        if len(der) == 0 or (len(der) == 1 and not der[0].isupper()):
            continue

        if len(der) == 2 and not der[0].isupper() and der[1].isupper():
            continue

        if len(der) >= 2 and der[-1].isupper() and all(not s.isupper() for s in der[:-1]):
            continue

        return False
    return True


def es_lineal_izquierda(producciones):
    """Verifica si todas las producciones son del tipo A -> Ba o A -> a"""
    for izq, der in producciones:
        if len(izq) != 1 or not izq[0].isupper():
            return False

        if len(der) == 0 or (len(der) == 1 and not der[0].isupper()):
            continue

        if len(der) == 2 and der[0].isupper() and not der[1].isupper():
            continue

        if len(der) >= 2 and der[0].isupper() and all(not s.isupper() for s in der[1:]):
            continue

        return False
    return True


def es_libre_contexto(producciones):
    """Verifica si todas las producciones tienen un solo no terminal a la izquierda."""
    for izq, _ in producciones:
        if len(izq) != 1 or not izq[0].isupper():
            return False
    return True


def es_sensible_contexto(producciones):
    """Verifica si todas cumplen |LHS| <= |RHS|"""
    for izq, der in producciones:
        if len(izq) > len(der):
            return False
    return True


def nombre_tipo(num):
    """Devuelve el nombre del tipo de lenguaje."""
    return {
        0: 'Tipo 0 (Recursivamente enumerable)',
        1: 'Tipo 1 (Sensible al contexto)',
        2: 'Tipo 2 (Libre de contexto)',
        3: 'Tipo 3 (Regular)'
    }[num]


def clasificar_gramatica(analizada):
    """Clasifica la gramatica en el tipo mas restrictivo posible."""
    producciones = analizada['producciones']
    detalles = {'verificaciones': {}, 'resumen': ''}

    derecha = es_lineal_derecha(producciones)
    izquierda = es_lineal_izquierda(producciones)
    detalles['verificaciones']['lineal_derecha'] = derecha
    detalles['verificaciones']['lineal_izquierda'] = izquierda
    if derecha or izquierda:
        detalles['resumen'] = 'Todas las producciones cumplen la forma de gramatica regular (linealidad).'
        return 3, detalles

    libre = es_libre_contexto(producciones)
    detalles['verificaciones']['libre_contexto'] = libre
    if libre:
        detalles['resumen'] = 'Cada produccion tiene un solo no terminal a la izquierda: Libre de contexto (Tipo 2).'
        return 2, detalles

    sensible = es_sensible_contexto(producciones)
    detalles['verificaciones']['sensible_contexto'] = sensible
    if sensible:
        detalles['resumen'] = 'Todas las producciones cumplen |LHS| <= |RHS|: Sensible al contexto (Tipo 1).'
        return 1, detalles

    detalles['resumen'] = 'No cumple las restricciones anteriores: Recursivamente enumerable (Tipo 0).'
    return 0, detalles
