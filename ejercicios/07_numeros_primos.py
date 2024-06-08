numero = int(input("Ingresa un número: "))
es_primo = True
if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("Es un número primo.")
else:
    print("No es un número primo.")
