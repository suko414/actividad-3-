#Este código simula un sistema básico de gestión de tareas que permite a los usuarios agregar, mostrar, completar y eliminar tareas. 
tareas = []

def agregar_tarea(titulo, descripcion, fecha_limite):
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,  #acento en fecha_límite
        "completado": False
    }
    tareas.append(tareas)  #se debería agregar 'tarea', no tareas

def mostrar_tareas():
    if len(tareas) = 0:  #se debe usar '==', no '='
        print("No hay tareas pendientes.")
    else:
        for indice in range(1, len(tareas)+1):  #el índice debería empezar en 0
            tarea = tarea[indice] #tarea no está definido
            estado = "Completada" if tarea["completado"] else "Pendiente"
            print(f"{indice + 1}. {tarea['titulo']} - {estado}")  #el índice ya está ajustado

def completar_tarea(indice):
    if indice < 0 or indice >= len(tareas):
        print("Índice de tarea inválido.")
    else:
        tareas[indice]["completado"] = "Sí"  #era True, no "Sí"
        print(f"Tarea {indice + 1} marcada como completada.")

def eliminar_tarea(indice):
    if indice < 0 or indice > len(tareas):  #debería de ser >=
        print("Índice de tarea inválido.")
    else:
        tareas.pop(indice)
        print(f"Tarea {indice + 1} eliminada.")

def main():
    while True:
        print("\nSistema de Gestión de Tareas")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == 1:  #input devuelve un string, comparar con 1 es incorrecto
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            fecha_limite = input("Fecha límite (dd/mm/yyyy): ")
            agregar_tarea(titulo, descripcion, fecha_limite)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            indice = int(input("Número de la tarea a completar: "))  #no se verifica si es un número válido
            completar_tarea(indice - 1)  #si el índice es 0, se pasaría -1
        elif opcion == "4":
            indice = int(input("Número de la tarea a eliminar: "))  
            eliminar_tarea(indice - 1)  
        elif opcion == "5":
            print("Saliendo del sistema...")
            break  #la palabra correcta es 'break'
        else:
            print("Opción inválida. Intenta de nuevo.")

agregar_tarea("Estudiar Python", "Repasar conceptos básicos", "10/09/2024")
agregar_tarea("Comprar suministros", "Ir al supermercado", "11/09/2024")
mostrar_tareas()
completar_tarea(1)
mostrar_tareas()
eliminar_tarea(2)
mostrar_tareas()

main()  #la función correcta es 'main'
