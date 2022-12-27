import functools
num = [1, 2, 3, 4, 5, 6, 2, 9, 10, 29, 45, 32, 87]
resultado = 0
for valor in num:
    resultado = resultado + valor
print(resultado)

print(str(functools.reduce((lambda x, resultado: x+resultado), num)))
