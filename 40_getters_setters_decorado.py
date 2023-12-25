class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    # obtener nombre
    @property
    def nombre(self):
        return self._nombre
    # dar valor a nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad no puede ser negativa")
# crear objeto, instanciar la clase
persona1 = Persona("Juan", 28)
print("Nombre: ",persona1.nombre)
persona1.nombre = "Karla"
# persona1.__nombre = "Jose"
print("Nombre: ",persona1.nombre)
persona1.edad = 30
print("Edad: ",persona1.edad)