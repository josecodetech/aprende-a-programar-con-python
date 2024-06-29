def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
        intercambio = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambio = True
        if not intercambio:
            break
numeros = [5,3,8,4,2]
print("Lista original: ", numeros)
ordenamiento_burbuja(numeros)
print("Lista ordenada: ",numeros)
