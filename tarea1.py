import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt

x = imread("escala.jpg")
 
def invertir_eje_x(img):
    return img[:, ::-1]
 
x_invertida = invertir_eje_x(x)
 
plt.imshow(x_invertida)
plt.show()
