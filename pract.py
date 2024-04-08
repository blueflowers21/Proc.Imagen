# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:52:38 2024

@author: Bruna Antelo
"""

#PRACTICA SEPARAR EN 3 CANALES BGR E IMPRIMIR A ESCALA DE GRIS

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
cv2.waitKey(0)
cv2.destroyAllWindows()

#ELIMINAR EL CIELO (AZUL)


#PINTAR LA FLOR EN DOS COLORES
