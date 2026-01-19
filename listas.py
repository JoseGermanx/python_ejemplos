# Demo: Gestor simple de tareas

tareas = ["Estudiar Python", "Hacer ejercicios", "Leer documentación"]

while True:
    print("\nTareas actuales:")
    if not tareas:
        print("¡Todas las tareas completadas!")
        

    for i, tarea in enumerate(tareas):
        print(f"{i}. {tarea}")

    print("\nOpciones:")
    print("1 - Agregar tarea")
    print("2 - Completar tarea")
    print("3 - Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nueva = input("Nueva tarea: ")
        tareas.append(nueva)

    elif opcion == "2":
        indice = input("Índice de tarea completada: ")
        if indice.isdigit():
            indice = int(indice)
            if 0 <= indice < len(tareas):
                tareas.pop(indice)
            else:
                print("Índice inválido")
        else:
            print("Debes ingresar un número")

    elif opcion == "3":
        print("Cerrando aplicación")
        break

    else:
        print("Opción inválida")
