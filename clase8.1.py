import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt

x = imread("onerice.bmp")
plt.imshow(x)
x= x[:,:,0]

def histo(X):
    (N,M) = X.shape
    n=256
    h = np.zeros((n,),np.uint8)
    for i in range (N):
        for j in range (M):
            x= X[i,j]
            h[x]=h[x]+1
    plt.plot(range(n), h[0:n])
    plt.show()
    
plt.hist(x,bins=30, range=(0,25),histtype="step")
plt.show()
histo(x)

''' Que hizo el ing en consola tambien podemos traducirlo
a codigo 

Si quiero sacar el histograma de la imagen original en la consola debo escribir
plt.hist(x)

(N,M) = x.shape

N
(apareceria 340 o 64)

M
(apareceria 340 o 64)

l=x (crea una copia)

l.shape=(N*M)

l (se imprime y luego)

y de ahi utilizamos

plt.hist(l y modificamos bins=30, range (0,25) , histtype = "step")
Tomar en cuenta que los valores son bins => plt.hist(x, bins=256, range(0,255), hysttype="step" '''