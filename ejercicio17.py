import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.longitud = 0

    def calcular(self):
        self.area = math.pi * self.radio ** 2
        self.longitud = 2 * math.pi * self.radio

    def mostrar(self):
        print("Radio:", self.radio)
        print("Área del círculo:", self.area)
        print("Longitud de la circunferencia:", self.longitud)


# Programa principal
r = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(r)
circulo.calcular()
circulo.mostrar()
