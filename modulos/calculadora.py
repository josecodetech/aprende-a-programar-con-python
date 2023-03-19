def sumar(num1,num2):
    return num1 + num2
def restar(num1,num2):
    return num1 - num2
def multiplicar(num1,num2):
    return num1 * num2
def dividir(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "No se puede dividir por cero"
if __name__=='__main__':
    print(restar(34,21))