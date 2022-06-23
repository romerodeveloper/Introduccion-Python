# CONTORNOS
Se veran los conceptos principales para la creacion de contornos de una imagen, en el archivo "contorno.py" se muestra el proceso de la creacion de los contornos de una imagen con diversas figuras geometricas, en el archivo "cntadorMonedas.py" se realiza el proceso de creacion de contornos a una imagen real, la cual se pretende contar el numero de objetos o monedas que se encuentran en el mismo..

## Requerimientos
Como principal requerimiento debe de instalarse una libreria de OpenCv. A continuacion el comando de instalacion.
 
 ``` PY
 pip install opencv-contrib-python
 ```

 Al finalizar la instalacion se podra usar la liberia de OpenCv de la siguiente maneras
``` PY
import cv2
```

## Tip importante
Al indicar la ubicacion de imagen o archivo, probablemente se obtenga un error por lo cual es necesario de enviar la ruta completa de la imagen, en el ejemplo propuesto en los ejercicios de contornos, se define una variable path la cual nos ayuda a indicar la ruta especifica. Para el uso de esta variable se traera automaticamente la libreria que se indica en la siguiente sentencia.

```PY
from importlib.resources import path

path = r'C:\Users\NICOLAS\Desktop\Cursos\Proyectos Python\Reconocimiento\MonedasContorno\monedassoles.jpg'
```

## Recursos
Si se requiere de una guia mas detallada, puede ingresar a la documentacion de OpenCv [aqui](https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html). 
