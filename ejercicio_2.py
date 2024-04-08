import numpy as np
import cv2
import matplotlib.pyplot as plt

I1 = cv2.imread("images/redgirl.jpg")

I = I1[:,:,(2,1,0)]

# Separate RGB channels
R = I[:,:,0]
G = I[:,:,1]
B = I[:,:,2]

Sr = R > 160
Sg = G < 70
Sb = B < 70

S = np.logical_and(Sr, np.logical_and(Sg, Sb))

# matar filas
(N, M) = S.shape
Q = S
for i in range(N):
    s = np.sum(S[i,:])
    if s < 10:
        Q[i,:] = False

#Copiar imagen
result = np.copy(I)
result[~Q] = result[~Q].mean(axis=-1, keepdims=True)

plt.imshow(result)
plt.show()
