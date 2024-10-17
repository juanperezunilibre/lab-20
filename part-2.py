precio=float(input("Ingrese precio del producto: "))

def calcular_descuento(precio, dto=10):
    return precio * float(dto) / 100

print(calcular_descuento(precio))
print(calcular_descuento(precio, 20))
print(calcular_descuento(precio, 40))
print(calcular_descuento(precio, 60))
print(calcular_descuento(precio, 80))
print(calcular_descuento(precio, 100))