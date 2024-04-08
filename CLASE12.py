import numpy as np
import cv2
import matplotlib.pyplot as plt

I1 = cv2.imread("lego.jpg")

I = I1[:,:,(2,1,0)]

#plt.imshow(I)

k = 4 #si se quiere que aparezca mas colores, cambiar esto

pixel = I.reshape((-1,3))
pixel = np.float32(pixel)

criteria = (cv2.TERM_CRITERIA_EPS +cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
compactness,labels, (centers)=cv2.kmeans(pixel,k, None, criteria, 100, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
labels = labels.flatten()

segmen = centers[labels]
segmen = segmen.reshape(I.shape)

plt.imshow(segmen)
plt.show()

