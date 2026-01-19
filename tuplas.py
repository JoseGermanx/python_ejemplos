# Demo: Coordenadas geográficas con tuplas

# Tupla con coordenadas (latitud, longitud)
ciudad = ("Santiago", -33.4489, -70.6693)

print("Coordenadas de la ciudad:")
print(ciudad)

# Acceso por índice
latitud = ciudad[1]
longitud = ciudad[2]
print(f"Latitud: {latitud}")
print(f"Longitud: {longitud}")

# Intento de modificación (provoca error)
# ciudad[1] = -34.0  # TypeError: las tuplas son inmutables

# Reemplazo de la tupla completa
ciudad = ("Santiago", -34.0, -70.6693)

# Lista de tuplas con varias ciudades
ciudades = [
    ("Santiago", -33.4489, -70.6693),
    ("Buenos Aires", -34.6037, -58.3816),
    ("Lima", -12.0464, -77.0428)
]

# Iterar sobre la lista de tuplas
for nombre, lat, lon in ciudades:
    print(f"La ciudad está ubicada en ({lat}, {lon})")
