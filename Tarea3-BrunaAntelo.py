#BRUNA ANTELO PRADO
import numpy as np
import cv2
import matplotlib.pyplot as plt


def detalles(img):
    print("size: ", img.shape)
    print("max: ",np.max(img))
    print("min: ", np.min(img))

I1 = cv2.imread("images/flowers.jpg")


I = I1[:,:,(2,1,0)]

#plt.imshow(I)

R = I[:,:,0]
G = I[:,:,1]
B = I[:,:,2]
RGB = np.concatenate((R,G,B),axis=1)
def imprimir(img):
    plt.imshow(img, cmap="gray")
    plt.show()
    
    
'''imprimir(R)    
imprimir(G)
imprimir(B)'''
    
plt.imshow(RGB, cmap="gray")

Rd = R.astype(float)
Gd = G.astype(float)
Bd = B.astype(float)

Zd = 1/3*Rd + 1/3*Gd +1/3*Bd

Z = Zd.astype(np.uint8)
plt.imshow(Z,cmap="gray")

n= 256
def hist (X,n=n):
    (N,M)=X.shape
    h = np.zeros((n,))

    for i in range(N):
        for j in range(M):
            x = X[i,j]
            h[x]= h[x] + 1
    plt.plot(range(n), h[0:n])
        
    plt.show()

#Solo se cambiaron estos valores para encontrar las partes amarillas de la imagen    
Sr = R>160
Sg = G>160
Sb = B<160

SRGB = np.concatenate((Sr,Sg,Sb),axis=1)

plt.imshow(SRGB, cmap="gray")

Srg= np.logical_and(Sr,Sg)
S= np.logical_and(Srg,Sb)
plt.imshow(S, cmap="gray")

'Para matar filas o las partes isoladas'
(N,M) = S.shape
Q = S
for i in range (N):
    s = np.sum(S[i,:])
    if s<20:
        Q[i,:] = 0
plt.imshow(Q,cmap="gray")

imin = 1000
imax = 0
jmin = 1000
jmax = 0

for i in range (N):
    for j in range (M):
        if Q[i,j]>0:
            if i < imin:
                imin = i
            if i > imax:
                imax = i
            if j < jmin:
                jmin=j
            if j > jmax:
                jmax = j

y = [imin,imin,imax,imax,imin]
x = [jmin,jmax,jmax,jmin,jmin]

plt.imshow(I)
plt.plot(x,y, color='yellow')
plt.show()

#PARA EL BORDE DE LA FLOR COLOR ROJA
E = np.zeros((N,M),np.uint8)
for i in range(N):
    for j in range(1,M):
        if Q[i,j] != Q[i,j-1]:
            E[i,j] = 1
            E[i,j-1] = 1
            
for i in range(1,N):
    for j in range(M):
        if Q[i-1,j] != Q[i,j]:
            E[i,j] = 1
            E[i,j-1] = 1
            

#PARA UNIR 
for i in range(N):
    for j in range(M):
        if E[i,j]==1:
            I[i,j,:]=[0,0,0]
            
plt.imshow(I, cmap="gray")
plt.show()            