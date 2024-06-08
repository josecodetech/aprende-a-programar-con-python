import os

def renombrar_archivos():
    archivos = os.listdir('.')
    for archivo in archivos:
        if archivo.endswith('.txt'):
            if len(archivo) > 8:
                nuevo_nombre = archivo[8:-4]+"back.txt"
                os.rename(archivo, nuevo_nombre)
                print(f"{archivo} -> {nuevo_nombre}")
if __name__ == "__main__":
    renombrar_archivos()              
            