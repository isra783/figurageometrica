Este proyecto implementa un sistema de clases usando Programación Orientada a Objetos (POO) en Python.
El taller aplica encapsulamiento, herencia, polimorfismo y sobrescritura de métodos utilizando figuras geométricas.
Descripción de Cada Clase
 FiguraGeometrica

Clase base del proyecto.
Incluye:

Atributos privados _ancho y _alto.

Encapsulamiento con @property y @setter.

Validaciones para impedir valores negativos o cero.

Método area() implementado.

Método perimetro() sin implementar (obligatorio sobrescribir).

Método __str__() que imprime sus dimensiones.

 Cuadrado

Hereda de FiguraGeometrica.

Recibe solo un valor (lado) en su constructor.

Llama al constructor del padre usando super().

Sobrescribe:

area()

perimetro()

__str__()

 Rectangulo

Hereda de FiguraGeometrica.

Constructor recibe ancho y alto.

Sobrescribe:

area()

perimetro()

__str__()

 main.py – Programa Principal

El programa:

Crea dos cuadrados y dos rectángulos.

Muestra:

Área

Perímetro

Valores de los atributos

Impresión del objeto

Modifica valores válidos.

Demuestra validación de errores usando try/except.

Usa funciones polimórficas:

 sumar_areas(figuras: list)

Suma las áreas de todas las figuras de la lista sin importar si son cuadrados o rectángulos.

 sumar_perimetros(figuras: list)

Suma los perímetros de todas las figuras.

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/849f1cb2-682a-4a49-ba59-4498d2efab41" />
