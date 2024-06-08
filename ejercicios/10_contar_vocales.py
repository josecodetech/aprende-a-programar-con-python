texto = input("Ingresa un texto: ").lower()
vocales = "aeiou"
conteo = sum(1 for char in texto if char in vocales)
print("Número de vocales:", conteo)
