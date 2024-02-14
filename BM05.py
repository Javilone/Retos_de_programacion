# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

from abc import ABC, abstractmethod


# Creación de la interfaz que usarán el resto de clases.
class Poligono(ABC):   
    @abstractmethod
    def area(self):
        pass
    def salida(self):
        pass

# Clases para poligonos
class Triangulo(Poligono):
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura
    def area(self):
        return((self.base*self.altura)/2)
    def salida(self):
        return f"El area del triángulo es {triangulo.area()}"

class Cuadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return(self.lado*self.lado)
    def salida(self):
        return f"El area del cuadrado es {cuadrado.area()}"
    
class Rectangulo(Poligono):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self):
        return(self.largo*self.ancho)
    def salida(self):
        return f"El area del rectángulo es {rectangulo.area()}"

# Creando los objetos
triangulo = Triangulo(4, 8)
cuadrado = Cuadrado(8)
rectangulo = Rectangulo(4,4)
triangulo2 = Triangulo(1, 2)

# Mostrar objetos por salida
print(triangulo.salida(),"\n",cuadrado.salida(),"\n",rectangulo.salida(),"\n",triangulo2.salida())
