import math
# formula area = pi / r ** 2

def area_circulo(radio):
    pi = round(math.pi, 4)
    return pi * radio ** 2

print(f"El area del circulo es: {area_circulo(5)}")