import os

# Clear console Function
def clear_console():
    os.system("cls")

clear_console()

# Select Menu
def mostrar_menu():
    print("=================================")
    print("║          MENÚ - PerfBuild      ")
    print("=================================")
    print("║ 1. ║Agregar Usuarios")
    print("║ 2. ║Ver Trabajadores")
    print("║ 3. ║Editar Trabajadores")
    print("║ 0. ║Salir")
    print("=================================")
    print('Dev by: Carlos Rivera, Cristobal Morales, Catalina Bulnes')


worker_name = []
worker_years = []
worker_level = []

# Enter workers
def joinWorkers ():

    worker = int(input("Cuantos trabajadores desea registrar?: "))

    for i in range(worker): 
        name = input("Ingresa el nombre del trabajador: ")
        worker_name.append(name)

        years = int(input("Ingresa los años del trabajador: "))
        worker_years.append(years)

        level = int(input("Ingrese el nivel del trabajador.\n1.- Poca experiencia (Junior - 1-3 años)\n2.- Mediana experiencia (Mid - 3-5 años)\n3.- Bastante experiencia (Senior - 5 o más años)\n"))

        if level == 1:
            worker_level.append("Junior")
        elif level == 2:
            worker_level.append("Mid")
        elif level == 3:
            worker_level.append("Senior")
        else: 
            worker_level.append("No definido")

        clear_console()
    
    return worker_name, worker_years, worker_level

def viewWorker ():
    while True:

        search_profile = int(input("Ingrese el ID de la persona que desea buscar: "))

        if search_profile == 0:
            print("El perfil no existe")
        elif search_profile <= len(worker_name):
            print("=================================")
            print(f'║ Usuario {search_profile} de {len(worker_name)} ')
            print("=================================")
            print(f"║ID:          ║ {search_profile}")
            print(f"║Nombre:      ║ {worker_name[search_profile - 1]}")
            print(f"║Edad:        ║ {worker_years[search_profile - 1]}")
            print(f"║Experiencia: ║ {worker_level[search_profile - 1]}") 
            print("=================================")
        else:
            print("El perfil no existe")

        break_while = int(input("Para buscar otro ID coloque 1, para salir, 0.\n"))

        if break_while == 0:
            clear_console()
            break  

        clear_console()

def getInfo():
    meters = float(input("Cuantos metros de construcción realizara?: "))
    days = float(input("Cuantos dias de trabajo realizara?: "))
    total_days = days * meters


# Request faena activity
def faena():
    activity_faena = {}

    while True:
        activity = input("¿Ingrese la actividad que desea realizar?: ")
        activity_reptitions = int(input("¿Cuantas veces quiere repetir esta actividad?: "))

        activity_faena[activity] = activity_reptitions
        
        finish_loop = input("¿Desea terminar de agregar tareas?: ")
        finish_loop = finish_loop.lower()

        if finish_loop == "s" or finish_loop == "si":
            clear_console()
            break

        clear_console()

    print( activity_faena )

# Restrictions
def restrictions ():
    
    lista_de_restricciones = {
        "Mal clima": None,
        "Equipamiento": None,
        "Contrato": None,
        "Dificultad": None,
        "Supervision": None
    }

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de opción que desea ejecutar: ")

    if opcion == "1":
        clear_console()
        joinWorkers ()
    elif opcion == "2":
        clear_console()
        viewWorker()
    elif opcion == "3":
        print('hola') 
    elif opcion == "0":
        clear_console()
        print("Saliendo del programa...")
        break
    else:
        clear_console()
        print("Opción inválida. Por favor, seleccione una opción válida.")