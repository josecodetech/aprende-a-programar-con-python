# escritura
fichero = open("fichero.txt","w")
fichero.write("Hola, mensaje cambiado")
fichero.close()
print("Texto guardado")
# lectura
fichero = open("fichero.txt","r")
texto = fichero.readline()
fichero.close()
print(texto)
print("Fichero leido")
