# conjunto vacio
conjunto_vacio = set()

# conjunto con elementos
numeros = {1,2,3,4,5,6} 
letras = set(['a','b','c'])

print(conjunto_vacio)
print(numeros)
print(letras)
print('*'*25)
# agregar elementos
frutas = {'manzana','platano','naranja'}
print(frutas)
frutas.add('pera')
print(frutas)
# eliminar elemento
frutas.remove('platano')
print(frutas)
# union de conjuntos
conjunto1={1,2,3}
conjunto2={3,4,5}
union = conjunto1 | conjunto2
print(union)
# interseccion 
interseccion = conjunto1 & conjunto2
print(interseccion)
# diferencia
diferencia = conjunto1 - conjunto2
print(diferencia)
# diferencia simetrica
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)
# pertenencia
if 3 in conjunto1:
    print("El 3 esta en el conjunto 1")
else:
    print("El 3 no esta en el conjunto 1")
# longitud
longitud = len(conjunto1)
print(longitud)
# conversion lista y conjunto
lista = [1,2,2,2,3,4,5,5,6,7,8,9]
print(lista)
conjunto = set(lista)
print(conjunto)
lista_nueva = list(conjunto)
print(lista_nueva)