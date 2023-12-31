class Persona:
    contador = 0 # variable clase
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1 # incrementa al crear objeto o instancia de clase
        
persona1 = Persona("Juan")
persona2 = Persona("Karla")
persona3 = Persona("Carlos")

# valor contador
print("Numero de personas : ", Persona.contador)
