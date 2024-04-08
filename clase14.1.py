import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/flowers.jpg")
row,col,_ = img.shape
M = np.float32 ([[0.5,0,8.0],[0.8,0.5,0]])

M2= cv2.getRotationMatrix2D(center=(2,0), angle=30, scale=0.5)

dst = cv2.warpAffine(img, M, (col,row))
out= cv2.hconcat((img,dst))
cv2.imshow("ejemplo", out)
cv2.waitKey()
cv2.destroyAllWindows()