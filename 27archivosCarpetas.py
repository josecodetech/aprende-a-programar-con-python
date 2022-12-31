import os
nombre = "MiCarpeta"
os.makedirs(nombre)
print(os.listdir("./"))
print(os.getcwd())
print(os.path.getsize(nombre))
print(os.path.isfile(nombre))
print(os.path.isdir(nombre))
# cambiar de directorio
nombre02 = "OtraCarpeta"
os.makedirs(nombre02)
os.chdir(nombre02)  # "../" "./"
print(os.getcwd())
print(os.listdir("./"))
os.chdir("../")
print(os.getcwd())
print(os.listdir("./"))
os.rename(nombre02, "Nuevo_nombre")
os.remove(os.getcwd()+"/carpeta02"+"/archivo.txt")
print("Archivo borrado")
os.chdir("carpeta02")
print(os.listdir("./"))
os.chdir("../")
os.rmdir("nueva_carpeta")
print(os.listdir("./"))
