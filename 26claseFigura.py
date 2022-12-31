class Figura():
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        print("Medoto a definir en clases hijas")


class Cuadrado(Figura):
    def __init__(self, lado1, lado2=0):
        super().__init__(lado1, lado2)
        self.lado = lado1

    def area(self):
        area = self.lado ** 2
        print(f'El area del cuadrado es {area}')

    def perimetro(self):
        perimetro = 4*self.lado
        print(f'El perimetro del cuadrado es {perimetro}')


class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        super().__init__(lado1, lado2)
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        area = self.lado1 * self.lado2
        print(f'El area del rectangulo es {area}')

    def perimetro(self):
        perimetro = 2*self.lado1 + 2*self.lado2
        print(f'El perimetro del rectangulo es {perimetro}')


if __name__ == '__main__':
    cuadradito = Cuadrado(3)
    cuadradito.area()
    cuadradito.perimetro()
    rectangulo = Rectangulo(4, 8)
    rectangulo.area()
    rectangulo.perimetro()
