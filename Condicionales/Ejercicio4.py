# Crear un programa que simule un cajero

saldo = 2000
print("1. Ingreso de dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. Salir")
opcion = int(input("ingrese la opcion a realizar: "))

if opcion==1:
    ingreso = float(input("cantidad a ingresar: "))
    saldo += ingreso
    print(f"su nuevo saldo es {saldo}")
elif opcion==2:
    retiro =  float(input("cantidad a retirar: "))
    if retiro>saldo:
        print("No puede retirar ese monto")
    else:
        saldo -= retiro
        print("retiro satisfactorio")
    print(f"su nuevo saldo es {saldo}")
elif opcion==3:
    print(f"su saldo disponible es {saldo}")
elif opcion==4:
    print("Fin")
else:
    print("Error de opcion")