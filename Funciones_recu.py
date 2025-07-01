
# Menú
def mostrar_opciones():
    """
    Función que pide al usuario una opción del menú
    Retorna la opción
    """
    opcion = input(f"Indique la opción que quiere realizar\n 1. Mostrar la lista de estudiantes y sus calificaciones\n 2. Ordenar los estudiantes de mayor a menor según su promedio\n 3. Buscar un estudiante por nombre y mostrar sus calificaciones\n 4. Buscar una calificación y mostrar a qué estudiante y materia pertenece\n 5. Salir\n Opción: ")
    return opcion

# Opción 1
def mostrar_matriz(matriz:list, lista:list):
    """
    Función que recorre una matriz y la printea
    matriz = lista de matriz a recorrer
    lista = lista a recorrer
    """
    for i in range(len(matriz)):
        print(f'{lista[i]}: ', end=" ")
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")



# Opción 2
def calcular_promedio(matriz:list):
    """
    Función que promedia los valores de una matriz
    matriz = lista donde se encuentran los valores a sumar
    Retorna el promedio de cada producto
    """
    valores_matrizA = 0
    valores_matrizB = 0
    valores_matrizC = 0
    valores_matrizD = 0
    for j in range(len(matriz[0])):
        valores_matrizA += matriz[0][j]
        valores_matrizB += matriz[1][j]
        valores_matrizC += matriz[2][j]
        valores_matrizD += matriz[3][j]
    promedio_matrizA = valores_matrizA / 3
    promedio_matrizB = valores_matrizB / 3
    promedio_matrizC = valores_matrizC / 3
    promedio_matrizD = valores_matrizD / 3
    return(promedio_matrizA, promedio_matrizB, promedio_matrizC, promedio_matrizD)

def ordenar_promedioEstudiantes(promedios:list, nombres:list):
    """
    Función que ordena los estudiantes por promedio de mayor a menor
    promedios = lista de promedios
    nombres = lista de estudiantes
    """
    for i in range(len(promedios)-1):
        for j in range(i+1, len(promedios)):
            if promedios[i] < promedios[j]:
                aux = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux
                aux2 = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux2

def mostrar_promedioOrdenados(promedios, nombres):
    """
    Función que muestra los estudiantes ordenados por promedio
    promedios = lista de promedios
    nombres = lista de estudiantes
    """
    for i in range(len(nombres)):
        print(f'Nombre: {nombres[i]}\nPromedio: {promedios[i]}')
        print(" ")



# Opción 3
def pedir_estudiante()->str:
    """
    Función que pide el nombre del estudiante a buscar
    Retorna el nombre indicado por el usuario
    """
    nombre = input('Indique el estudiante que desea buscar(Ana, Bruno, Carla, Diego): ')
    return nombre

def mostrar_estudiante(matriz:list, nombre:str, fila:int):
    """
    Función que muestra el estudiante dentro de una matriz y sus calificaciones
    matriz = lista donde se encuentran las calificaciones
    nombre = nombre del estudiante
    fila = fila correspondiente al estudiante a mostrar
    """
    print(f'{nombre} obtuvo un {matriz[fila][0]} en Matemática, {matriz[fila][1]} en Biología y {matriz[fila][2]} en Historia')



# Opción 4
def pedir_calificacion()->int:
    """
    Función que pide la caliificacion y devuelve un entero
    Retorna el valor indicado por el usuario
    """
    calificacion = int(input('Indique la calificacion que desea buscar: '))
    return calificacion

def buscar_calificacion(calificacion:int, matriz:list):
    """
    Función que busca la calificacion dentro de una matriz
    calificacion = entero que se busca en la matriz
    matriz = lista donde se realiza la búsqueda del número
    """
    existe = False
    estudianteA = matriz[0]
    estudianteB = matriz[1]
    estudianteC = matriz[2]
    estudianteD = matriz[3]
    materia = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == calificacion:
                existe = True
                if existe == True:
                    match j:
                        case 0:
                            materia = "Matemática"
                        case 1:
                            materia = "Historia"
                        case 2:
                            materia = "Biología"
                    if matriz[i] == estudianteA:
                        print(f'Ana obtuvo {calificacion} en {materia}')
                    if matriz[i] == estudianteB:
                        print(f'Bruno obtuvo {calificacion} en {materia}')
                    if matriz[i] == estudianteC:
                        print(f'Carla tuvo {calificacion} en {materia}')
                    elif matriz[i] == estudianteD:
                        print(f'Diego obtuvo {calificacion} en {materia}')
    if existe == False:
        print('No se ha encontrado ninguna calificacion con la nota indicada')
