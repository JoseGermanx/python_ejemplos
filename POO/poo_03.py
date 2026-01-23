class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} hace un sonido")


# Crear instancia
mi_gato = Animal("Michi")

# Ejecutar método
mi_gato.hablar()

# Verificar tipo
print(isinstance(mi_gato, Animal))


# La instancia puede almacenarse en estructuras
animales = []
animales.append(mi_gato)

# Pasar la instancia como parámetro
def presentar_animal(animal):
    animal.hablar()

presentar_animal(mi_gato)


# Explicación

# La clase Animal define una estructura y un comportamiento.

# mi_gato = Animal("Michi") crea un objeto real en memoria a partir de la clase.

# El método hablar() se ejecuta desde la instancia, usando sus propios datos.

# isinstance(mi_gato, Animal) devuelve True, confirmando que el objeto pertenece a esa clase.

# La instancia no es algo abstracto:
# puede guardarse en una lista, pasarse a funciones y manipularse como cualquier otro objeto.

# La clase es el plano.
# La instancia es el objeto que existe y se usa en el programa.