# Crea un programa que comprueba si los paréntesis, llaves y corchetes
# de una expresión están equilibrados.
#  - Equilibrado significa que estos delimitadores se abren y cierran
#  en orden y de forma correcta.
#  - Paréntesis, llaves y corchetes son igual de prioritarios.
#  No hay uno más importante que otro.
#  - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  - Expresión no balanceada: { a * ( c + d ) ] - 5 }


def verificarExpresion(evaluation):
    
    pila = []
    symbol = {')':'(','}':'{', ']':'['}

    for tipo in evaluation:
        if tipo in symbol.values():
            pila.append(tipo)
        
        # Verifica si es un carácter de cierre. Se verifica si la pila no está vacía 
        # y si el último elemento de la pila coincide con el carácter de apertura esperado. 
        # Si coincide (pila.pop() = symbol), se elimina de la pila (pila = []).
        elif tipo in symbol.keys():
            if not pila or pila.pop() != symbol[tipo]:
                return False
            
    # Devuelve True si la pila está vacía al final
    return not pila


evaluation = input("Introduce alguna expresión: ")
veredict = verificarExpresion(evaluation)

if veredict:
    # La pila está vacía al final de la iteración, lo que indica que la expresión está balanceada
    print("La expresión está balanceada.")
else:
    
    print("La expresión no está balanceada.")