# Procedimiento: imprimir usuarios e intereses
def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print("Datos del usuario:")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")
        print("Intereses:")
        for interes in usuario['intereses']:
            print(f"- {interes}")
        print("-" * 20)


# Datos de ejemplo
usuarios = [
    {
        "nombre": "Ana",
        "edad": 20,
        "intereses": ["programación", "música", "fotografía"]
    },
    {
        "nombre": "Luis",
        "edad": 17,
        "intereses": ["videojuegos", "diseño", "tecnología"]
    }
]

# Llamada al procedimiento
mostrar_usuarios(usuarios)


# Procedimiento 2: verificar edad de acceso
def verificar_acceso(edad):
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado.")

verificar_acceso(20)