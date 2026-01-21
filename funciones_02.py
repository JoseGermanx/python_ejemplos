edad_texto = "25"
edad = int(edad_texto)

precio = "19.99"
precio_float = float(precio)

numero = 10
numero_texto = str(numero)

print(edad, precio_float, numero_texto)

print(bool(""))
print(bool(0))
print(bool("Hola"))


x = 10
y = "Python"

print(type(x))
print(type(y))


print(isinstance(x, int))
print(isinstance(y, str))


texto = "Python"
numeros = [1, 2, 3, 4]

print(len(texto))
print(len(numeros))

cadena = "Hola"
lista_caracteres = list(cadena)

print(lista_caracteres)

tupla = tuple([1, 2, 3])
diccionario = dict(nombre="Ana", edad=30)

print(tupla)
print(diccionario)

edad = input("Ingresa tu edad: ")
print(f"Tienes {edad} años")


for i in range(1, 6):
    print(i)

numero = 3.7
print(round(numero))

valor = 3.14159
print(round(valor, 2))
