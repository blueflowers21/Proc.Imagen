# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:11:54 2024

@author: Bruna Antelo
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("images/flowers.jpg")
fila,col,_=image.shape

cantidad=3
numeros=int(col/cantidad)
font=cv2.FONT_HERSHEY_SIMPLEX
org=(50,50)
fontScale=1
color=(255,0,0)
grosor=2


for i in range (0,col,numeros):
    img1 = cv2.line(image,(i,0),(i,fila),(255,0,0),4)
    image = cv2.putText(image,"a",org,font,fontScale,color,grosor)
    
    
for i in range (0,col,numeros):
    img1 = cv2.line(image,(0,i),(col,i),(255,0,0),4)
    

cv2.imshow("EJEMPLO 1",img1)
cv2.waitKey(0)

font=cv2.FONT_HERSHEY_SIMPLEX
org=(50,50)
fontScale=1
color=(255,0,0)
grosor=2
image = cv2.putText(image,"OpenCV",org,font,fontScale,color,grosor)


cv2.imshow("EJEMPLO 2",image)

cv2.waitKey(0)

cv2.destroyAllWindows()