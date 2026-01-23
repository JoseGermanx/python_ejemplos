# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return (base * altura) / 2


# Llamadas a las funciones
print("Conversión de Celsius a Fahrenheit:")
print("0°C ->", celsius_a_fahrenheit(0), "°F")
print("25°C ->", celsius_a_fahrenheit(25), "°F")
print("100°C ->", celsius_a_fahrenheit(100), "°F")

print("\nÁrea del triángulo:")
print("Base 10, Altura 5 ->", area_triangulo(10, 5))


