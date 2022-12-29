fichero = open("archivo.txt", "r")
linea = fichero.readline()
print(f'Estoy leyendo la linea donde dice \'{linea}\'')
fichero.close()

fichero = open("archivo.txt", "r")
lineas = fichero.read()
print(f"Estoy leyendo todas las lineas -> \'{lineas}\'")
fichero.close()
