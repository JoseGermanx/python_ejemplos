from collections import Counter

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

while True:
    print("\n--- MENÚ BIBLIOTECA ---")
    print("1. Mostrar todos los libros")
    print("2. Buscar libros por género")
    print("3. Estadísticas por género")
    print("4. Mostrar libros con bajo stock")
    print("5. Agregar nuevo libro")
    print("6. Actualizar stock")
    print("7. Eliminar libro")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        for codigo, info in libros.items():
            print(codigo, "-", info["titulo"], "| Stock:", info["stock"])

    elif opcion == "2":
        genero = input("Ingrese género: ")
        encontrados = False
        for info in libros.values():
            if info["genero"] == genero:
                print("-", info["titulo"])
                encontrados = True
        if not encontrados:
            print("No hay libros de ese género")

    elif opcion == "3":
        contador = Counter(info["genero"] for info in libros.values())
        print("Libros por género:", contador)

    elif opcion == "4":
        for info in libros.values():
            if info["stock"] < 3:
                print("-", info["titulo"])

    elif opcion == "5":
        codigo = input("Código: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = int(input("Año nacimiento autor: "))
        genero = input("Género: ")
        stock = int(input("Stock: "))

        libros[codigo] = {
            "titulo": titulo,
            "autor": (autor, anio),
            "genero": genero,
            "stock": stock
        }
        print("Libro agregado")

    elif opcion == "6":
        codigo = input("Código del libro: ")
        if codigo in libros:
            cantidad = int(input("Cantidad a sumar: "))
            libros[codigo]["stock"] += cantidad
            print("Stock actualizado")
        else:
            print("Libro no encontrado")

    elif opcion == "7":
        codigo = input("Código a eliminar: ")
        if codigo in libros:
            del libros[codigo]
            print("Libro eliminado")
        else:
            print("Código no válido")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
