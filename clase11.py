import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("x/x1.png")

img1 = img[:,:,0]

img2 = cv2.imread("x/x2.png")

img3 = img2[:,:,0]

#TIENEN QUE SER DEL MISMO TAMAÑO LAS FOTOS PARA HACER LA SUMA Y RESTA PONDERADA
x3_r = cv2.resize(img1, (334,326), interpolation=cv2.INTER_LINEAR)
x1_r = cv2.resize(img3, (334,326), interpolation=cv2.INTER_LINEAR)

#SUMA
Xc = x1_r.copy()
Xd = x3_r.copy()
Y=(0.5*Xc)+(0.5*Xd)

Y = Y.astype(np.uint8)

plt.imshow(Y,cmap="gray")
plt.show()

#RESTA
Xc = x1_r.copy()
Xd = x3_r.copy()
YR=(0.5*Xc)-(0.5*Xd)

YR = YR.astype(np.uint8)

plt.imshow(YR,cmap="gray")
plt.show()

#MULTIPLICACIÓN

imgm = cv2.imread("x/x7.png")

imgm1 = imgm[:,:,0]

imgm2 = cv2.imread("x/x8.png")

imgm3 = imgm2[:,:,0]



x3_r = cv2.resize(imgm1, (334,326), interpolation=cv2.INTER_LINEAR)
x1_r = cv2.resize(imgm3, (334,326), interpolation=cv2.INTER_LINEAR)

imgm3 = img2[:,:,0]

def segmenta(x, t):
    (F,C) = x.shape  # Get the shape of the image
    Y = np.zeros((F,C))  # Create an array of zeros with the same shape as the image
    area = 0  # Initialize area counter
    for i in range(F):  # Iterate through the rows
        for j in range(C):  # Iterate through the columns
            if x[i,j] > t:  # Check if pixel value is greater than the threshold
                Y[i,j] = 255  # Set pixel value to 255 (white)
                area = area + 1  # Increment area counter
    print("area= ", area)  # Print the area of the segmented region
    return Y  # Return the segmented image

Xc = x1_r.copy()
Xd = segmenta(x3_r, 120)
Ym=(0.5*Xc)*(0.5*Xd)

Ym = Ym.astype(np.uint8)

plt.imshow(Ym,cmap="gray")
plt.show()

