class Producto:
    descuento = 0.10  # 10% de descuento general

    def __init__(self, nombre, precio):
        self.nombre = nombre
        if Producto.validar_precio(precio):
            self.__precio = precio
        else:
            print("Precio inválido")
            self.__precio = 0

    def get_precio(self):
        return self.__precio

    def aplicar_descuento(self):
        return self.__precio * (1 - Producto.descuento)

    @classmethod
    def set_descuento(cls, nuevo_descuento):
        cls.descuento = nuevo_descuento

    @staticmethod
    def validar_precio(precio):
        return precio > 0

# Crear productos
prod1 = Producto("Teclado", 100)
prod2 = Producto("Mouse", 50)

# Ver precios
print(prod1.get_precio())
print(prod2.get_precio())

# Aplicar descuento
print(prod1.aplicar_descuento())
print(prod2.aplicar_descuento())

# Cambiar descuento general
Producto.set_descuento(0.20)

print(prod1.aplicar_descuento())
print(prod2.aplicar_descuento())
