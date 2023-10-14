palabras = ["hola","mundo","python"]
mayusculas = []
for palabra in palabras:
    mayusculas.append(palabra.upper())
print(palabras)
print(mayusculas)
print("*"*30)
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)