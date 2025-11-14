import customtkinter as ctk
from tkinter import messagebox
from analizador_gramatica import analizar_gramatica_texto
from clasificador import clasificar_gramatica, nombre_tipo
from explicaciones import explicar_clasificacion
from generador import generar_ejemplo
from reporte import generar_reporte_pdf
from visualizador import visualizar_gramatica
from utilidades import comparar_gramaticas


# Configuracion base
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Clasificador Chomsky AI")
ventana.geometry("900x600")

# ---- Funciones de interfaz ----
def accion_analizar():
    texto = entrada_gramatica.get("1.0", "end").strip()
    if not texto:
        messagebox.showwarning("Aviso", "Por favor ingresa una gramatica para analizar.")
        return

    gramatica = analizar_gramatica_texto(texto)
    tipo, detalles = clasificar_gramatica(gramatica)
    explicacion = explicar_clasificacion(tipo, detalles)
    salida_texto.delete("1.0", "end")
    salida_texto.insert("end", f"TIPO DETECTADO: {nombre_tipo(tipo)}\n\n")
    salida_texto.insert("end", f"{detalles['resumen']}\n\n")
    salida_texto.insert("end", explicacion)


def accion_generar_ejemplo():
    tipo = combo_tipo.get()
    if tipo == "":
        tipo = 3
    else:
        tipo = int(tipo.split()[1])
    texto = generar_ejemplo(tipo)
    entrada_gramatica.delete("1.0", "end")
    entrada_gramatica.insert("end", texto)


def accion_visualizar():
    texto = entrada_gramatica.get("1.0", "end").strip()
    if not texto:
        messagebox.showwarning("Aviso", "Primero ingresa o genera una gramatica.")
        return
    gramatica = analizar_gramatica_texto(texto)
    visualizar_gramatica(gramatica)


def accion_reporte():
    texto = entrada_gramatica.get("1.0", "end").strip()
    if not texto:
        messagebox.showwarning("Aviso", "Primero analiza una gramatica antes de generar el reporte.")
        return
    gramatica = analizar_gramatica_texto(texto)
    tipo, detalles = clasificar_gramatica(gramatica)
    explicacion = explicar_clasificacion(tipo, detalles)
    generar_reporte_pdf(gramatica, (tipo, detalles), explicacion)
    messagebox.showinfo("Exito", "Reporte generado correctamente (reporte.pdf).")


def accion_comparar():
    ventana_comparar = ctk.CTkToplevel(ventana)
    ventana_comparar.title("Comparar Gramaticas")
    ventana_comparar.geometry("700x500")

    lbl1 = ctk.CTkLabel(ventana_comparar, text="Gramatica 1:")
    lbl1.pack(pady=5)
    entrada1 = ctk.CTkTextbox(ventana_comparar, width=600, height=150)
    entrada1.pack(pady=5)

    lbl2 = ctk.CTkLabel(ventana_comparar, text="Gramatica 2:")
    lbl2.pack(pady=5)
    entrada2 = ctk.CTkTextbox(ventana_comparar, width=600, height=150)
    entrada2.pack(pady=5)

    def ejecutar_comparacion():
        g1 = entrada1.get("1.0", "end").strip()
        g2 = entrada2.get("1.0", "end").strip()
        if not g1 or not g2:
            messagebox.showwarning("Aviso", "Debes ingresar ambas gramaticas.")
            return
        resultado = comparar_gramaticas(g1, g2)
        messagebox.showinfo("Resultado", resultado)

    btn_comp = ctk.CTkButton(ventana_comparar, text="Comparar", command=ejecutar_comparacion)
    btn_comp.pack(pady=10)


# ---- INTERFAZ ----
frame_izq = ctk.CTkFrame(ventana, width=300)
frame_izq.pack(side="left", fill="y", padx=10, pady=10)

frame_der = ctk.CTkFrame(ventana)
frame_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Área de entrada
lbl_entrada = ctk.CTkLabel(frame_izq, text="Ingrese o genere una gramatica:")
lbl_entrada.pack(pady=5)
entrada_gramatica = ctk.CTkTextbox(frame_izq, width=250, height=250)
entrada_gramatica.pack(pady=5)

combo_tipo = ctk.CTkComboBox(frame_izq, values=["Tipo 0", "Tipo 1", "Tipo 2", "Tipo 3"])
combo_tipo.set("Tipo 3")
combo_tipo.pack(pady=5)

btn_analizar = ctk.CTkButton(frame_izq, text="Analizar", command=accion_analizar)
btn_analizar.pack(pady=5)

btn_generar = ctk.CTkButton(frame_izq, text="Generar ejemplo", command=accion_generar_ejemplo)
btn_generar.pack(pady=5)

btn_visualizar = ctk.CTkButton(frame_izq, text="Visualizar", command=accion_visualizar)
btn_visualizar.pack(pady=5)

btn_reporte = ctk.CTkButton(frame_izq, text="Exportar reporte", command=accion_reporte)
btn_reporte.pack(pady=5)

btn_comparar = ctk.CTkButton(frame_izq, text="Comparar gramaticas", command=accion_comparar)
btn_comparar.pack(pady=5)

# Área de salida
lbl_salida = ctk.CTkLabel(frame_der, text="Resultado del analisis:")
lbl_salida.pack(pady=5)
salida_texto = ctk.CTkTextbox(frame_der, width=550, height=500)
salida_texto.pack(pady=10)
print("Iniciando interfaz grafica...")

ventana.mainloop()