num1 = int(input("Primer numero-> "))
num2 = int(input("Segundo numero-> "))
try:
    resultado = num1 / num2
    print(resultado)
except NameError:
    print("Variable no definida")
except ZeroDivisionError:
    print("Error al dividir por cero")
finally:
    print("Esto se ejecuta siempre")
