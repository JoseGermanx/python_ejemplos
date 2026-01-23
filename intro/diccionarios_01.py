# Crear el diccionario con los datos iniciales
persona = {
    "nombre": "Juan",
    "edad": 30,
    "email": "juan@email.com"
}

# Acceder a un valor usando su clave
print("Nombre:", persona["nombre"])

# Modificar un dato
persona["edad"] = 31

# Agregar un nuevo dato
persona["pais"] = "Argentina"

# Eliminar un campo (puede usarse pop o del)
persona.pop("email")
# del persona["email"]

# Mostrar claves, valores y pares
print("\nClaves:")
print(persona.keys())

print("\nValores:")
print(persona.values())

print("\nPares clave-valor:")
print(persona.items())

# Iterar sobre el diccionario
print("\nDatos de la persona:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Usar get() para acceder de forma segura
telefono = persona.get("telefono", "No disponible")
print("\nTeléfono:", telefono)
