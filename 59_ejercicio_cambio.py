# Definir denominaciones de euros y centimos
DENOMINACIONES = [50000, 20000, 10000, 5000, 2000, 1000, 500,200,100, 50, 20, 10, 5, 2, 1 ]
def calcular_cambio(cantidad):
    """Calcula la cantidad de billetes y monedas necesarios para devolver la cantidad de dinero indicada.
    Se asume que la cantidad se expresa en centimos.
    
    Parametros:
    cantidad (float) : La cantidad de dinero en euros
    Retorna:
    dict: Un diccionario con la cantidad de cada denominacion
    """
    # Convertir la cantidad a centimos
    cantidad_centimos = int(round(cantidad * 100))
    # Iniciamos el diccionario de respuesta
    resultado = {denominacion: 0 for denominacion in DENOMINACIONES}
    # Calcular cantidad de cada denominacion
    for denominacion in DENOMINACIONES:
        if cantidad_centimos >= denominacion:
            resultado[denominacion]= cantidad_centimos // denominacion
            cantidad_centimos = cantidad_centimos % denominacion
    return resultado
def imprimir_resultado(resultado):
    """
    Imprime el resultado de la cantidad de billetes y monedas necesarios.
    
    Parametros: Resultado de funcion calcular cambio
    resultado(dict): Un diccionario con la cantidad de cada denominacion
    """
    for denominacion, cantidad in resultado.items():
        if cantidad > 0:
            if denominacion > 200:
                print(f"{cantidad} billete(s) de {denominacion//100} euros")
            elif denominacion >= 100:
                print(f"{cantidad} moneda(s) de {denominacion//100} euros")
            else:
                print(f"{cantidad} moneda(s) de {denominacion} centimos")
def main():
    cantidad = float(input("Introduce la cantidad en euros: "))
    resultado = calcular_cambio(cantidad)
    imprimir_resultado(resultado)
if __name__ == "__main__":
    main()   
    