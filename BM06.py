# Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que
#   lo resuelvan automáticamente.

from unidecode import unidecode

cadena = input("Introduce algunas palabras para contar cuántas veces se repitan palabras: ")

# Convierte la cadena a palabras minúsculas sin tildes.
cadena = unidecode(cadena).lower()

# Guarda las palabras una a una sin espacios.
lista_palabras = cadena.split()

# Se hace el conteo de palabras y se agregan al diccionario
cuenta_palabras = {}
for palabra in lista_palabras:
    if palabra in cuenta_palabras:
        cuenta_palabras[palabra] += 1
    else:
        cuenta_palabras[palabra] = 1

for palabra, contador in cuenta_palabras.items():
    print(f'La palabra "{palabra}" aparece {contador} veces.')