# Funciones
def menu():
    tareas = []

    while True:
        print("\n--- Gestor de tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            crear_tarea(tareas, titulo)
            print("Tarea agregada.")

        elif opcion == "2":
            mostrar_tareas(tareas)

        elif opcion == "3":
            try:
                posicion = int(input("Posición a eliminar: "))
            except ValueError:
                print("Eso no es un número válido. Intenta de nuevo.")
                continue

            eliminado = eliminar_tarea(tareas, posicion)
            if eliminado:
                print("Tarea eliminada.")
            else:
                print("Esa posición no existe.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

menu()

def crear_tarea(tareas, titulo):
    tarea = {'titulo': titulo}
    tareas.append(tarea)


def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
        return
    for indice, tarea in enumerate(tareas):
        print(f"Tarea número {indice + 1}: {tarea['titulo']}")


def eliminar_tarea(tareas, posicion):
    indice = posicion - 1
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        return True
    else:
        return False
