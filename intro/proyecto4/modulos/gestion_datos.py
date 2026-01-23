# Lista que almacena las tareas
tareas = []

def agregar_tarea(texto):
    tarea = {
        "tarea": texto,
        "completado": False
    }
    tareas.append(tarea)

def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    for i, t in enumerate(tareas, start=1):
        estado = "✔" if t["completado"] else "✘"
        print(f"{i}. {t['tarea']} [{estado}]")

def marcar_completada(indice):
    if indice < 0 or indice >= len(tareas):
        print("Índice inválido.")
        return
    tareas[indice]["completado"] = True

def eliminar_tarea(indice):
    if indice < 0 or indice >= len(tareas):
        print("Índice inválido.")
        return
    tareas.pop(indice)
