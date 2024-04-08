# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:42:19 2024

@author: Bruna Antelo
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("images/flowers.jpg")
B,G,R=cv2.split(image)
cv2.imshow("original",image)
cv2.waitKey(0)

cv2.imshow("blue",B)
cv2.waitKey(0)

cv2.imshow("Green",G)
cv2.waitKey(0)

cv2.imshow("Red",R)


#cv2.line(image,start_point,end_point,color,thickness)

inicio=(0,0)
final=(250,250)
color = (255,0,0) #COMBINACION DE BGR
grosor=9
image = cv2.line(image,inicio,final,color,grosor)

inicio_y = 0
final_y = image.shape[0]

rango=5

for i in range(rango):
    x = (i + 1) * 35 #posicion x que debe cambiar con cada iteracion

    inicio = (x, inicio_y)
    final = (x, final_y)

    cv2.line(image, inicio, final, color, grosor)
 
inicio_x = 0
final_x = image.shape[0]

for j in range(rango):
    j = (j + 1) * 35 #posicion x que debe cambiar con cada iteracion

    inicio = (inicio_x, j)
    final = (final_x, j)

    cv2.line(image, inicio, final, color, grosor)

cv2.imshow("EJEMPLO 1",image)
cv2.waitKey(0)

cv2.destroyAllWindows()

def details(image):
    print("size= ", image.shape)  # Imprime la forma de la imagen
    print("max= ", np.max(image))  # Imprime el valor máximo de los píxeles
    print("min= ", np.min(image))  # Imprime el valor mínimo de los píxeles

    
   
details(image)