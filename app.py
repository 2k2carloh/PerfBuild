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
    print("║ 1. ║ Agregar usuarios")
    print("║ 2. ║ Ver trabajadores")
    print("║ 3. ║ Editar trabajadores")
    print("║ 4. ║ Agregar faena")
    print("║ 5. ║ Ver faena")
    print('║ 6. ║ Ingresar datos de cuadrillas')
    print("║ 7. ║ Ver cuadrillas y trabajadores por cuadrilla")
    print("║ 8. ║ Calcular la construcción")
    print("║ 0. ║ Salir")
    print("=================================")

#Statements
worker_name = []
worker_years = []
worker_level = []
worker_contract = []
worker_salary = []
worker_id_level = []
activity_faena = {}
cuadrilla = {}

# Restrictions porcentages 
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

        contract = None

        while contract is None:
            try:
                contract = int(input("Ingrese el tipo de contrato del trabajador.\n1.- Definido\n2.- Indefinido\n3.- Sin contrato"))

                if contract == 1:
                    worker_contract.append("Definido")
                elif contract == 2:
                    worker_contract.append("Indefinido")
                else: 
                    worker_contract.append("Sin contrato")
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
                    print(f"║ ID:          ║ {search_profile}")
                    print(f"║ Nombre:      ║ {worker_name[search_profile - 1]}")
                    print(f"║ Edad:        ║ {worker_years[search_profile - 1]}")
                    print(f"║ Experiencia: ║ {worker_level[search_profile - 1]}") 
                    print(f"║ Contrato:    ║ {worker_contract[search_profile - 1]}")
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

        activity = None
        while activity is None:
            try:
                activity = input("Ingrese la actividad de faena: ")

                if re.match(r'^\s*$', activity): 
                    clear_console()
                    print("Error: debe ingresar un nombre válido.")
                    activity = None
            except ValueError:
                clear_console()
                print("Error: debe ingresar un nombre válido.")
                activity = None

        activity_faena_repeat = None
        while activity_faena_repeat is None:
            try:
                activity_reptitions = int(input("Ingrese la cantidad de repeticiones de la actividad: "))
                if activity_reptitions < 0:  
                    clear_console()
                    print("Error: debe ingresar un número positivo válido .")
                else:
                    activity_faena_repeat = activity_reptitions
            except ValueError:
                clear_console()
                print("Error: debe ingresar un número válido.")
                activity = None
        
        activity_faena[activity] = activity_faena_repeat
        
        
        finish_loop = input("¿Desea terminar de agregar tareas? Si(s) para terminar, No(n) para continuar: ")
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

            ghost_input = input("Para continuar presione una tecla")

            if ghost_input == "ghost input ;)":
                clear_console()
            else:
                clear_console()

def viewCrewData():

    if len(cuadrilla) == 0:
        clear_console()
        ghost_input = input('Error: No tienes cuadrillas suficientes para hacer esto.\n')

        if ghost_input == "ghost input ;)":
            clear_console()
        else:
            clear_console()
    else:
        print("=================================")
        print("║ Cuadrilla ║ Trabajadores")
        print("=================================")
        for key, value in cuadrilla.items():
            print(f"║ {key} - {value}")

        print("=================================")
        print('')
        ghost_input = input("Para continuar presione una tecla")

        if ghost_input == "a":
            clear_console()
        else:
            clear_console()

def calculateDateConstrucction():
    
    if len(worker_name) == 0 :
        print('Antes de continuar, debes ingresar trabajadores.')
    elif len(activity_faena) == 0:
        print('Antes de continuar, debes ingresar actividades de faena.')
    elif len(cuadrilla) == 0:
        print('Antes de continuar, debes ingresar cuadrillas.')
    else:
        
        construcction_title = input("Ingrese que construcción desea calcular: ")
        counstruction_days = int(input("Ingrese la cantidad de días que durará la construcción: "))
        construction_meters = int(input("Ingrese la cantidad de metros cuadrados que se construirán: "))
        construction_cost = int(input("Ingrese el costo de la construcción: "))
        construction_cost_per_day = construction_cost / counstruction_days
        construction_cost_per_metere = construction_cost / construction_meters

        construction_meters_lineal = construction_meters ** 0.5

        percentage_payment_worker = ( construction_cost * 35 ) / 100

        #Junior payment is 5% of the total payment
        #Mid payment is 10% of the total payment
        #Senir payment is 20% of the total payment

        junior_payment = ( percentage_payment_worker * 20 ) / 100
        mid_payment = ( percentage_payment_worker * 30 ) / 100
        senior_payment = ( percentage_payment_worker * 50 ) / 100

        junior_count = 0
        mid_count = 0
        senior_count = 0

        meters_per_minute = 0

        for i in worker_level:
            if i == "Junior (Junior - 1-3 años)":
                junior_count += 1
                worker_id_level.append(1)
            elif i == "Mid (Mid - 3-6 años)":
                mid_count += 1
                worker_id_level.append(2)
            elif i == "Senior (Senior - 7 o más años)":
                senior_count += 1
                worker_id_level.append(3)
            else:
                print("Error: no hay trabajadores")

        payment_per_junior = junior_payment / junior_count
        payment_per_mid = mid_payment / mid_count
        payment_per_senior = senior_payment / senior_count

        for i in worker_id_level:
            if i == 1:
                worker_salary.append(payment_per_junior)
            elif i == 2:
                worker_salary.append(payment_per_mid)
            elif i == 3:
                worker_salary.append(payment_per_senior)
            else:
                print("Error: no hay trabajadores")

        for i in range(len(worker_level)):
            if worker_level[i] == "Junior (Junior - 1-3 años)":
                if worker_contract[i] == "Definido":
                    meters_per_minute += 0.3
                elif worker_contract[i] == "Indefinido":
                    meters_per_minute += 0.2
                else: 
                    meters_per_minute += 0.1
            elif worker_level[i] == "Mid (Mid - 3-6 años)":
                if worker_contract[i] == "Definido":
                    meters_per_minute += 0.5
                elif worker_contract[i] == "Indefinido":
                    meters_per_minute += 0.4
                else: 
                    meters_per_minute += 0.3
            else:
                if worker_contract[i] == "Definido":
                    meters_per_minute += 0.7
                elif worker_contract[i] == "Indefinido":
                    meters_per_minute += 0.6
                else: 
                    meters_per_minute += 0.5

        meters_per_hours = meters_per_minute * 60

        estimated_meters_per_day = construction_meters / counstruction_days

        hours_per_day = estimated_meters_per_day / meters_per_hours

        clear_console() 
        for i in range(len(worker_name)):
            print("=================================")
            print(f"║ Nombre: ║ {worker_name[i]}")
            print(f"║ Sueldo: ║ {worker_salary[i]}")
            print("=================================")

        print(f"El costo por día es de: {round(construction_cost_per_day, 2)}")
        print(f"El costo por metro cuadrado es de: {round(construction_cost_per_metere, 2)}")
        print(f"La jornada laboral es de: {round(hours_per_day)} horas por día")
        print(f'Los metros lineales de la faena son {round(construction_meters_lineal, 2)}')
        print(f'El rendimiento de mano de obra es de {round(estimated_meters_per_day, 2)} metros cuadrados por día')

        fanea_time = hours_per_day / 2

        count_faena_time = 0

        for i in activity_faena.values():
            count_faena_time += i

        hours_faena_per_activity = fanea_time / count_faena_time
        faena_total = hours_faena_per_activity * counstruction_days

        print(f'El tiempo estimado de cada actividad de faena es de {round(hours_faena_per_activity, 2)} horas por días')
        print(f'El tiempo para cada actividad es de: {round(faena_total, 2)} horas en {counstruction_days} días')

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
        viewCrewData()
    elif opcion == "8":
        clear_console()
        calculateDateConstrucction()
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