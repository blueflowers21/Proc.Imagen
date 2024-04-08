import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('images/flowers.jpg')

kernel1 = np.ones((5,5),np.float32)/90
#Mantiene profundidad al ponerlo en 1
img=cv2.filter2D(src=image,ddepth=-1, kernel=kernel1) 

kernel2= np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
img2= cv2.filter2D(src=image,ddepth=-1,kernel=kernel2)

cv2.imshow("a",img)
cv2.imshow("b",img2)
cv2.waitKey()
cv2.destroyAllWindows()


