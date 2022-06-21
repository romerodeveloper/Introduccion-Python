#formato de codigo que se repetira n veces hasta que se cumpla una determinada condicion

import math

numero = int(input("Escriba un numero positivo: "))

while numero<0:
    print("porfavor ingrese un numero positivo")
    numero = int(input("vuelva a ingresar un numero: "))
print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero):.2f} ")