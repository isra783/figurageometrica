class figura_geometrica():
    def __init__(self,ancho,alto ):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self.ancho

    @ancho.setter
    def ancho(self,valor):
        if valor <= 0 :
            raise ValueError('los valores a ingresar deben de ser mayores que 0')
        self.ancho = valor

    @property
    def alto(self):
        return self.alto
    @alto.setter
    def alto(self,valor):
        if valor <= 0 :
            raise ValueError('los valores a ingresar deben de ser mayores que 0')
        self.alto = valor


    def area(self):
        return self.ancho * self.alto


    def perimetro():
        pass

    def __str__(self):
        return f'la figura geometrica posee un dimendcion {self.ancho}ancho y {self.alto} alto '




