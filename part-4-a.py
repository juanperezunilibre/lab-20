numeros =[3, 5, 9, 11, 2, 8]

# 3 funciones - suma, max, min
# max, sum, min

def suma(numeros: list[int]):
    """ Función para sumar los valores de una lista de enteros
     
    Args:
        numeros (list[int]): lista de enteros para la suma

    Returns:
        int: La suma de los números de la lista  
    """
    acum_suma = 0
    for numero in numeros:
        acum_suma += numero
    numeros.pop(3)
    print(numeros)
    return acum_suma

def maximo(numeros: list[int]):
    """ Encuentra el numero maximo de la lista

    Args:
        numeros (list[int]): lista de enteros

    Returns:
        int: el número máximo de la lista  
    """
    max_number = 0
    for numero in numeros:
        if numero > max_number:
            max_number = numero
    return max_number

def minimo(numeros: list[int]):
    """ Encuentra el numero mínimo de la lista

    Args:
        numeros (list[int]): lista de enteros

    Returns:
        int: el número mínimo de la lista  
    """
    min_number = numeros[0]
    for numero in numeros:
        if numero < min_number:
            min_number = numero
    return min_number

print("La suma de la lista es:", suma(numeros))
print("El valor maximo de la lista es:", maximo(numeros))
print("El valor mínimo de la lista es:", minimo(numeros))


