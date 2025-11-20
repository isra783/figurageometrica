from figura_geo import figura_geometrica

class cuadrado(figura_geometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return self.ancho * 4

    def __str__(self):
        return f"Cuadrado(lado={self.ancho})"


