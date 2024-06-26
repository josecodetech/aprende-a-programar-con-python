lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]
concatenada = [str(a) + str(b) 
               for a, b in zip(lista1, lista2)]
print("Lista concatenada:", concatenada)
