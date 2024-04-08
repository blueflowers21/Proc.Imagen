import numpy as np
import cv2
import matplotlib.pyplot as plt

def detalles(img):
    print("size: ", img.shape)
    print("max: ", np.max(img))
    print("min: ", np.min(img))

x = cv2.imread("images/pato.jpg")

I = x[:,:,(2,1,0)]
I2 = x[:,:,0]

# Separate RGB channels
R = I[:,:,0]
G = I[:,:,1]
B = I[:,:,2]

# Concatenate RGB channels for visualization
RGB = np.concatenate((R,G,B), axis=1)

# Function to print and show an image
def imprimir(img):
    plt.imshow(img, cmap="gray")
    plt.show()

imprimir(R)
imprimir(G)
imprimir(B)

# Show the RGB image
plt.imshow(RGB, cmap="gray")

# Convert RGB channels to float
Rd = R.astype(float)
Gd = G.astype(float)
Bd = B.astype(float)

# Compute the average of RGB channels
Zd = 1/3 * Rd + 1/3 * Gd + 1/3 * Bd

# Convert the result back to uint8
Z = Zd.astype(np.uint8)
plt.imshow(Z, cmap="gray")

n = 256

def histo(X):
    (N, M) = X.shape
    n = 256
    h = np.zeros((n,), np.uint8)
    for i in range(N):
        for j in range(M):
            x = X[i, j]
            h[x] = h[x] + 1
    plt.plot(range(n), h[0:n])
    plt.show()

Sr = R > 150
Sg = G < 150
Sb = B < 40

SRGB = np.concatenate((Sr, Sg, Sb), axis=1)
plt.imshow(SRGB, cmap="gray")

Srg = np.logical_and(Sg, Sg)
S = np.logical_and(Srg, Sb)
plt.imshow(S, cmap="gray")

# Matar filas
(N, M) = S.shape
Q = S
for i in range(N):
    s = np.sum(S[i,:])
    if s < 20:
        Q[i,:] = 0
plt.imshow(Q, cmap="gray")

imin = 1000
imax = 0
jmin = 1000
jmax = 0
for i in range(N):
    for j in range(M):
        if Q[i,j] > 0:
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

plt.imshow(I)
plt.plot(x, y)
plt.show()


plt.hist(R.ravel(), bins=255, range=(0, 255), histtype="step", color='red')
plt.hist(B.ravel(), bins=255, range=(0, 255), histtype="step", color='blue')
plt.hist(G.ravel(), bins=255, range=(0, 255), histtype="step", color='green')
plt.show()
