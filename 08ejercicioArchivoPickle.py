
import pickle


# grabar
with open('nombres.pickle', 'wb') as f:
    lista = ['Jose','M Mar', 'Lucia','Eva']

    pickle.dump(lista, f, pickle.HIGHEST_PROTOCOL)
    print("Fichero guardado")
# leer
with open('nombres.pickle', 'rb') as f:

    lista = pickle.load(f)
    print(lista)
    print("Fichero leido")
