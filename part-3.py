numeros = []
while True:
    numero = input("Ingrese numero: ")
    if numero == "q":
        break
    numeros.append(int(numero))

def mayor_valor(*args):
    """ Recibe un numero arbitrario de argumentos y retorna el valor mas alto
     
    Args:
        *args: numero de argumentos
         
    Returns:
     int: numero mas alto
    """
    print(args)
    return max(args)

result = mayor_valor(*numeros)
print(result)