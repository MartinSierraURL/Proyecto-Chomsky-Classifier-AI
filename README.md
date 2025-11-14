# Proyecto-Chomsky-Classifier-AI
El Chomsky Classifier AI es un agente inteligente capaz de analizar una gramática formal o un autómata y determinar automáticamente a qué tipo pertenece dentro de la Jerarquía de Chomsky (Tipo 0, 1, 2 o 3).


Proyecto-Chomsky-Classifier-AI

El proyecto Chomsky Classifier AI es una aplicación con interfaz gráfica desarrollada en Python utilizando customtkinter.
Permite analizar una gramática formal, clasificarla dentro de la jerarquía de Chomsky (Tipos 0, 1, 2 o 3) y generar reportes, ejemplos y visualizaciones.

Este proyecto incluye un sistema modular que separa el análisis, la clasificación, las explicaciones, la generación de ejemplos y la interfaz gráfica.

Características principales

Interfaz gráfica moderna creada con customtkinter.

Clasificación automática del tipo de gramática según la jerarquía de Chomsky.

Análisis sintáctico de reglas para validar su estructura.

Generación de ejemplos automáticos de gramáticas de distintos tipos.

Explicaciones paso a paso del proceso de clasificación.

Visualización de la gramática en una ventana adicional.

Exportación a PDF del análisis realizado (si ReportLab está instalado).

Comparación entre dos gramáticas para verificar si son equivalentes.

Funciona sin necesidad de instalar programas externos como Graphviz

===ESTRUCTURA DEL PROYECTO===  

Proyecto-Chomsky-Classifier-AI/

├── analizador_gramatica.py      → Analiza reglas de gramática

├── clasificador.py              → Clasifica según Chomsky

├── explicaciones.py             → Explicaciones del tipo detectado

├── generador.py                 → Genera gramáticas de ejemplo

├── interfaz_grafica.py          → Archivo principal de la interfaz GUI

├── reporte.py                   → Generación de reportes PDF

├── utilidades.py                → Funciones extra (comparaciones, etc.)

├── README.md                    → Documento actual

└── gramatica_diagrama.png       → Imagen generada si se usa visualizador

