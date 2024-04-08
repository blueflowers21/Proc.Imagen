import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt

def detalles(img):
    print('size = ', img.shape)
    print('max = ', np.max(img))
    print('min = ', np.min(img))

img = imread("Sephiroth.bmp")
X = img[:,:,0]
plt.figure(figsize=(8,8))
#plt.imshow(X,cmap="gray")
#plt.show()

#Procede a comentar todo

#Iniciaremos a sacar un muestreo
#Sacamos filas y columnas
#Nx el numero de filas de nuestra imagen y d es el paso
d = 8
(Nx,Mx) = X.shape
ix = range (0,Nx,d)
jx = range(0,Mx,d)
#Estas varaibles es para saber que tan grande son o que valores tomamos.
Ny = len(ix) 
My = len(jx)

#Ahora viene el muestreo // uint8 es valor enteros *sin decimales*
Y = np.zeros((Ny,My),np.uint8)
for i in range(Ny):
    for j in range(My):
        Y[i,j]= X[ix[i],jx[j]]
        
plt.figure(figsize = (8,8))
plt.imshow(Y, cmap="gray")
plt.show()
detalles(Y)

n = 256
def hist (X,n=n):
    (N,M) =X.shape
    h = np.zeros((n))
    for i in range (N):
        for j in range (M):
            x= X[i,j]
            h[x]= h[x]+1
    return h

n= 256
h = hist(Y, n=n)
plt.figure(figsize=(12,8))
plt.plot(range(n),h[0:n])
plt.show()

import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt

# Función para imprimir detalles de la imagen
def detalles(img):
    print('size = ', img.shape)
    print('max = ', np.max(img))
    print('min = ', np.min(img))

# Leer la imagen
img = imread("images/flowers.jpg")

# Extraer el canal de color azul (en este caso, estamos asumiendo que es una imagen en escala de grises)
X = img[:,:,0]

# Crear una figura de tamaño 8x8
plt.figure(figsize=(8,8))

# Comentar o descomentar según sea necesario para mostrar la imagen
# plt.imshow(X, cmap="gray")
# plt.show()

# Realizar muestreo
d = 8  # Tamaño del paso para el muestreo
(Nx, Mx) = X.shape  # Obtener dimensiones de la imagen original
ix = range(0, Nx, d)  # Índices de filas
jx = range(0, Mx, d)  # Índices de columnas
Ny = len(ix)  # Número de filas muestreadas
My = len(jx)  # Número de columnas muestreadas

# Crear una matriz para el muestreo
Y = np.zeros((Ny, My), np.uint8)

# Realizar el muestreo
for i in range(Ny):
    for j in range(My):
        Y[i, j] = X[ix[i], jx[j]]

# Mostrar la imagen muestreada
plt.figure(figsize=(8,8))
plt.imshow(Y, cmap="gray")
plt.show()

# Imprimir detalles de la imagen muestreada
detalles(Y)

# Función para calcular el histograma de una imagen
n = 256
def hist(X, n=n):
    (N, M) = X.shape
    h = np.zeros((n))
    for i in range(N):
        for j in range(M):
            x = X[i, j]
            h[x] = h[x] + 1
    return h

# Calcular el histograma de la imagen muestreada
n = 256
h = hist(Y, n=n)

# Visualizar el histograma
plt.figure(figsize=(12,8))
plt.plot(range(n), h[0:n])
plt.show()

