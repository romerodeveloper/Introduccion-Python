#Introduccion a listas
array=["futbol", "Pc", 18.6, 18, [6,7,10.4],True,False,18]

'''aqui muestra un solo elemento de la lista'''
print(array[4])

'''aqui muestra una serie de datos'''
print(array[0:3])

#Funcion de conteo de elementos
print(len(array))

#agregar valores al array, luego de la ultima posicion
array.append(66)
array.append(True)

#agregar un valor en una posicion especifica
array.insert(1,88)

#Agregar elementos a la lista en bloque
array.extend([1,44,True,"fuerza nico"])
print(array)

#Concatenar un array
array2 = [30,43,"nico deja de pensar en ella"]
array3 = array+array2
print(array3)

#Buscar un valor en la lista. Retorna un booleano
print("Pc" in array)

#Encontrar el index de un valor
print(array.index("Pc"))

#Cantidad de veces que se repite una palabra
print(array.count(18))

#Remover un elemento de la lista
array.remove(18)
print(array)

#Metodo para voltear de elementos la lista
array.reverse()
print(array)

#ordenar los metodos de forma ascendente
array4 = [1,3,2,8,5,10,-11]
array4.sort()
print(array4)

#Metodo para limpiar un array, eliminar todo su contenido
array.clear()
print(array)

