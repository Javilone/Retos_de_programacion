# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
#   la que el siguiente siempre es la suma de los dos anteriores.
#   0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(1,50):
    print(fibonacci(i), end=" ")