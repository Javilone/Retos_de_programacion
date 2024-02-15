#¿ES UN ANAGRAMA?
# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
#  - Un Anagrama consiste en formar una palabra reordenando TODAS
#    las letras de otra palabra inicial.
#  - NO hace falta comprobar que ambas palabras existan.
#  - Dos palabras exactamente iguales no son anagrama.

def anagrama(palabra1, palabra2):
    if len(palabra1) == len(palabra2):
        lista1 = []
        lista2 = []
        for letra1 in palabra1:
            lista1.append(letra1)
        for letra2 in palabra2:
            lista2.append(letra2)
            
        sorted(lista1)
        sorted(lista2)

        if sorted(lista1) == sorted(lista2):
            print("Las palabras eran anagramas.")
        else: print("Esas palabras no son anagramas.")
                
    else: print("Esas palabras no son anagramas.")
    
inp1 = input("Introduce un palabra: ").lower()
inp2 = input("Introduce la segunda palabra: ").lower()

(anagrama(inp1, inp2))
