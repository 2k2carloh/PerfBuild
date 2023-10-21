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
    print("║ 4. ║Agrear Tareas")
    print("║ 5. ║Ver Tareas")
    print("║ 0. ║Salir")
    print("=================================")
    print('Proyecto de: Carlos Rivera, Cristobal Morales, Catalina Bulnes')

worker_name = []
worker_years = []
worker_level = []
activity_faena = {}

# Enter workers
def joinWorkers ():

    worker = int(input("Cuantos trabajadores desea registrar?: "))

    for i in range(worker): 
        name = input("Ingresa el nombre del trabajador: ")
        worker_name.append(name)

        years = int(input("Ingresa los años del trabajador: "))
        worker_years.append(years)

        level = int(input("Ingrese el nivel del trabajador.\n1.- Poca experiencia (Junior - 1-3 años)\n2.- Mediana experiencia (Mid - 3-6 años)\n3.- Bastante experiencia (Senior - 7 o más años)\n"))

        if level == 1:
            worker_level.append("Junior (Junior - 1-3 años)")
        elif level == 2:
            worker_level.append("Mid (Mid - 3-6 años)")
        elif level == 3:
            worker_level.append("Senior (Senior - 7 o más años)")
        else: 
            worker_level.append("No definido")

        clear_console()
    
    return worker_name, worker_years, worker_level

def viewWorker ():
    while True:

        search_profile = int(input("Ingrese el ID de la persona que desea buscar: "))

        if search_profile == 0:
            print("Error: El perfil no existe")
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
            print("Error: El perfil no existe")

        break_while = int(input("Para buscar otro ID coloque 1, para salir, 0.\n"))

        if break_while == 0:
            clear_console()
            break  

        clear_console()

def getInfo():
    meters = float(input("Cuantos metros de construcción realizara?: "))
    days = float(input("Cuantos dias de trabajo realizara?: "))
    total_days = days * meters

def modiftyWorker():
    
    while True:

        search_profile = int(input("Ingresa el ID del trabajador que desea modificar: "))

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
            print('')
            print("=======================")
            print(f"║0. ║ Salir          ║")
            print(f"║1. ║ Nombre         ║")
            print(f"║2. ║ Edad           ║")
            print(f"║3. ║ Experiencia    ║") 
            print("=======================")

            while True: 
                modify_profile = int(input("¿Que esea modificar este perfil?: "))

                if modify_profile == 1:
                    new_name = input('Ingresa el nuevo nombre: ')
                    worker_name[search_profile - 1] = new_name
                elif modify_profile == 2:
                    new_years = int(input('Ingresa la nueva edad: '))
                    worker_years[search_profile - 1] = new_years
                elif modify_profile == 3:
                    new_level = int(input("Ingresa el nuevo nivel de experiencia: \n1.- Poca experiencia (Junior - 1-3 años)\n2.- Mediana experiencia (Mid - 3-6 años)\n3.- Bastante experiencia (Senior - 7 o más años)\n"))
                    if new_level == 1:
                        worker_level[search_profile - 1] = "Junior (Junior - 1-3 años)"
                    elif new_level == 2:
                        worker_level[search_profile - 1] = "Mid (Mid - 3-6 años)"
                    elif new_level == 3:
                        worker_level[search_profile - 1] = "Senior (Senior - 7 o más años)"
                    else: 
                        worker_level.append("No definido")
                else:
                    print("Error: Opción no valida")

                modify_profile = int(input('Desea modificar otra información?\n1. Si \n0. No\n'))
                if modify_profile == 0:
                    break

        else:
            print("El perfil no existe")

        break_while = int(input("Para modificar otro perfil coloque 1, para salir, 0.\n"))

        if break_while == 0:
            clear_console()
            break  

        clear_console()

# Restrictions
def restrictions ():
    
    lista_de_restricciones = {
        "Mal clima": None,
        "Equipamiento": None,
        "Contrato": None,
        "Dificultad": None,
        "Supervision": None
    }

# Request faena activity
def faena():

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

# View Faerna Activity
def viewFaena():
    print("=================================")
    print("║ Tarea ║ Repeticiones")
    print("=================================")
    for key, value in activity_faena.items():
        print(f"║ {key} - {value}")

    print("=================================")
    print('')
    ghost_input = input("Para continuar presione una tecla")

    if ghost_input == "a":
        clear_console()
    else:
        clear_console()

# MENU NAVEGATION
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
        clear_console()
        modiftyWorker()
    elif opcion == "4":
        clear_console()
        faena()
    elif opcion == "5":
        clear_console()
        viewFaena()
    elif opcion == "0":
        clear_console()
        print("Saliendo del programa...")
        break
    else:
        clear_console()
        print("Opción inválida. Por favor, seleccione una opción válida.")