# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:41:50 2024

@author: Bruna Antelo
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

#ENUMERAR LAS CUADRICULAS
image = cv2.imread("images/frutos_rojos.png")
fila,col,_=image.shape
# Crear una copia de la imagen original
image_cuadriculas_enumeradas = image.copy()

numero_cuadriculas = 8  # Número de cuadrículas en una fila/columna
tamano_cuadriculas = min(fila, col) // numero_cuadriculas  # Tamaño de cada cuadrícula

 
# Definir parámetros para el dibujo de líneas y texto
color = (0, 255, 0)  # Color verde para las líneas
grosor = 2
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color_texto = (0, 0, 255)  # Color rojo para el texto
 
# Dibujar y enumerar cuadrículas
contador = 1
for fila in range(numero_cuadriculas):
    for columna in range(numero_cuadriculas):
        # Calcular coordenadas de inicio y fin para cada cuadrícula
        inicio = (columna * tamano_cuadriculas, fila * tamano_cuadriculas)
        final = ((columna + 1) * tamano_cuadriculas, (fila + 1) * tamano_cuadriculas)
        # Dibujar línea para la cuadrícula
        image_cuadriculas_enumeradas = cv2.rectangle(image_cuadriculas_enumeradas, inicio, final, color, grosor)
        # Calcular posición para el texto (centro de la cuadrícula)
        pos_texto = ((inicio[0] + final[0]) // 2, (inicio[1] + final[1]) // 2)
        # Agregar número al centro de la cuadrícula
        image_cuadriculas_enumeradas = cv2.putText(image_cuadriculas_enumeradas, str(contador), pos_texto, font, fontScale, color_texto, grosor)
        contador += 1  # Incrementar el contador
 
# Mostrar la imagen resultante
cv2.imshow("Trabajo 1 - Cuadrículas Enumeradas", image_cuadriculas_enumeradas)
cv2.waitKey(0)
cv2.destroyAllWindows()