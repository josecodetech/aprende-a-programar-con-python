from random import randint as azar
continua = 's'
while (continua == 's' or continua == 'S'):
    lanzaDado = azar(1, 6)
    print(f'Has sacado un {lanzaDado}')
    continua = input("Continuamos (s/n)?")
print("Bien, lo dejamos aqui.")
