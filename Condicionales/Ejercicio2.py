#Pedir 3 numeros y determinar cual es mayor

n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese otro numero: "))
n3 = int(input("ingrese otro numero: "))

if n1>=n2 and n1>=n3:
    print(f"El numero mayor es el numero {n1}")
elif n2>=n1 and n2>=n3:
    print(f"El numero mayor es el numero {n2}")
elif n3>=n1 and n3>=n2:
    print(f"El numero mayor es el numero {n3}")
