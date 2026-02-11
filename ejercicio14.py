class Numero:
    def __init__(self, n):
        self.n = n
        self.cuadrado = 0
        self.cubo = 0

    def calcular(self):
        self.cuadrado = self.n ** 2
        self.cubo = self.n ** 3

    def mostrar(self):
        print("Número:", self.n)
        print("Cuadrado:", self.cuadrado)
        print("Cubo:", self.cubo)

n = float(input("Ingrese un número: "))
numero = Numero(n)
numero.calcular()
numero.mostrar()




