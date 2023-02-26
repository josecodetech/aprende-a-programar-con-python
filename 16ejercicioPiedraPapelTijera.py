

import random
import sys


def iniciar():
    global partidas, ganadas, perdidas, empatadas
    partidas = 0
    ganadas = 0
    perdidas = 0
    empatadas = 0


def menu():
    print("""
          Indica el numero de la opcion seleccionada:
          1. Piedra
          2. Papel
          3. Tijera
          0. Salir
          """)
    opcion = input("->")
    if opcion not in ['1', '2', '3', '0']:
        print('Selecciona una opcion valida\n')
        opcion_usuario = None
    else:
        if opcion == '1':
            opcion_usuario = 'Piedra'
        if opcion == '2':
            opcion_usuario = 'Papel'
        if opcion == '3':
            opcion_usuario = 'Tijera'
        if opcion == '0':
            print('Hasta pronto!!!')
            sys.exit()
    return opcion_usuario




def elige_maquina():
    lista_opciones = ['Piedra', 'Papel', 'Tijera']
    opcion = random.choice(lista_opciones)
    return opcion


def comprobar(opcion_usuario, opcion_maquina):
    global partidas, ganadas, perdidas, empatadas
    partidas += 1
    print("\n")
    if (opcion_usuario == opcion_maquina):
        print("Hemos empatado!!!")
        empatadas += 1  # empatadas = empatadas + 1
    elif (opcion_usuario == 'Piedra') and (opcion_maquina == 'Tijera'):
        print("Has ganado!!!")
        ganadas += 1
    elif (opcion_usuario == 'Papel') and (opcion_maquina == 'Piedra'):
        print("Has ganado!!!")
        ganadas += 1
    elif (opcion_usuario == 'Tijera') and (opcion_maquina == 'Papel'):
        print("Has ganado!!!")
        ganadas += 1
    else:
        print("Has perdido!!!")
        perdidas += 1
    print("\n")
    print('*'*20)
    print(f'Mi opcion fue {opcion_maquina}')
    print(f'Tu opcion fue {opcion_usuario}')
    print(f'Llevamos {partidas} partidas')
    print(f'Llevamos {ganadas} ganadas')
    print(f'Llevamos {perdidas} perdidas')
    print(f'Llevamos {empatadas} empatadas')
    print('*'*20)
    print("\n")


def main():
    iniciar()
    opcion_usuario = menu()
    while True:
        if opcion_usuario != None:
            opcion_maquina = elige_maquina()
            comprobar(opcion_usuario, opcion_maquina)
        opcion_usuario = menu()


if __name__ == '__main__':
    main()
