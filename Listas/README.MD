# LISTAS Y CONJUNTOS

## **Conjunto**
Es un tipo de datos de colección desordenado que es iterable, mutable y no tiene elementos duplicados. La clase de conjunto de Python representa la noción matemática de un conjunto.

### _Operaciones_

| __Operacion__ | __Escritura__
|-----------|-----------
| A==B | Conjuntos equivalentes o iguales, retorna como resultado un booleano.
| A palito B | Union de conjuntos, combina los elementos de los conjuntos, si se repite algun elemento solo se deja un solo valor.
|A&B | Interseccion de conjuntos, se obtiene como resultado el conjunto de los elementos en comun
|B-A | Diferencia de conjuntos, conjunto de elementos de B que no tiene A
| A^B | Diferencia simetrica, conjunto que contiene elementos de B que no tiene A y elementos de A que no tiene B

## **Lista**
Es una estructura de datos formada por una secuencia ordenada de objetos. Los elementos de una lista pueden accederse mediante su índice.

### _Operaciones_

| __Operacion__ | __Escritura__
|-----------|-----------
| Funcion de conteo de elementos | len(array)
| Agregar valores al array, en la ultima posicion de la lista | array.append("Valor")
| Agregar un valor en una posicion especifica, el primer valor es la posicion y el segundo es el elemento a ingresar | array.insert(1,"Valor")
| Agregar una serie de elementos a la lista en bloque | array.extend([1,44,True,"fuerza nico"])
| Concatenar un array | array3 = array+array2
| Buscar un valor en la lista. Retorna un booleano | print("Pc" in array)
| Encontrar el indice de un elemento de la lista | array.index("Pc")
| Cantidad de veces que se repite un elemento | array.count("valor")
|Remover un elemento de la lista | array.remove("Valor")
|Metodo para voltear de elementos la lista | array.reverse()
| Ordenar los metodos de forma ascendente, en casos numericos | array.sort()
| Metodo para limpiar una lista, eliminar todos los elementos de la lista | array.clear()