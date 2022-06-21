#Saber si dos nombres tienen coincidencia al inicio y al final

nombre1 = input("ingrese un nombre: ")
nombre2 = input("ingrese otro nombre: ")

if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("los nombres tienen una coincidencia")
else:
    print("no hay coincidencia")