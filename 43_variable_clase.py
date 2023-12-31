class MiClase:
    variable_de_clase = 0
    def __init__(self, valor):
        self.valor = valor

print(MiClase.variable_de_clase)
objeto1 = MiClase(1)
objeto2 = MiClase(2)
print(objeto1.variable_de_clase)
print(objeto2.variable_de_clase)
print(objeto1.valor)