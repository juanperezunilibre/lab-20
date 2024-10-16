meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    #"Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

def mascaracteres():
    """ Devuelve la palabra con mas caracteres de la lista """

    palabra = ""

    for mes in meses:
        if len(mes) > len(palabra):
            palabra = mes
    return palabra

def mascaracteres2():
    """ Devuelve la palabra con mas caracteres de la lista """
    mas_largo = max([len(mes) for mes in meses])
    meses_largos = sorted([mes for mes in meses if len(mes) == mas_largo])
    return meses_largos[0]


print("Ordenado alfabeticamente", mascaracteres2())
print("No ordenado alfabeticamente", mascaracteres())