# Ejercicio_Python

## Gestor de tareas (app.py)

Aplicación de consola sencilla para gestionar una lista de tareas (to-do list).

### Cómo ejecutarla

```bash
python3 app.py
```

### Funcionamiento

Al ejecutarse, la app muestra un menú interactivo con las siguientes opciones:

1. **Agregar tarea**: pide un título y lo añade a la lista de tareas en memoria. No se permiten títulos vacíos.
2. **Mostrar tareas**: lista todas las tareas actuales, numeradas.
3. **Eliminar tarea**: pide el número de la tarea a eliminar y la borra de la lista.
4. **Guardar tareas**: guarda la lista de tareas actual en el archivo `todos.csv`.
5. **Salir**: cierra la aplicación. Si hay cambios sin guardar, pregunta si se desea guardarlos antes de salir.

Las tareas solo existen en memoria mientras el programa está en ejecución; para conservarlas es necesario usar la opción **Guardar tareas**, que las persiste en `todos.csv`.
