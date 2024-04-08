import numpy as np
import cv2 
import matplotlib.pyplot as plt

# Leer la imagen
x = cv2.imread("rojos.png")

# Convert color channels from BGR to RGB
x = x[:,:,0]

# Definir una función para calcular y mostrar el histograma de la imagen
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


plt.hist(x, bins=30, range=(0, 25), histtype="step")
plt.show()

# Mostrar el histograma utilizando la función histo
histo(x)
