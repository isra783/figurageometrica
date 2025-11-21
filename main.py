from cuadrado import cuadrado
from rectangulo import rectangulo

def sumar_areas(figuras):
    return sum(figura.area() for figura in figuras)

def sumar_perimetros(figuras):
    return sum(figura.perimetro() for figura in figuras)

if __name__ == "__main__":
    # Crear objetos válidos
    c1 = cuadrado(4)
    c2 = cuadrado(7)
    r1 = rectangulo(5, 10)
    r2 = rectangulo(2, 10)

    print(c1)
    print("Área:", c1.area(), "Perímetro:", c1.perimetro())

    print(r1)
    print("Área:", r1.area(), "Perímetro:", r1.perimetro())

    # Demostrar validación

    try:
        cuadrado(-5)
    except ValueError as e:
        print("Error demostrado:", e)


    figuras = [c1, c2, r1, r2]

    print("Suma total de áreas:", sumar_areas(figuras))
    print("Suma total de perímetros:", sumar_perimetros(figuras))





