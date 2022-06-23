from importlib.resources import path
import cv2
import numpy as np

#Valores de la matriz, que determinan el suavizado, los pixeles a agrupar
valorgauus = 9
valorkernel = 9
path = r'C:\Users\NICOLAS\Desktop\Cursos\Proyectos Python\Reconocimiento\MonedasContorno\monedassoles.jpg'
original = cv2.imread(path)
grises = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)

#Elimina el ruido de la imagen, la desenfoca y agrupa los pixeles, osea los reduce
suavizado = cv2.GaussianBlur(grises, (valorgauus,valorkernel), 0)

#Es un segundo suavizado, que resalta solo las figuras de la imagen
canny = cv2.Canny(suavizado, 60, 100)

#variable que se define
Kernel = np.ones((valorkernel,valorkernel),np.uint8)

#Tomar solo el contorno mayor
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, Kernel)

#Encontrar contornos
contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("monedas encontradas: {}".format(len(contornos)))

cv2.drawContours(original, contornos, -1, (0,0,255), 3)
#Mostrar resulados
#cv2.imshow("Imagen escala de grises", grises)
#cv2.imshow("Imagen con suavizado", suavizado)
#cv2.imshow("Imagen con eliminacion de ruido", canny)
cv2.imshow("Imagen con eliminacion de lo interno del objeto de interes", cierre)
cv2.imshow("Resultado", original)
cv2.waitKey(0)