#!/usr/bin/env python3
"""Consola principal para Clasificador de Chomsky"""

from analizador_gramatica import analizar_gramatica_texto
from clasificador import clasificar_gramatica, nombre_tipo
from explicaciones import explicar_clasificacion
from generador import generar_ejemplo
from visualizador import visualizar_gramatica
from reporte import generar_reporte_pdf
from utilidades import comparar_gramaticas
import sys

MENU = '''
==============================
   CLASIFICADOR CHOMSKY AI
==============================
1) Analizar gramatica (pegar reglas)
2) Cargar ejemplo desde archivo
3) Generar ejemplo aleatorio
4) Explicacion paso a paso
5) Visualizar gramatica (texto)
6) Exportar reporte (PDF)
7) Comparar dos gramaticas
8) Salir
------------------------------
Selecciona una opcion: '''

ultima_gramatica = None
ultima_clasificacion = None
ultima_explicacion = None


def leer_gramatica_por_consola():
    print("Escribe la gramatica linea por linea. Deja una linea vacia para terminar:")
    lineas = []
    while True:
        try:
            linea = input().strip()
        except EOFError:
            break
        if not linea:
            break
        lineas.append(linea)
    return "\n".join(lineas)


def main():
    global ultima_gramatica, ultima_clasificacion, ultima_explicacion

    while True:
        opcion = input(MENU).strip()

        if opcion == '1':
            texto = leer_gramatica_por_consola()
            gramatica = analizar_gramatica_texto(texto)
            ultima_gramatica = gramatica
            tipo, detalle = clasificar_gramatica(gramatica)
            ultima_clasificacion = (tipo, detalle)
            print(f"\nResultado: {nombre_tipo(tipo)}")
            print(detalle['resumen'])

        elif opcion == '2':
            ruta = input("Ruta del archivo de texto con la gramatica: ").strip()
            try:
                with open(ruta, 'r', encoding='utf-8') as f:
                    texto = f.read()
                gramatica = analizar_gramatica_texto(texto)
                ultima_gramatica = gramatica
                tipo, detalle = clasificar_gramatica(gramatica)
                ultima_clasificacion = (tipo, detalle)
                print(f"\nResultado: {nombre_tipo(tipo)}")
                print(detalle['resumen'])
            except Exception as e:
                print("Error leyendo el archivo:", e)

        elif opcion == '3':
            tipo = input("Tipo a generar (0,1,2,3) o ENTER para aleatorio: ").strip()
            try:
                g = generar_ejemplo(int(tipo)) if tipo else generar_ejemplo()
            except Exception:
                g = generar_ejemplo()
            print("\nGramatica generada:\n")
            print(g)
            gramatica = analizar_gramatica_texto(g)
            ultima_gramatica = gramatica
            tipo, detalle = clasificar_gramatica(gramatica)
            ultima_clasificacion = (tipo, detalle)
            print(f"\nResultado: {nombre_tipo(tipo)}")

        elif opcion == '4':
            if not ultima_gramatica:
                print("No hay gramatica analizada aun.")
                continue
            explicacion = explicar_clasificacion(ultima_gramatica)
            ultima_explicacion = explicacion
            print(explicacion)

        elif opcion == '5':
            if not ultima_gramatica:
                print("No hay gramatica analizada aun.")
                continue
            visualizar_gramatica(ultima_gramatica)

        elif opcion == '6':
            if not ultima_gramatica or not ultima_clasificacion:
                print("No hay gramatica analizada aun.")
                continue
            salida = input("Nombre del archivo PDF (ej: reporte.pdf): ").strip() or 'reporte.pdf'
            generar_reporte_pdf(ultima_gramatica, ultima_clasificacion, ultima_explicacion, salida)
            print(f"Reporte generado: {salida}")

        elif opcion == '7':
            print("Pega la primera gramatica (termina con linea vacia):")
            g1 = leer_gramatica_por_consola()
            print("Pega la segunda gramatica (termina con linea vacia):")
            g2 = leer_gramatica_por_consola()
            n = input("Profundidad maxima para comparar (ej: 5): ").strip()
            try:
                n = int(n)
            except Exception:
                n = 5
            resultado = comparar_gramaticas(g1, g2, n)
            print(resultado)

        elif opcion == '8':
            print("Saliendo del programa...")
            sys.exit(0)

        else:
            print("Opcion no valida, intenta de nuevo.")


if __name__ == '__main__':
    main()
