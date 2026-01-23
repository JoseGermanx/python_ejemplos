# Ámbitos de las variables (global y local)

contador = 10  # variable global

def sumar_uno():
    contador = 5  # variable local
    print("Dentro de la función:", contador)

sumar_uno()
print("Fuera de la función:", contador)


# 2. Recursividad

def contar_hasta_cero(n):
    if n == 0:
        print("Fin")
        return
    print(n)
    contar_hasta_cero(n - 1)

contar_hasta_cero(5)


#multiples valores

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    return suma, resta, multi

resultado_suma, resultado_resta, multi = operaciones(10, 3)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Mujl:", multi)


# incluye los 3 conceptos
# Variable global
contador_global = 0


def factorial_con_info(n):
    """
    Demuestra:
    - ámbito local (n, resultado)
    - uso de variable global
    - recursividad
    - retorno múltiple
    """
    global contador_global
    contador_global += 1  # uso de variable global

    if n == 0 or n == 1:
        return 1, contador_global  # retorno múltiple

    resultado, llamadas = factorial_con_info(n - 1)
    return n * resultado, llamadas


# Uso
factorial, total_llamadas = factorial_con_info(5)

print("Factorial:", factorial)
print("Llamadas recursivas:", total_llamadas)
