# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

valor = int(input("Introduce un entero para convertirlo a decimal: "))
resto = []

while valor > 0:
    dividir = divmod(valor,2)  
    resto.insert(0,dividir[1])
    
    valor = dividir[0]

for n in resto:
    print(n,end="")