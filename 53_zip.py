nombres = ['Juan','Maria','Carlos']
edades = [20, 25, 30]
combinado = zip(nombres, edades)
print(type(combinado))
combinado = list(combinado)
print(combinado)
print(type(combinado))
combinado = zip(nombres, edades)
for nombre, edad in combinado:
    print(nombre, " tiene ", edad, " años.")
nombres = ['Juan','Maria','Carlos']
edades = [20, 25, 30]  
alturas = [1.75, 1.60, 1.80]
combinado = zip(nombres, edades, alturas)
for nombre, edad, altura in combinado:
    print(nombre, " tiene ", edad, " años y mide ", altura, "mts.")  
combinado = zip(nombres, edades, alturas)
for persona in combinado:
    nombre, edad, altura = persona
    print(f"{nombre}, tiene {edad} años y {altura} de alto.")