import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/flowers.jpg")
fil,col,_ = img.shape

pt_A = [0,0]
pt_B = [0,fil]
pt_C = [fil,col]
pt_D = [col,0]

entrada = np.float32([pt_A,pt_B,pt_C,pt_D])

salida = np.float32([[0,0],
                     [0,fil],
                     [col*0.3,7*fil/20],
                     [col*0.3,0]])

salida1 = np.float32([[col,0],
                     [col,fil],
                     [col*0.7,7*fil/20],
                     [col*0.7,0]])

salida2 = np.float32([[3*col/10,7*fil/20],
                     [0,fil],
                     [fil,col],
                     [7*col/10,7*fil/20]])

M= cv2.getPerspectiveTransform(entrada,salida)
M1= cv2.getPerspectiveTransform(entrada,salida1)
M2= cv2.getPerspectiveTransform(entrada,salida2)
M3= cv2.getRotationMatrix2D(center = (fil/2,col/4),angle = 180,scale = 0.4)


dst=cv2.warpAffine(img,M3,(col,fil))
out=cv2.warpPerspective(img,M,(col,fil), flags = cv2.INTER_LINEAR)
out1=cv2.warpPerspective(img,M1,(col,fil), flags = cv2.INTER_LINEAR)
out2 = cv2.warpPerspective(img,M2,(col,fil), flags = cv2.INTER_LINEAR)

out_final = cv2.hconcat((img,out+out1+out2+dst))

cv2.imwrite("ejm.jpg",out_final)
cv2.imshow("ej",out_final)
cv2.waitKey()
cv2.destroyAllWindows()