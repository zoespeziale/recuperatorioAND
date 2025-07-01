def temperatura_media_alta(temperaturas:list, umbral:int):   #Parámetros formales
    """
    Función que calcula el promedio de la temperaturas e indica si es mayor que el umbral
    temperaturas = lista de temperaturas
    umbral = entero
    Retorna True o False
    """
    mayor = False
    suma = 0
    for i in range(len(temperaturas)):
        suma += temperaturas[i]
    promedio = suma / len(temperaturas)
    if promedio > umbral:
        mayor = True
    return mayor




temperaturas = [18,22,25,20,21]
umbral = 20
print(temperatura_media_alta(temperaturas, umbral)) #Invocación 
                        #Parámetros actuales