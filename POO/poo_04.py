class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
        print("-" * 20)


# Crear objetos
libro1 = Libro("1984", "George Orwell", 1949)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)

# Llamar al método
libro1.mostrar_info()
libro2.mostrar_info()
