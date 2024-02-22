# Escribe una función que reciba un texto y retorne verdadero o
# falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.

from unidecode import unidecode

def palindromas(cadena1):
    # Obtengo la frase en minusculas y sin tildes
    cadena1 = cadena1.lower()
    cadena1 = unidecode(cadena1).lower()
    # Obtengo la frase sin espacios y también del reves
    sinespacios = cadena1.replace(" ","")    
    delreves = sinespacios[::-1]
    # Comparto ambos resultados
    if sinespacios == delreves:
        print("La frase es palindroma")
    else:
        print("La frase no era palíndroma")
    
cadena1 = input("Introduce una palabra o frase: ")
palindromas(cadena1)
