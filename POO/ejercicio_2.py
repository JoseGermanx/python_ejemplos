class Mascota:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años.")

    def es_joven(self):
        return self.edad < 5


# Lista de mascotas
mascotas = [
    Mascota("Luna", 2, "perra"),
    Mascota("Rocky", 7, "perro"),
    Mascota("Milo", 4, "gato"),
    Mascota("Nala", 6, "gata"),
]

# Recorrer mascotas
for mascota in mascotas:
    mascota.presentarse()
    if mascota.es_joven():
        print("Es joven")
    else:
        print("No es joven")
    print()

# Bonus: filtrar mascotas jóvenes
mascotas_jovenes = []

for mascota in mascotas:
    if mascota.es_joven():
        mascotas_jovenes.append(mascota)

print("Mascotas jóvenes:")
for mascota in mascotas_jovenes:
    print(mascota.nombre)

# Explicación

# La clase Mascota define datos (nombre, edad, tipo) y comportamiento.

# presentarse() muestra información usando los atributos del objeto.

# es_joven() no imprime nada: devuelve un valor lógico, lo que permite tomar decisiones.

# Cada mascota es un objeto distinto dentro de una lista común.

# Al recorrer la lista, cada objeto responde según su propio estado.

# El bonus muestra que los objetos pueden clasificarse y reutilizarse sin perder identidad.