def aplicar_funcion(func, valor):
    return func(valor)

def doblar(num):
    return num * 2

resultado = aplicar_funcion(doblar, 5)
print("Resultado:", resultado)
