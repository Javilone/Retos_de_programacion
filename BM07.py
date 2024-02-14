# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


cadena = input("Introduce algunas palabras: ")
lista = []
cadena_invertida = []

for letra in cadena:
    lista.append(letra)

while lista:
    cadena_invertida.append(lista.pop())
    
for l in cadena_invertida:
    print(l,end="")