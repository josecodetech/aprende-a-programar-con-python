class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
class Transporte:
    def __init__(self, capacidad):
        self.capacidad = capacidad
class Camion(Vehiculo, Transporte):
    def __init__(self, marca, modelo, capacidad, carga):
        Vehiculo.__init__(self, marca, modelo)
        Transporte.__init__(self, capacidad)
        self.carga = carga
    def describir_camion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Capacidad: {self.capacidad}, Carga: {self.carga}"
mi_camion = Camion("Volvo", "VNL", 15000, "Madera")
print(mi_camion.describir_camion())
   