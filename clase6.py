import numpy as np
import cv2
import matplotlib.pyplot as plt

# Function to print details of the image
def detalles(img):
    print("size: ", img.shape)
    print("max: ", np.max(img))
    print("min: ", np.min(img))

# Read an image
I1 = cv2.imread("images/redgirl.jpg")

# Convert color channels from BGR to RGB
I = I1[:,:,(2,1,0)]

# Show the RGB image
plt.imshow(I)

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

# Show individual color channels
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

# Define the number of bins for histogram
n = 256

# Function to compute and plot histogram
def hist(X, n=n):
    (N, M) = X.shape
    h = np.zeros((n,))
    for i in range(N):
        for j in range(M):
            x = X[i,j]
            h[x] = h[x] + 1
    plt.plot(range(n), h[0:n])
    plt.show()

# Thresholding for red, green, and blue channels
Sr = R > 150
Sg = G < 40
Sb = B < 50

# Concatenate the thresholded images
SRGB = np.concatenate((Sr, Sg, Sb), axis=1)
plt.imshow(SRGB, cmap="gray")

# Logical AND operation for thresholded images
Srg = np.logical_and(Sr, Sg)
S = np.logical_and(Srg, Sb)
plt.imshow(S, cmap="gray")

# Remove rows with low sum
(N, M) = S.shape
Q = S
for i in range(N):
    s = np.sum(S[i,:])
    if s < 10:
        Q[i,:] = 0
plt.imshow(Q, cmap="gray")

# Find bounding box coordinates
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

# Create coordinates for plotting bounding box
y = [imin, imin, imax, imax, imin]
x = [jmin, jmax, jmax, jmin, jmin]


plt.imshow(I)
plt.plot(x, y)
plt.show()
