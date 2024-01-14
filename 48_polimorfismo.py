class Animal:
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"
    
def interactuar_con_animal(animal):
    return animal.hacer_sonido()

mi_perro = Perro()
mi_gato = Gato()
print(mi_perro.hacer_sonido())
resultado_perro = interactuar_con_animal(mi_perro)
resultado_gato = interactuar_con_animal(mi_gato)
print(resultado_perro)
print(resultado_gato)