# Ejercicio donde pida 2 numeros y determine cual de ellos es par

dato1 = int(input("ingresa un numero "))
dato2 = int(input("ingresa otro numero "))

if ((dato1%2)==0) and ((dato2%2)==0):
    print(f"los numeros son pares: {dato1}, {dato2}")
elif (dato1%2)==0:
    print(f"el numero {dato1} es par")
elif (dato2%2)==0:
    print(f"el numero {dato2} es par")
else:
    print("ninguno es par")
        