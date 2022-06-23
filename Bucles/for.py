#Bucle for recorre datos de una determinada coleccion con un rango determinado

#Se define la lista
data = [2,5,6,7,8,1, "nico deja de pensar en ella"]

#El ciclo for recorrera las iteraciones de la lista una por una, la variable i es el iterador
for i in data:
    print(f"objeto: {i}")

#Ejercicio: sumatoria de todos los numeros entre 0 y 100

#total es una variable resultante que se ira incrementando
total = 0

#Se define un rango de valores, como si fuera una lista.
for i in range(0,101):
    #El ciclo tomara la variable total con un valor inicial y le sumara el valor de la iteracion correspondiente
    total+=i

#El resultado es un ciclo de sumas constantes hasta finalizar el rango
print(f"el resultado de la suma es: {total}")