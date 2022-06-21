# Encontrar area y longitud de un circulo

from cmath import pi


radio = float(input("r: "))

area = pi*(radio**2)
longitud = 2*pi*radio

print(f"Se tiene de area: {area:.1f} y de longitud: {longitud:.1f}")