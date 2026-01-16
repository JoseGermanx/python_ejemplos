from modulos.validaciones import es_numero, clasificar_temperatura, clasificar_edad

temp_input = input("Ingrese la temperatura en °C: ")

if es_numero(temp_input):
    temperatura = float(temp_input)
    categoria = clasificar_temperatura(temperatura)
    print(f"Temperatura: {temperatura}°C → {categoria}")
else:
    print("Error: debe ingresar un número válido.")

edad_input = input("Ingrese su edad: ")

if es_numero(edad_input):
    edad = int(float(edad_input))
    print(clasificar_edad(edad))
else:
    print("Error: la edad debe ser numérica.")
