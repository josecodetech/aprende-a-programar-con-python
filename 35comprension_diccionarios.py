# nuevo_diccionario = {clave: valor for elemento in secuencia}
numeros = [1,2,3,4,5]
diccionario_cuadrados = {num: num**2 for num in numeros}
print(numeros)
print(diccionario_cuadrados)

numeros = [1,2,3,4,5,6,7,8]
diccionario_pares = {num: num for num in numeros if num % 2 == 0}
print(diccionario_pares)

palabras = ["python", "con","josecodetech"]
diccionario_longitudes = {palabra: len(palabra) for palabra in palabras}
print(diccionario_longitudes)