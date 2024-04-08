import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt

# Leer la imagen "images.jpg" utilizando imread de OpenCV
img = imread("images.jpg")

# Función para imprimir detalles de la imagen
def details(img):
    print("size= ", img.shape)  # Imprime la forma de la imagen
    print("max= ", np.max(img))  # Imprime el valor máximo de los píxeles
    print("min= ", np.min(img))  # Imprime el valor mínimo de los píxeles

# Imprimir la forma de la imagen
print(img.shape)    

# Leer nuevamente la imagen "images.jpg" para asegurar que la imagen esté disponible
img = imread("images.jpg")

# Extraer el primer canal de la imagen (asumiendo que es una imagen en escala de grises)
X = img[:,:,0]

# Definir el tamaño de paso para el submuestreo
d = 8

# Obtener las dimensiones de la imagen original
(Nx, Mx) = X.shape

# Definir los índices para el submuestreo
ix = range(0, Nx, d)
jx = range(0, Mx, d)

# Calcular las nuevas dimensiones después del submuestreo
Ny = len(ix)
My = len(jx)

# Crear una matriz para la imagen submuestreada
Y = np.zeros((Ny, My), np.uint8)

# Realizar el submuestreo
for i in range(Ny):
    for j in range(My):
        Y[i, j] = X[ix[i], jx[j]]

# Mostrar la imagen submuestreada
plt.figure(figsize=(8,8))
plt.imshow(Y, cmap="gray")
plt.show()

# Imprimir detalles de la imagen submuestreada
details(Y)

# Función para calcular el histograma de la imagen
def hist(X, n=256):
    (N, M) = X.shape
    h = np.zeros((n,))
    for i in range(N):
        for j in range(M):
            x = X[i, j]
            h[x] = h[x] + 1
    return h

# Definir el número de bins del histograma
n = 256

# Calcular el histograma de la imagen submuestreada
h = hist(Y, n=n)

# Visualizar el histograma
plt.figure(figsize=(12, 8))
plt.plot(range(n), h[0:n])
plt.show()

# Definir el tamaño del paso para la cuantificación
p = 64

# Obtener las dimensiones de la imagen original
(Nx, Mx) = X.shape

# Crear una matriz para la imagen cuantificada
Y = np.zeros((Ny, My), np.uint8)

# Realizar la cuantificación
for i in range(Ny):
    for j in range(My):
        x = int(np.fix(X[i, j] / p) * p)
        Y[i, j] = x

# Mostrar la imagen cuantificada
plt.imshow(Y, cmap="gray")

# Calcular el histograma de la imagen cuantificada
hist(Y, n=n)
