# Escribe una función que calcule y retorne el factorial de un número dado
# de forma recursiva.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
    
num = int(input("Pon un número: "))
print(factorial(num))