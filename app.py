import os
import re

# Clear console Function
def clear_console():
    os.system("cls")

clear_console()

# Select Menu
def view_menu():
    print("=================================")
    print("║          MENÚ - PerfBuild      ")
    print("=================================")
    print("║ 1. ║ Agregar Usuarios")
    print("║ 2. ║ Ver Trabajadores")
    print("║ 3. ║ Editar Trabajadores")
    print("║ 4. ║ Agregar Tareas")
    print("║ 5. ║ Ver Tareas")
    print("║ 6. ║ ver cuadrillas y trabajadores por cuadrilla")
    print("║ 0. ║ Salir")
    print("=================================")
    print('Proyecto de: Carlos Rivera, Cristobal Morales, Catalina Bulnes')

#Statements
worker_name = []
worker_years = []
worker_level = []
activity_faena = {}
cuadrilla = {}

def restrictionsPorcentages():
    restrictions_list = {
        "Mal clima": None,
        "Equipamiento": None,
        "Contrato": None,
        "Dificultad": None,
        "Supervision": None
    }

    restrictions = None
    while restrictions is None:

        number_counts = 1

        for key in restrictions_list.keys():
            print(f" {number_counts} ║ {key}")
            number_counts += 1

        print("")
        
        restrictions = input("¿Qué restricciones quieres usar? (separa con comas): ")
        if re.match(r'^\s*$', restrictions): 
            clear_console()
            print("Error: debe ingresar un nombre válido.")
            restrictions = None

    restrictions = [int(x) for x in restrictions.split(",")]

    total_restrictions = len(restrictions)
    percentage_per_restriction = 15 / total_restrictions

    for i in restrictions:
        restriction = list(restrictions_list.keys())[i-1]
        restrictions_list[restriction] = percentage_per_restriction

    print("Lista de restricciones con porcentajes:")
    for restriction, percentage in restrictions_list.items():
        if percentage is not None:
            print(f"{restriction}: {percentage}%")

    ghost_input = input("Para continuar presione una tecla")

    if ghost_input == "ghost input ;)":
        clear_console()
    else:
        clear_console()  

    return restrictions_list


# Enter workers
def joinWorkers ():

    worker = None

    while worker is None:
        try:
            worker = int(input("Cuantos trabajadores desea registrar?: "))
        except ValueError:
            clear_console()
            print("Error: debe ingresar un número válido.")
    

    for i in range(worker):

        name = None
        while name is None:
            name = input("Ingresa el nombre del trabajador: ")
            if re.match(r'^\s*$', name): 
                clear_console()
                print("Error: debe ingresar un nombre válido.")
                name = None

        worker_name.append(name)
        
        years = None
        while years is None:
            try:
                years = int(input("Ingresa los años del trabajador: "))
                worker_years.append(years)
            except ValueError:
                clear_console()
                print("Error: debe ingresar un año valido. ")

        level = None

        while level is None:
            try:
                level = int(input("Ingrese el nivel del trabajador.\n1.- Poca experiencia (Junior - 1-3 años)\n2.- Mediana experiencia (Mid - 3-6 años)\n3.- Bastante experiencia (Senior - 7 o más años)\n"))

                if level == 1:
                    worker_level.append("Junior (Junior - 1-3 años)")
                elif level == 2:
                    worker_level.append("Mid (Mid - 3-6 años)")
                elif level == 3:
                    worker_level.append("Senior (Senior - 7 o más años)")
                else: 
                    worker_level.append("No definido")
            except ValueError:
                clear_console()
                print("Error: debe ingresar una opción valida. ")

        clear_console()

# View workers info 
def viewWorker ():

        search_profile = None

        while search_profile is None:

            try:
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
            except ValueError:
                clear_console()
                print("Error: debe ingresar un número válido.")

# Modify workers info 
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
                modify_profile = int(input("¿Que desea modificar este perfil?: "))

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
        
def getIntoCrewData():

    if len(worker_name) == 0:
        clear_console()
        ghost_input = input('Error: No tienes trabajadores suficientes para hacer esto.\n')

        if ghost_input == "ghost input ;)":
            clear_console()
        else:
            clear_console()            

    else:
        number_of_crews = None
                    
        while number_of_crews is None:
            try:
                number_of_crews = int(input(f"Ingrese la cantidad de cuadrillas: \nTe recomendamos colocar la misma cantidad de cuadrillas que las actividades de faena: {len(activity_faena)} "))
            except ValueError:
                clear_console()
                print("Error: debe ingresar un número válido.")

            count_workers = len(worker_level)

            for i in range(number_of_crews):
                number_of_workers = None
                validate_workers = False

                while validate_workers is False:
                    try:
                        if len(worker_name) == 0:
                            print('Error: No tienes trabajadores suficientes para hacer esto.')
                            break

                        number_of_workers = int(input(f"Ingrese la cantidad de trabajadores de la cuadrilla {i+1}\n(Tienes {count_workers} trabajadores)\n "))

                        if number_of_workers < 0:  
                            clear_console()
                            print("Error: debe ingresar un número positivo válido .")
                        else:
                            if count_workers == 0:
                                clear_console()
                                ghost_input = input('Ya no tienes trabajadores suficientes para hacer esto.\n')

                                validate_workers = True
                            else:
                                if count_workers >= number_of_workers:
                                    cuadrilla[f'Cuadrilla {i+1}'] = number_of_workers

                                    count_workers -= number_of_workers

                                    if count_workers == 0:
                                        break

                                    validate_workers = True
                                        
                                elif number_of_workers == 0:
                                    clear_console()
                                    print("Error: no hay suficientes trabajadores")
                                else:
                                    clear_console()
                                    print("Error: no hay suficientes trabajadores")

                    except ValueError:
                        clear_console()
                        print("Error: debe ingresar un número válido.")

            for key, value in cuadrilla.items():
                print(f"║ {key} - {value}")

            ghost_input = input("Para continuar presione una tecla")

            if ghost_input == "ghost input ;)":
                clear_console()
            else:
                clear_console()

# MENU NAVEGATION
while True:
    view_menu()
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
    elif opcion == "6":
        clear_console()
        getIntoCrewData()
    elif opcion == "7":
        clear_console()
        restrictionsPorcentages()
    elif opcion == "0":
        clear_console()
        print("Saliendo del programa...")
        break
    else:
        clear_console()

        ghost_input = input("Opción inválida. Por favor, seleccione una opción válida.")

        if ghost_input == "a":
            clear_console()
        else:
            clear_console()