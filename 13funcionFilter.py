num = [1, 2, 3, 4, 5, 6, 2, 9, 10, 29, 45, 32, 87]
pares = []
for valor in num:
    if(valor % 2 == 0):
        pares.append(valor)
print(num)
print(pares)

print(list(filter((lambda valor: valor % 2 == 0), num)))
