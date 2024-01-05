class Hucha:
    def __init__(self, importe_inicial=0):
        self.__importe = importe_inicial
    def obtener_importe(self):
        return self.__importe
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__importe += cantidad
        else:
            print("La cantidad ingresada debe ser mayor que cero")
    def sacar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__importe:
            self.__importe -= cantidad
        else:
            print("La cantidad ingresada debe ser mayor que cero y no puede exceder el importe actual")
    def mostrar_importe(self):
        return f"El importe actual en la hucha es: {self.__importe}"
    
mi_hucha = Hucha(100)
mi_hucha.ingresar(50)
print(mi_hucha.mostrar_importe())
mi_hucha.sacar(100)
print(mi_hucha.mostrar_importe())
# print(mi_hucha.__importe) esto dara error
print(mi_hucha.obtener_importe())
