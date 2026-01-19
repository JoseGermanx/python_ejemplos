# Crear dos listas con colores (incluyendo repetidos):

catalogo_a = ["rojo", "azul", "verde", "negro", "blanco", "azul"]
catalogo_b = ["amarillo", "verde", "negro", "gris", "blanco", "verde"]


# Convertir las listas a conjuntos:

set_a = set(catalogo_a)
set_b = set(catalogo_b)


# Mostrar resultados:

print("Unión:", set_a | set_b)
print("Intersección:", set_a & set_b)
print("Solo catálogo A:", set_a - set_b)
print("Solo catálogo B:", set_b - set_a)


# Agregar un nuevo color al catálogo A:

set_a.add("violeta")


# Eliminar un color del catálogo B:

set_b.discard("gris")


# Mostrar los catálogos actualizados:

print("Catálogo A actualizado:", set_a)
print("Catálogo B actualizado:", set_b)