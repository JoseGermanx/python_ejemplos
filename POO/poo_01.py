class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1


# Instanciar objetos
persona1 = Persona("Ana", 25)
persona2 = Persona("Carlos", 30)

# Ejecutar métodos
persona1.presentarse()
persona2.presentarse()

# Cumplir años
persona1.cumplir_anios()

# Ver que cada objeto mantiene su estado
persona1.presentarse()
persona2.presentarse()

# Explicación

# class Persona: define una plantilla para crear personas.

# __init__ es el método especial que se ejecuta al crear un objeto.
# self.nombre y self.edad guardan datos propios de cada instancia.

# presentarse() usa esos atributos para mostrar información del objeto.

# cumplir_anios() modifica el estado del objeto sumando 1 a su edad.

# Cuando se crean persona1 y persona2, ambos usan la misma clase, pero mantienen datos independientes.
# Al cumplir años persona1, solo cambia su edad, no la de persona2.

# Esto muestra cómo una clase genera múltiples objetos con identidad y comportamiento propios.