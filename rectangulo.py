from figura_geo import figura_geometrica

class rectangulo(figura_geometrica):
    def __init__(self,lado,ancho):
        super().__init__(ancho,alto)

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def __str__(self):
        return f"el rectangulo tiene de ancho{self.ancho} y de  alto{self.alto}"
