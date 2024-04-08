import numpy as np
import cv2

image = cv2.imread("images/frutos_rojos.png")
N,M,L = image.shape

#image.shape para ver el tamaño de la imagen en consola

#para cambiar el tamaño
#img_pequeño = cv2.resize(image, (200,200), interpolation=cv2.INTER_LINEAR)
#img_grande = cv2.resize(image, (600,800), interpolation = cv2.INTER_LINEAR)
cv2.imshow("orginial",image)

#usar factores para reducir o agrandar , reducir<1    agrandar>1
#img_small = cv2.resize(image,None,fx = 0.6,fy=0.6, interpolation = cv2.INTER_LINEAR)
img_grande = cv2.resize(image, None, fx = 1.3, fy = 1.3, interpolation=cv2.INTER_LINEAR)
eg=1.3
img_gn = cv2.resize(image, None, fx = eg, fy = eg, interpolation=cv2.INTER_NEAREST)
img_ga = cv2.resize(image, None, fx = eg, fy = eg, interpolation=cv2.INTER_AREA)

#cv2.imshow("pequeño",img_small)
#cv2.imshow("grande lineal",img_grande)
#cv2.imshow("grande cercano",img_gn)
#cv2.imshow("grande area",img_ga)
#cv2.imwrite("inter lineal",img_grande)

cortar2 = image[1:1,150:300]
cortar = image[100:300,150:300]
cv2.imshow("corte",cortar)
cv2.imshow("corte",cortar2)
cv2.waitKey() #para que acepte cualquier tecla y se destruya/cierre
cv2.destroyAllWindows()