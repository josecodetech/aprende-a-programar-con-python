def es_par(numero=0):
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")


def es_par_return(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False


def sumar(numero1=0, numero2=0):
    resultado = numero1 + numero2
    return resultado


# es_par(13)
numero = int(input("Dime un numero y te dire si es par -> "))
es_par(numero)
numero = int(input("Dime un numero y te dire si es par -> "))
if(es_par_return(numero) == True):  # podemos eliminar la comparacion en este caso por ser booleano
    print("El numero es par")
else:
    print("El numero es impar")
# llamada a sumar
numero1 = int(input("Dime el primer numero "))
numero2 = int(input("Dime el segundo numero "))
resultado = sumar(numero1, numero2)
print(
    f'El resultado de sumar {numero1} mas {numero2} es igual a {resultado}')
