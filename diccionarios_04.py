# Base de datos de productos (diccionario anidado)
productos = {
    "P001": {"nombre": "Teclado", "precio": 5000, "stock": 10},
    "P002": {"nombre": "Mouse", "precio": 3000, "stock": 25},
    "P003": {"nombre": "Monitor", "precio": 80000, "stock": 5},
}

# Acceder a un producto por ID
producto = productos["P001"]
print("Producto P001:", producto)

# Agregar un nuevo producto
productos["P004"] = {"nombre": "Auriculares", "precio": 12000, "stock": 8}

# Modificar el stock de un producto existente
productos["P002"]["stock"] = 20

# Eliminar un producto
productos.pop("P003")

# Iterar sobre todos los productos
print("\nListado de productos:")
for id_producto, datos in productos.items():
    print(
        f"Producto: {datos['nombre']} | "
        f"Precio: ${datos['precio']} | "
        f"Stock: {datos['stock']}"
    )

# Bonus: productos con stock menor a 10
print("\nProductos con stock bajo:")
for id_producto, datos in productos.items():
    if datos["stock"] < 10:
        print(
            f"Producto: {datos['nombre']} | "
            f"Precio: ${datos['precio']} | "
            f"Stock: {datos['stock']}"
        )
