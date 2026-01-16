def leer_str(mensaje):
    return input(mensaje).strip()

def leer_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número entero.")

def leer_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingrese un número decimal.")
