from collections import Counter

# Datos iniciales
libros = {
    "B001": {
        "titulo": "1984",
        "autor": ("George Orwell", 1903),
        "genero": "Distopía",
        "stock": 5
    },
    "B002": {
        "titulo": "El Hobbit",
        "autor": ("J. R. R. Tolkien", 1892),
        "genero": "Fantasía",
        "stock": 2
    },
    "B003": {
        "titulo": "Fahrenheit 451",
        "autor": ("Ray Bradbury", 1920),
        "genero": "Distopía",
        "stock": 1
    }
}

# Mostrar todos los libros
print("Libros disponibles:")
for codigo, info in libros.items():
    print(codigo, "-", info["titulo"], "| Stock:", info["stock"])

# Buscar por género
genero_buscado = input("\nIngrese un género: ")
generos = {info["genero"] for info in libros.values()}

if genero_buscado in generos:
    print("Libros del género", genero_buscado)
    for info in libros.values():
        if info["genero"] == genero_buscado:
            print("-", info["titulo"])
else:
    print("No hay libros de ese género")

# Contar libros por género
contador_generos = Counter(info["genero"] for info in libros.values())
print("\nCantidad de libros por género:", contador_generos)

# Libros con bajo stock
print("\nLibros con stock menor a 3:")
for info in libros.values():
    if info["stock"] < 3:
        print("-", info["titulo"])

# Agregar un libro nuevo
libros["B004"] = {
    "titulo": "Dune",
    "autor": ("Frank Herbert", 1920),
    "genero": "Ciencia ficción",
    "stock": 4
}

# Actualizar stock
libros["B002"]["stock"] += 3

# Bonus: eliminar un libro
codigo_eliminar = input("\nCódigo a eliminar: ")
if codigo_eliminar in libros:
    del libros[codigo_eliminar]
    print("Libro eliminado")
else:
    print("Código no encontrado")
