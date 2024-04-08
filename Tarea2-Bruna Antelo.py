import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt

def details(img):
    print('size = ', img.shape)
    print('max = ', np.max(img))
    print('min = ', np.min(img))

img = imread("images.jpg")
X = img[:,:,0]
plt.figure(figsize=(8,8))
#plt.imshow(X,cmap="gray")
#plt.show()

#Sacamos filas y columnas
d = 8 #paso
(Nx,Mx) = X.shape  #Nx el numero de filas , Mx son las columnas 
ix = range (0,Nx,d)
jx = range(0,Mx,d)
Ny = len(ix) 
My = len(jx)

#Muestreo de imagen 
Y = np.zeros((Ny,My),np.uint8) #uint8 valores enteros
Y = X[np.ix_(ix, jx)]  #np.ix_ para indexar las filas y columnas de la matriz X
       
plt.figure(figsize = (8,8))
plt.imshow(Y, cmap="gray")
plt.show()
details(Y)

#Sin usar la libreria de numpy
def hist(X, n=256):
    h = np.zeros(n, dtype=np.uint32) 
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            x = X[i, j]
            h[x] += 1
    return h

#Usando la libreria numpy, existe ya una función que uno solo le da los valores que necesita para hacer el histograma
def hist2(X, n=256):
    h, _ = np.histogram(X.flatten(), bins=n, range=(0, n))
    return h

n= 256
h = hist(Y, n=n)
plt.figure(figsize=(12,8))
plt.plot(range(n),h[0:n])
plt.show()

n= 256
h = hist2(Y, n=n)
plt.figure(figsize=(12,8))
plt.plot(range(n),h[0:n])
plt.show()
