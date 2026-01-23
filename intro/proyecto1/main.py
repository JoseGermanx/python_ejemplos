# main.py
# Punto de entrada de la aplicación
# Descripción: Lee datos desde consola y usa un módulo externo

from modulos.operaciones import sumar

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = sumar(num1, num2)

print(f"La suma de {num1} y {num2} es {resultado}")
