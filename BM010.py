# Crea un programa que sea capaz de transformar texto natural a código
# morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar
#   la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#   o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
#   https://es.wikipedia.org/wiki/Código_morse.

from unidecode import unidecode
import re

morseCode = {
    "A":".- ", "B":"-... ", "C":"-.-. ",
    "CH":"---- ", "D":"-.. ", "E":". ",
    "F":"..-. ", "G":"--. ", "H":".... ",
    "I":".. ", "J":".--- ", "K":"-.- ",
    "L":".-.. ", "M":"-- ", "N":"-. ",
    "Ñ":"--.-- ", "O":"--- ", "P":".--. ",
    "Q":"--.- ", "R":".-. ", "S":"... ",
    "T":"- ", "U":"..- ", "V":"...- ",
    "W":".-- ", "X":"-..- ", "Y":"-.-- ",
    "Z":"--.. ", "0":"----- ", "1":".---- ",
    "2":"..--- ", "3":"...-- ", "4":"....- ",
    "5":"..... ", "6":"-.... ", "7":"--... ",
    "8":"---.. ", "9":"----. ", ".":".-.-.- ",
    ",":"--..-- ", "?":"..--.. ", '"':".-..-. ",
    " ":"       "
    }

phrase = input("Introduce una frase para convertirla a morse o de morse a texto natural: ")

decodePhrase = [phrase]

def toMorse(phrase):
    phrase = unidecode(phrase).upper()
    wordList = phrase.split()

    phraseMorse = ""

    for word in wordList:
        for letter in word:
            if letter in morseCode:
                phraseMorse = phraseMorse + morseCode[letter]
        phraseMorse = phraseMorse + " "
    return print(phraseMorse)


def toNaturalText(phrase):
    wordList = re.split(r'(\s+)', phrase)
    phraseNaturalText = ""
    
    for word in wordList:
        word = word+" "
        
        if word in morseCode.values():
            lista = list(morseCode.keys())[list(morseCode.values()).index(word)]
            lista = lista
            phraseNaturalText = phraseNaturalText + lista
        elif re.match(r"\s\s\s", word):
            phraseNaturalText = phraseNaturalText + " "
        
    phraseNaturalText = phraseNaturalText
    return print(phraseNaturalText)


if "-" and "." not in phrase:
    toMorse(phrase)
else:
    toNaturalText(phrase)