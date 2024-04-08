import numpy as np
import cv2 
import matplotlib.pyplot as plt

# Lee la imagen "lego.jpg" utilizando OpenCV
B = cv2.imread("lego.jpg")

# Reordena los canales de la imagen para tener el formato RGB en lugar de BGR
img = B[:, :, (2, 1, 0)]

# Extrae los canales de color R (rojo), G (verde) y B (azul)
R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

# Calcula el valor promedio de los canales R, G y B
valor = 0.333
X = valor * R + valor * G + valor * B

# Concatena los canales R, G y B horizontalmente para visualizarlos juntos
RGB = np.concatenate((R, G, B), axis=1)

# Función para imprimir detalles de la imagen
def details(img):
    print("size= ", img.shape)  # Imprime la forma de la imagen
    print("max= ", np.max(img))  # Imprime el valor máximo de los píxeles
    print("min= ", np.min(img))  # Imprime el valor mínimo de los píxeles

# Imprime detalles de los canales R, G y B
print("ROJO")
details(R)
print("VERDE")
details(G)
print("AZUL")
details(B)

# Muestra la imagen resultado (X) en escala de grises
plt.imshow(X, cmap="gray")
plt.show()
