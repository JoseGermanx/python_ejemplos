class Empleado:
    aumento_general = 1.05  # atributo de clase

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aplicar_aumento(self):
        self.salario *= Empleado.aumento_general

    @classmethod
    def cambiar_aumento(cls, nuevo_factor):
        cls.aumento_general = nuevo_factor

    @staticmethod
    def salario_alto(salario, umbral=1000):
        return salario >= umbral

# Crear empleados
emp1 = Empleado("Ana", 900)
emp2 = Empleado("Luis", 1200)

# Evaluar salarios
print(Empleado.salario_alto(emp1.salario))
print(Empleado.salario_alto(emp2.salario))

# Cambiar aumento general
Empleado.cambiar_aumento(1.10)

# Aplicar aumento a todos
emp1.aplicar_aumento()
emp2.aplicar_aumento()

print(emp1.salario)
print(emp2.salario)
