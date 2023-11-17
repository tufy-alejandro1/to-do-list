#Lista para almacenar tareas
tareas = []

#Función para agregar una tarea
def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")
    
#Función para mostar tdas las tareas
def mostrar_tareas():
    if not tareas:
        print('La lista de tareas está vacía.')
    else:
        print('Lista de tareas: ')
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
            
#Función para eliminar una tarea
def eliminar_tarea(numero_tarea):
    if 1 <= numero_tarea <= len(tareas):
        tarea_eliminada = tareas.pop(numero_tarea -1)
        print('Tarea eliminada')
    else:
        print('Número de tarea no válido.')
        
#Menu interactivo
while True:
    print("to-do list")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("1. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        nueva_tarea = input("Ingresa la nueva tarea:")
        agregar_tarea(nueva_tarea)
    elif opcion == '2':
        mostrar_tareas()
    elif opcion == '3':
        if not tareas:
            print("La lista de tareas está vacía.")
        else: 
            mostrar_tareas()
            tarea_a_eliminar = int(input("Ingresa el número de la tarea que quieres eliminar: "))
    elif opcion == '4':
        print("Hasta luego!")
        break
    else:
        print("Opción no válida.")
        
            





