# Solicitar una frase al usuario
frase = input("Ingresa una frase: ").lower()

# Dividir la frase en palabras
palabras = frase.split()

# Diccionario para contar frecuencias
frecuencia = {}

# Contar palabras usando get()
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Imprimir el diccionario final
print("\nFrecuencia de palabras:")
print(frecuencia)

# Bonus: ordenar por frecuencia descendente
frecuencia_ordenada = dict(
    sorted(frecuencia.items(), key=lambda item: item[1], reverse=True)
)

print("\nFrecuencia ordenada (descendente):")
for palabra, cantidad in frecuencia_ordenada.items():
    print(f"{palabra}: {cantidad}")
