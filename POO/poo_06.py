class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.set_precio(precio)

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: el precio debe ser un valor positivo")


# Crear producto con precio válido
producto = Producto("Notebook", 1200)

# Mostrar precio
print("Precio actual:", producto.get_precio())

# Intentar asignar un precio inválido
producto.set_precio(-500)

# Modificar precio correctamente
producto.set_precio(1500)
print("Nuevo precio:", producto.get_precio())
