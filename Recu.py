from Funciones_recu import *

estudiantes = ["Ana", "Bruno", "Carla", "Diego"]

calificaciones = [
    #Matemática, Historia, Biología
    [9, 8, 10],
    [6, 7, 8],
    [10, 10, 9],
    [7, 6, 5]
]

print("¡Bienvenido al reporte de estudiantes de la escuela 801!")
print("")
while True:

    opcion = int(mostrar_opciones())
    print("")
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
        print("La opción indicada no existe")
        opcion = int(mostrar_opciones())
    print("")

    match opcion:

        case 1:
            mostrar_matriz(calificaciones, estudiantes)

        case 2:
            lista_promedios = list(calcular_promedio(calificaciones))
            copia_estudiantes = ["Ana", "Bruno", "Carla", "Diego"]
            ordenar_promedioEstudiantes(lista_promedios, copia_estudiantes)
            mostrar_promedioOrdenados(lista_promedios, copia_estudiantes)

        case 3:
            nombre = pedir_estudiante()
            while nombre != 'Ana' and nombre != 'Bruno' and nombre != 'Carla' and nombre != 'Diego':
                print('El estudiante ingresado no existe.')
                nombre = pedir_estudiante()
            if nombre == 'Ana':
                fila = 0
            if nombre == 'Bruno':
                fila = 1
            if nombre == 'Carla':
                fila = 2
            if nombre == 'Diego':
                fila = 3 
            mostrar_estudiante(calificaciones, nombre, fila)

        case 4:
            calificacion = pedir_calificacion()
            buscar_calificacion(calificacion, calificaciones)

        case 5:
            print('¡Hasta luego!')
            break

        case _:
            print('La opción indicada no existe.')
            continue
    
    print("")
    otra_accion = input('¿Desea realizar otra acción? (Si/No): ').lower()
    print("")
    while otra_accion != 'si' and otra_accion != 'no':
        print('Ingrese una opción válida')
        otra_accion = input('¿Desea realizar otra acción? (Si/No): ')
    if otra_accion == 'no':
        print('¡Hasta luego!')
        break
    