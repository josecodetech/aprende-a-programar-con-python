# clase padre
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def describir(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
# clase hija
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color
    def describir_coche(self):
        return f"{self.describir()}, Color: {self.color}"
# instanciamos la clase
mi_coche = Coche("Toyota","Corolla","Rojo")
# acceder a metodos y atributos
print(mi_coche.describir_coche())
print(mi_coche.describir())
print(mi_coche.marca)
