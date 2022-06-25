from importlib.resources import path
from unittest.mock import patch
import cv2
from cv2 import VideoCapture
import numpy as np
path = r'C:\Users\NICOLAS\Desktop\Cursos\Proyectos Python\Reconocimiento\Reconocimientofacial1\haarcascade_frontalface_default.xml'
ruidos= cv2.CascadeClassifier(path)

camara = cv2.VideoCapture(1)
while True:
    _, captura = camara.read()
    grises = cv2.cvtColor(captura, cv2.COLOR_BGR2GRAY)
    cara = ruidos.detectMultiScale(grises, 1.3, 5)
    for(x,y,e1,e2) in cara:
        cv2.rectangle(captura, (x, y), (x+e1,y+e2), (255,0,0), 2)
    cv2.imshow("resultado rostro", captura)

    if cv2.waitKey(1) == ord('q'):
        break
camara.release()
cv2.destroyAllWindows()