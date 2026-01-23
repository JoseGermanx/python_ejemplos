class Celular:
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    def encender(self):
        print(f"Encendiendo {self.marca} {self.modelo}...")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento} GB")


# Crear objetos
celular1 = Celular("Samsung", "Galaxy S22", 128)
celular2 = Celular("Apple", "iPhone 13", 256)

# Usar métodos
celular1.encender()
celular1.mostrar_info()

print()

celular2.encender()
celular2.mostrar_info()

# Explicación

# La clase Celular representa un objeto del mundo real usando código.

# El método __init__ define los datos mínimos que necesita cada celular al crearse.

# Cada objeto (celular1, celular2) es una instancia distinta:
# comparten la clase, pero mantienen sus propios valores.

# Los métodos encender() y mostrar_info() usan los atributos del objeto que los ejecuta.

# Esto muestra cómo una clase sirve como molde y los objetos son las versiones concretas que se usan en el programa.