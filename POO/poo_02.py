class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"{self.nombre}, {self.edad} años")


# Crear objetos
persona1 = Persona("Lucía", 28)
persona2 = Persona("Martín", 35)

# Estado inicial
persona1.presentarse()
persona2.presentarse()

# Modificar edad solo de persona1
persona1.edad = 29

print("\nDespués de modificar la edad de persona1:")
persona1.presentarse()
persona2.presentarse()

# Agregar atributo dinámico solo a persona1
persona1.profesion = "Ingeniera"

print("\nAtributos de cada objeto:")
print("persona1:", persona1.__dict__)
print("persona2:", persona2.__dict__)

# Explicación

# La clase Persona define atributos comunes: nombre y edad.

# persona1 y persona2 son instancias distintas, cada una con su propio estado en memoria.

# Cuando se modifica persona1.edad, solo cambia ese objeto.
# persona2 permanece igual, lo que demuestra independencia entre instancias.

# El atributo profesion se agrega dinámicamente a persona1.
# Python lo permite porque los atributos pertenecen al objeto, no exclusivamente a la clase.

# Al imprimir __dict__ se ve claramente que:

# persona1 tiene nombre, edad y profesion

# persona2 solo tiene nombre y edad

# Esto deja visible que los objetos pueden compartir estructura inicial, pero no están obligados a tener exactamente los mismos atributos.