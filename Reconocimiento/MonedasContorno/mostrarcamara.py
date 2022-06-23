from ast import While
import cv2

capturavideo = cv2.VideoCapture(1)

if not capturavideo.isOpened():
    print("No se encontro una camara")
    exit()

while True:
    tipocamara, camara = capturavideo.read()
    grises = cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY)
    cv2.imshow("En vivo", grises)
    if cv2.waitKey(1) == ord("q"):
        break

capturavideo.release()
cv2.destroyAllWindows()