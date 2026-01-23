# Sistema de gestión de estudiantes con menú

estudiantes = [
    ("Ana", 25, "Córdoba"),
    ("Luis", 30, "Rosario"),
    ("María", 22, "Córdoba"),
    ("Pedro", 28, "Mendoza"),
    ("Sofía", 26, "Buenos Aires")
]

while True:
    print("\n--- MENÚ ---")
    print("1. Listar estudiantes")
    print("2. Buscar estudiantes por ciudad")
    print("3. Calcular edad promedio")
    print("4. Agregar nuevo estudiante")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        for nombre, edad, ciudad in estudiantes:
            print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

    elif opcion == "2":
        ciudad_busqueda = input("Ingrese ciudad: ")
        contador = 0
        for _, _, ciudad in estudiantes:
            if ciudad.lower() == ciudad_busqueda.lower():
                contador += 1
        print(f"Estudiantes de {ciudad_busqueda}: {contador}")

    elif opcion == "3":
        suma_edades = 0
        for _, edad, _ in estudiantes:
            suma_edades += edad
        promedio = suma_edades / len(estudiantes)
        print(f"Edad promedio: {promedio:.2f}")

    elif opcion == "4":
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        ciudad = input("Ciudad: ")
        estudiantes.append((nombre, edad, ciudad))
        print("Estudiante agregado.")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
