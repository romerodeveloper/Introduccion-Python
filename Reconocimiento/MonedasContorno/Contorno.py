# Contornos
from importlib.resources import path
import cv2

#Declaracion de variable que permite definir la ruta de la imagen
path = r'C:\Users\NICOLAS\Desktop\Cursos\Proyectos Python\Reconocimiento\MonedasContorno\contorno.jpg'

#Se define la variable que coniene la imagen a leer
imagen = cv2.imread(path)

#Convertir imagen a escala de grises
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#Obtener la imagen como un umbral
tipo_umbral,umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)

contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#Dibujar los contornos de la imagen, se ingresa la funcion que dibuja los contornos antes de mostrarla
cv2.drawContours(imagen, contorno, -1, (251, 63, 52), 3)
#Se define la funcion que muestra la imagen, se determina el nombre en el primer parametro y la variable que la contiene en el segundo parametro
cv2.imshow('Imagen inicial', imagen)
cv2.imshow('Imagen de ejemplo transformada', grises)
cv2.imshow('Imagen de ejemplo umbral', umbral)


#Se ingresa la funcion que permite que la ventana emergente se quede estatica
#Si es 1 se mantiene por un segundo, si es 0 se queda fija
cv2.waitKey(0)

#Al salir la ventana emergente desaparece las demas
cv2.destroyAllWindows()
