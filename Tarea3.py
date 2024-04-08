import numpy as np
import cv2
import matplotlib.pyplot as plt

def details(img):
    print("size: ", img.shape)
    print("max: ", np.max(img))
    print("min: ", np.min(img))

I1 = cv2.imread("images/flowers.jpg")
I = I1[:, :, (2, 1, 0)]

R = I[:, :, 0]
G = I[:, :, 1]
B = I[:, :, 2]


yellow = 160

# Mascara binaria para los canales de los colores R,G,B 
Sr = R > yellow
Sg = G > yellow
Sb = B < yellow

# Combinar las mascaras
S = np.logical_and(Sr, np.logical_and(Sg, Sb))

# Para matar filas, osea regiones isoladas 
(N, M) = S.shape
Q = S.copy()
for i in range(N):
    s = np.sum(S[i, :])
    if s < 20:
        Q[i, :] = 0

# coordenadas del enmarcado
imin = 1000
imax = 0
jmin = 1000
jmax = 0

for i in range(N):
    for j in range(M):
        if Q[i, j] > 0:
            if i < imin:
                imin = i
            if i > imax:
                imax = i
            if j < jmin:
                jmin = j
            if j > jmax:
                jmax = j

y = [imin, imin, imax, imax, imin]
x = [jmin, jmax, jmax, jmin, jmin]

# Display the original image with the bounding box
plt.imshow(I)
plt.plot(x, y, color='yellow', linewidth=2)
plt.show()



