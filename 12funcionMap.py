num = [1, 2, 3, 4, 5, 6]
print(num)
resultado = []
for valor in num:
    resultado.append(valor*2)
print(resultado)

# funcion map
print(list(map((lambda x: x*2), num)))
