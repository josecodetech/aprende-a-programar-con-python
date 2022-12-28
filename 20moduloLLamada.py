from moduloPropio import es_par as par

continua = 's'
while(continua == 's'):
    numero = int(input("Dime un numero "))
    valor = par(numero)
    if valor == True:
        print(f'El numero {numero} es par')
    else:
        print(f'El numero {numero} es impar')
    continua = input("Quieres continuar (s/n)?")
print("Hasta pronto!!!")
