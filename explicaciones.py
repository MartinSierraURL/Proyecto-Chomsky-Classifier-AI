"""Modulo para generar explicaciones de cada tipo de gramatica segun Chomsky."""

def explicar_clasificacion(tipo, detalles):
    """Devuelve una explicacion segun el tipo detectado."""
    if tipo == 3:
        return (
            "La gramatica es de Tipo 3 (Regular).\n"
            "Todas las producciones tienen la forma A -> aB o A -> a.\n"
            "Esto significa que el lenguaje generado puede ser reconocido por un automata finito.\n"
            "Las gramaticas regulares describen lenguajes simples, como secuencias o patrones regulares."
        )

    elif tipo == 2:
        return (
            "La gramatica es de Tipo 2 (Libre de contexto).\n"
            "Cada produccion tiene un solo no terminal a la izquierda (A -> α).\n"
            "Este tipo de gramatica puede ser procesada por un automata de pila.\n"
            "Es comun en lenguajes de programacion y expresiones anidadas, como parentesis balanceados."
        )

    elif tipo == 1:
        return (
            "La gramatica es de Tipo 1 (Sensible al contexto).\n"
            "Todas las producciones cumplen que |lado izquierdo| <= |lado derecho|.\n"
            "Esto significa que el lenguaje necesita contexto para ser reconocido.\n"
            "Es mas potente que las libres de contexto, pero menos que las de tipo 0."
        )

    else:
        return (
            "La gramatica es de Tipo 0 (Recursivamente enumerable).\n"
            "No cumple las restricciones de los tipos anteriores.\n"
            "Estas gramaticas son las mas generales y pueden generar cualquier lenguaje que una maquina de Turing pueda reconocer.\n"
            "Sin embargo, no todos los problemas asociados a este tipo de gramaticas son decidibles."
        )
