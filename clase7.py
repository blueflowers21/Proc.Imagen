import numpy as np
import cv2
import matplotlib.pyplot as plt

# Función para imprimir detalles de la imagen
def detalles(img):
    print("size: ", img.shape)
    print("max: ", np.max(img))
    print("min: ", np.min(img))

# Leer la imagen desde el archivo
I1 = cv2.imread("images/flowers.jpg")

# Cambiar el orden de los canales de color de BGR a RGB
I = I1[:,:,(2,1,0)]

# Separar los canales de color
R = I[:,:,0]
G = I[:,:,1]
B = I[:,:,2]

# Concatenar los canales de color para visualización
RGB = np.concatenate((R,G,B), axis=1)

# Función para imprimir imágenes en escala de grises
def imprimir(img):
    plt.imshow(img, cmap="gray")
    plt.show()

# Visualizar la imagen RGB
plt.imshow(RGB, cmap="gray")
plt.title('Imagen RGB')
plt.show()

# Convertir los canales de color a flotante
Rd = R.astype(float)
Gd = G.astype(float)
Bd = B.astype(float)

# Calcular la imagen en escala de grises como la media de los canales de color
Zd = 1/3 * Rd + 1/3 * Gd + 1/3 * Bd
Z = Zd.astype(np.uint8)
plt.imshow(Z, cmap="gray")
plt.title('Imagen en escala de grises')
plt.show()

# Definir el número de bins para el histograma
n = 256

# Función para calcular y mostrar el histograma de una imagen
def hist(X, n=n):
    (N, M) = X.shape
    h = np.zeros((n,))

    for i in range(N):
        for j in range(M):
            x = X[i, j]
            h[x] = h[x] + 1
    plt.plot(range(n), h[0:n])
    plt.title('Histograma')
    plt.show()

# Mostrar histogramas RGB
hist(R.flatten(), n)
hist(G.flatten(), n)
hist(B.flatten(), n)

# Crear máscaras para segmentar la flor
Sr = R > 150
Sg = G < 40
Sb = B < 50

# Combinar las máscaras para obtener la región de interés
SRGB = np.concatenate((Sr, Sg, Sb), axis=1)
plt.imshow(SRGB, cmap="gray")
plt.title('Máscaras combinadas')
plt.show()

# Aplicar operaciones lógicas para refinar la segmentación
Srg = np.logical_and(Sr, Sg)
S = np.logical_and(Srg, Sb)
plt.imshow(S, cmap="gray")
plt.title('Operaciones lógicas')
plt.show()

# Eliminar filas con poca presencia de la región de interés
(N, M) = S.shape
Q = S
for i in range(N):
    s = np.sum(S[i,:])
    if s < 20:
        Q[i,:] = 0
plt.imshow(Q, cmap="gray")
plt.title('Eliminación de filas')
plt.show()

# Encontrar límites de la región de interés
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

# Dibujar el contorno de la flor sobre la imagen original
plt.imshow(I)
plt.plot(x, y, color='red')
plt.title('Contorno de la flor')
plt.show()

# Crear máscara para el borde de la flor (color rojo)
E = np.zeros((N, M), np.uint8)
for i in range(N):
    for j in range(1, M):
        if Q[i,j] != Q[i,j-1]:
            E[i,j] = 1
            E[i,j-1] = 1
for i in range(1, N):
    for j in range(M):
        if Q[i-1,j] != Q[i,j]:
            E[i,j] = 1
            E[i,j-1] = 1

# Unir el borde de la flor a la imagen original
for i in range(N):
    for j in range(M):
        if E[i,j] == 1:
            I[i,j,:] = [200, 5, 255]
plt.imshow(I)
plt.title('Flor enmarcada en la imagen original')
plt.show()
