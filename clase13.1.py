import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/flowers.jpg')

fila, colum, _ = img.shape

M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])  

dst1 = cv2.warpAffine(img, M, (colum // 2, fila // 2))
dst2 = cv2.warpAffine(img, M, (colum // 2, fila // 2))
dst3 = cv2.warpAffine(img, M, (colum // 2, fila // 2))
dst4 = cv2.warpAffine(img, M, (colum // 2, fila // 2))

fila_concat1 = cv2.hconcat([dst1, dst2])
fila_concat2 = cv2.hconcat([dst3, dst4])

matriz_img = cv2.vconcat([fila_concat1, fila_concat2])
salida_final = cv2.hconcat([img, matriz_img])

cv2.imshow("Resultado", salida_final)
cv2.waitKey()
cv2.destroyAllWindows()