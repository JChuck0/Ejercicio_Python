import csv

# Constantes
ARCHIVO_TAREAS = "todos.csv"

# Funciones
def menu():
    """Bucle principal del gestor de tareas: muestra el menú y despacha
    cada opción a su función correspondiente."""
    tareas = []
    hay_cambios_sin_guardar = False

    while True:
        print("\n--- Gestor de tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Guardar tareas")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ").strip()
            if not titulo:
                print("El título no puede estar vacío. Intenta de nuevo.")
                continue
            crear_tarea(tareas, titulo)
            hay_cambios_sin_guardar = True
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
                hay_cambios_sin_guardar = True
                print("Tarea eliminada.")
            else:
                print("Esa posición no existe.")

        elif opcion == "4":
            if guardar_tareas(tareas, ARCHIVO_TAREAS):
                hay_cambios_sin_guardar = False
                print("Tareas guardadas correctamente.")

        elif opcion == "5":
            if hay_cambios_sin_guardar:
                respuesta = input(
                    "Tienes cambios sin guardar. ¿Guardar antes de salir? (s/n): "
                ).strip().lower()
                if respuesta == "s":
                    guardar_tareas(tareas, ARCHIVO_TAREAS)
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


def crear_tarea(tareas, titulo):
    """Añade una nueva tarea con el título indicado a la lista de tareas."""
    tarea = {'titulo': titulo}
    tareas.append(tarea)


def mostrar_tareas(tareas):
    """Imprime por pantalla todas las tareas, numeradas desde 1."""
    if not tareas:
        print("No hay tareas pendientes.")
        return
    for indice, tarea in enumerate(tareas):
        print(f"Tarea número {indice + 1}: {tarea['titulo']}")


def eliminar_tarea(tareas, posicion):
    """Elimina la tarea en la posición indicada (base 1).

    Devuelve True si se eliminó correctamente, False si la posición no existe.
    """
    indice = posicion - 1
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        return True
    else:
        return False


def guardar_tareas(tareas, archivo):
    """Guarda la lista de tareas en un archivo CSV.

    Devuelve True si el guardado fue exitoso, False si ocurrió un error.
    """
    try:
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=['titulo'])
            escritor.writeheader()
            for tarea in tareas:
                escritor.writerow(tarea)
        return True
    except OSError as error:
        print(f"No se pudieron guardar las tareas en '{archivo}': {error}")
        return False


def cargar_tareas(archivo):
    """Carga la lista de tareas desde un archivo CSV.

    Si el archivo no existe, no se puede leer o tiene un formato inválido,
    devuelve una lista vacía en lugar de interrumpir el programa.
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lectura = csv.DictReader(f)
            if lectura.fieldnames != ['titulo']:
                print(f"El archivo '{archivo}' tiene un formato inválido.")
                return []
            return list(lectura)
    except FileNotFoundError:
        return []
    except OSError as error:
        print(f"No se pudieron cargar las tareas desde '{archivo}': {error}")
        return []


menu()