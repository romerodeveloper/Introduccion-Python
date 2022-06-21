#Condicional if

from traceback import print_tb


dato = int(input("Ingrese un numero: "))

if dato>0 :
    print("numero positivo")
    print("segundo resultado positivo")
elif dato==0:
    print("resultado cero")
else:
    print("es negativo")

print("fin")