"""Modulo que genera ejemplos de gramaticas para probar el sistema."""

def generar_ejemplo(tipo=3):
    """Devuelve un ejemplo de gramatica segun el tipo de Chomsky solicitado."""
    if tipo == 3:
        return (
            "# Gramatica regular (Tipo 3)\n"
            "S -> aA | bB\n"
            "A -> aS | bAA | a\n"
            "B -> bS | aBB | b"
        )

    elif tipo == 2:
        return (
            "# Gramatica libre de contexto (Tipo 2)\n"
            "S -> aSb | ab"
        )

    elif tipo == 1:
        return (
            "# Gramatica sensible al contexto (Tipo 1)\n"
            "S -> aABb\n"
            "A -> aA | a\n"
            "B -> Bb | b"
        )

    else:
        return (
            "# Gramatica recursivamente enumerable (Tipo 0)\n"
            "S -> aSb | SS | aAb\n"
            "A -> aA | b"
        )
