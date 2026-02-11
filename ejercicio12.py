class Empleado:
    def __init__(self, horas, valor_hora, porcentaje_retencion):
        self.horas = horas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion
        
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular_salarios(self):
        self.salario_bruto = self.horas * self.valor_hora
        self.retencion = self.salario_bruto * self.porcentaje_retencion / 100
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar_resultados(self):
        print("Salario bruto:", self.salario_bruto)
        print("Retención en la fuente:", self.retencion)
        print("Salario neto:", self.salario_neto)


# Programa principal
empleado = Empleado(48, 5000, 12.5)
empleado.calcular_salarios()
empleado.mostrar_resultados()
