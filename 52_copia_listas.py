lista_original = [1,2,3,4]
lista_copia = lista_original
print(lista_original)
print(id(lista_original))
print(type(lista_original))
print(lista_copia)
print(id(lista_copia))
print(type(lista_copia))
lista_original.append(5)
lista_copia.append(6)
print(lista_original)
print(lista_copia)
print(lista_original is lista_copia)
# con Copy
print('*'*25)
print('Usando copy')
lista_copia02 = lista_original.copy()
print(lista_original)
print(id(lista_original))
print(type(lista_original))
print(lista_copia02)
print(id(lista_copia02))
print(type(lista_copia02))
lista_original.append(7)
lista_copia02.append(8)
print(lista_original)
print(lista_copia02)
print(lista_original is lista_copia02)
# con slicing
print('*'*25)
print('Usando slicing')
lista_copia03 = lista_original[:] #[1:3]
print(lista_original)
print(id(lista_original))
print(type(lista_original))
print(lista_copia03)
print(id(lista_copia03))
print(type(lista_copia03))
# con metodo copy
import copy
print('*'*25)
print('Usando metodo copy')
lista_copia04 = copy.deepcopy(lista_original)
print(lista_original)
print(id(lista_original))
print(type(lista_original))
print(lista_copia04)
print(id(lista_copia04))
print(type(lista_copia04))
print(lista_original is lista_copia04)
# ejemplos varios
# asignacion directa
lista_original = [1,2,3,4]
lista_copia = lista_original
lista_copia[0] = 100
print('*'*25)
print('Ejercicios: ')
print(lista_original)
print(lista_copia)
# funcion copy
lista_copia = lista_original.copy()
lista_copia[1] = 200
print(lista_original)
print(lista_copia)
# slicing
lista_copia = lista_original[:]
lista_copia[2] = 300
print(lista_original)
print(lista_copia)
# modulo copy
lista_original = [[1,2],[3,4]]
lista_copia = copy.deepcopy(lista_original)
lista_copia[0][1] = 1000
print(lista_original)
print(lista_copia)