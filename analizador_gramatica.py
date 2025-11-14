"""Analizador de gramaticas formales en texto.
Formato por linea: LHS -> RHS1 | RHS2
Se permite usar '->' o '→'
"""
import re

PATRON_REGLA = re.compile(r"\s*(?P<izq>[^-→]+)\s*(?:->|→)\s*(?P<der>.+)")


def separar_simbolos(cadena: str):
    """Divide una cadena en simbolos terminales y no terminales."""
    cadena = cadena.strip()
    if ' ' in cadena:
        return cadena.split()
    else:
        simbolos = []
        i = 0
        while i < len(cadena):
            c = cadena[i]
            if c.isupper():
                simbolos.append(c)
                i += 1
            else:
                j = i
                while j < len(cadena) and not cadena[j].isupper():
                    j += 1
                simbolos.append(cadena[i:j])
                i = j
        return [s for s in simbolos if s != '']

def analizar_gramatica_texto(texto: str):
    """Convierte un texto con reglas en una estructura interna."""
    producciones = []
    no_terminales = set()
    terminales = set()

    lineas = texto.splitlines()
    for linea in lineas:
        linea = linea.strip()
        if not linea or linea.startswith('#'):
            continue

        m = PATRON_REGLA.match(linea)
        if not m:
            continue

        lado_izq = m.group('izq').strip()
        lado_der = m.group('der').strip()
        simbolos_izq = separar_simbolos(lado_izq)
        no_terminales.update([s for s in simbolos_izq if s.isupper()])

        partes = [p.strip() for p in re.split(r'\s*\|\s*', lado_der)]
        for p in partes:
            simbolos_der = separar_simbolos(p)
            producciones.append((simbolos_izq, simbolos_der))
            for s in simbolos_der:
                if s.isupper():
                    no_terminales.add(s)
                else:
                    if s != 'ε' and s != '':
                        terminales.add(s)

    return {
        'producciones': producciones,
        'no_terminales': sorted(no_terminales),
        'terminales': sorted(terminales)
    }

