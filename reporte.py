"""Modulo para generar reportes en PDF o TXT con los resultados del analisis."""
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    DISPONIBLE_REPORTLAB = True
except Exception:
    DISPONIBLE_REPORTLAB = False


def generar_reporte_pdf(gramatica, clasificacion, explicacion, ruta_salida="reporte.pdf"):
    texto = []
    texto.append("=== CLASIFICADOR CHOMSKY AI ===\n")
    texto.append("Reporte generado automaticamente.\n\n")

    tipo, detalle = clasificacion
    texto.append(f"TIPO DETECTADO: {tipo} - {detalle.get('resumen', '')}\n\n")

    texto.append("PRODUCCIONES:\n")
    for izq, der in gramatica['producciones']:
        lado_izq = ''.join(izq)
        lado_der = ''.join(der) if der else 'ε'
        texto.append(f"  {lado_izq} -> {lado_der}")
    texto.append("\n")

    texto.append("EXPLICACION:\n")
    texto.append(explicacion or "No hay explicacion disponible.\n")

    contenido = "\n".join(texto)

    if DISPONIBLE_REPORTLAB:
        try:
            pdf = canvas.Canvas(ruta_salida, pagesize=letter)
            ancho, alto = letter
            y = alto - 50
            for linea in contenido.split("\n"):
                pdf.drawString(50, y, linea)
                y -= 14
                if y < 50:
                    pdf.showPage()
                    y = alto - 50
            pdf.save()
            print(f"Reporte PDF generado: {ruta_salida}")
        except Exception as e:
            print("Error generando PDF:", e)
    else:
        # Si no esta reportlab, crea un archivo de texto
        ruta_txt = ruta_salida.replace(".pdf", ".txt")
        with open(ruta_txt, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"Reportlab no instalado. Se genero archivo de texto: {ruta_txt}")
