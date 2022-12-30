class Coche:
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def arrancar(self):
        print("Estoy en marcha")


class Autobus(Coche):
    def pasajeros(self):
        print("El autobus esta vacio")


miCoche = Coche("rojo", 5)
print(miCoche)
print(miCoche.color)
print(miCoche.puertas)
miCoche.arrancar()

otroCoche = Coche('verde', 3)
print(otroCoche)
print(otroCoche.color)
print(otroCoche.puertas)
otroCoche.arrancar()


miAutobus = Autobus("azul", 3)
print(miAutobus)
print(miAutobus.color)
print(miAutobus.puertas)
miAutobus.arrancar()
miAutobus.pasajeros()
