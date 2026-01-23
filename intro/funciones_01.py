def saludar():
    print("Hola, bienvenido a Python")

saludar()
saludar()
saludar()


def multiplicar(a, b):
    return a * b

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

resultado = multiplicar(num1, num2)
print("El resultado es:", resultado)


def bienvenida(nombre):
    print(f"Hola {nombre}, que tengas un buen día")

nombre_usuario = input("Ingresa tu nombre: ")
bienvenida(nombre_usuario)
