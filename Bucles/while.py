import math
#Ejercicio: Proponer que se solicite un numero positivo, si no cumple la condicion solicitar el numero hasta que sea positivo

#Solicitud del numero
numero = int(input("Escriba un numero positivo: "))

#Ciclo con la condicion de un numero menor a cero
while numero<0:
    print("porfavor ingrese un numero positivo")
    numero = int(input("vuelva a ingresar un numero: "))
print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero):.2f} ")