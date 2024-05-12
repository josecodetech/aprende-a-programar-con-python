import time

def calcular_tiempo(funcion):
    def envuelve(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecucion de {funcion.__name__}: {round(fin-inicio,2)}")
    return envuelve #wrapper
@calcular_tiempo    
def operacion():
    time.sleep(2)
    print("Operacion realizada")
operacion()
