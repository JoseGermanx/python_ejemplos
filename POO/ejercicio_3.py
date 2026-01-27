class Libro:
    def __init__(self, titulo, autor, precio, stock):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
        self.set_precio(precio)

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: el precio debe ser positivo")

    def vender(self, unidades):
        if unidades <= 0:
            print("Error: las unidades deben ser mayores a cero")
        elif unidades > self.stock:
            print("Error: stock insuficiente")
        else:
            self.stock -= unidades
            print(f"Venta realizada: {unidades} unidades")

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: {self.get_precio()}")
        print(f"Stock: {self.stock}")
        print("-" * 20)

# Crear libros
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 15, 10)
libro2 = Libro("1984", "George Orwell", 20, 5)

# Mostrar información
libro1.mostrar_info()
libro2.mostrar_info()

# Realizar ventas
libro1.vender(3)
libro1.vender(20)

# Modificar precio
libro2.set_precio(-5)
libro2.set_precio(18)

libro2.mostrar_info()
