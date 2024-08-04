def mayor_que_cinco(num):
    return num > 5

numeros = [2, 3, 5, 6, 7, 8]
filtrados = list(filter(mayor_que_cinco, numeros))
print("Filtrados:", filtrados)
