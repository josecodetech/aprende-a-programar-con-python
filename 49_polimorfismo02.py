import math
class FiguraGeometrica:
    def calcular_area(self):
        pass
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio  
    def calcular_area(self):
        return math.pi * self.radio ** 2
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
def calcular_area_figura(figura):
    return figura.calcular_area()

circulo = Circulo(5)
rectangulo = Rectangulo(3, 4)
# rectangulo.calcular_area()
area_circulo = calcular_area_figura(circulo)
area_rectangulo = calcular_area_figura(rectangulo)
print(f"Area del circulo : {area_circulo:.2f}")
print(f"Area del rectangulo : {area_rectangulo:.2f}")
