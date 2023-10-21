# map(funcion, secuencia)
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x: x**2,numeros))
print(numeros)
print(cuadrados)
print("-"*60)
# sin map
cuadrados = []
for numero in numeros:
    cuadrados.append(numero**2)
print(numeros)
print(cuadrados)