import os


def existe_carpeta(ruta):
    if os.path.exists(ruta):
        return True
    else:
        return False


directorio_actual = os.getcwd()
print(f'El directorio actual es {directorio_actual}')
# crear carpeta
nueva_carpeta = input("Dime el nombre de la carpeta nueva -> ")
ruta_completa = os.path.join(directorio_actual, nueva_carpeta)
print(ruta_completa)
if existe_carpeta(ruta_completa):
    print("La carpeta ya existe")
else:
    os.mkdir(ruta_completa)
    print("Carpeta creada")
# eliminar carpeta
eliminar_carpeta = input("Dime el nombre de la carpeta a eliminar -> ")
ruta_completa = os.path.join(directorio_actual, eliminar_carpeta)
if existe_carpeta(ruta_completa):
    print("Carpeta borrada")
    os.rmdir(ruta_completa)
else:
    print("La carpeta no existe, no podemos borrarla")

# listar
directorio = os.path.join(directorio_actual, 'carpeta02')
contenido = os.listdir(path=directorio)
print(contenido)

# recorrer directorio
directorio = os.getcwd()
with os.scandir(path=directorio) as elem:
    print(elem)
    for elemento in elem:
        print(elemento.name)
        if elemento.is_file():
            print(f'{elemento} es un archivo')
        elif elemento.is_dir():
            print(f'{elemento} es una carpeta')
