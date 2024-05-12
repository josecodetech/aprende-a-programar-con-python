def validar(funcion):
    def envolver(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Solo se permiten numeros enteros")
        return funcion(*args, **kwargs)
    return envolver
@validar
def suma(a,b):
    return a + b

print(suma(5,3))
# llamada invalida
print(suma(4, "5"))