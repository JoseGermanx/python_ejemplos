from modulos.menu import mostrar_menu
from modulos.gestion_datos import (
    agregar_tarea,
    listar_tareas,
    marcar_completada,
    eliminar_tarea
)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        texto = input("Ingrese la tarea: ")
        agregar_tarea(texto)
        continue

    if opcion == "2":
        listar_tareas()
        continue

    if opcion == "3":
        listar_tareas()
        indice = int(input("Número de tarea: ")) - 1
        marcar_completada(indice)
        continue

    if opcion == "4":
        listar_tareas()
        indice = int(input("Número de tarea a eliminar: ")) - 1
        eliminar_tarea(indice)
        continue

    if opcion == "5":
        print("Saliendo del programa...")
        break

    print("Opción inválida.")
