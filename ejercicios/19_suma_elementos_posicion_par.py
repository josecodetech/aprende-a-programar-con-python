lista = [1, 2, 3, 4, 5, 6]
suma = sum(lista[i] for i in range(len(lista)) 
           if i % 2 == 0)
print("Suma de elementos en posiciones pares:",
      suma)
