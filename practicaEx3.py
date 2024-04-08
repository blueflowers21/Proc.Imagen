# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:47:24 2024

@author: Bruna Antelo
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("images/flowers.jpg")
fila,col,_=image.shape

inicio=(5,5)
final=(220,220)
color=(255,0,0)
grosor=2
image=cv2.rectangle(image,inicio,final,color,grosor)
cv2.imshow("Ejemplo3",image)

cv2.waitKey(0)

image2 = cv2.imread("images/frutos_rojos.png")

weightedSum=cv2.addWeighted(image,0.5,image2,0.4,0)
cv2.imshow("Weighted Image",weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()

#SUMA DE IMAGENES
 
# Cargar las imágenes
image1 = cv2.imread('images/flowers.jpg')
image2 = cv2.imread('images/seagull.jpg')
 
# Asegurarse de que las imágenes tengan el mismo tamaño
alto, ancho, _ = image1.shape
image2 = cv2.resize(image2, (ancho, alto))  # Redimensionar image2 al tamaño de image1
 
#weightedSum = image1 + image2
 
# Realizar la suma ponderada de las imágenes
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
 
# Mostrar la imagen resultante
cv2.imshow('Ejemplo 4', weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()