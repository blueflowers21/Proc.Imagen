import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt

# Example demonstrating numpy array shapes
'''
x = np.array([1,2,3,4])
print(x.shape)

y = np.zeros([2,3,4])
print(y.shape)

y.shape = (3,8)

print(y)
'''

# Reading an image using OpenCV and displaying it using matplotlib
x = imread("onerice.bmp")
plt.imshow(x)

# Function to print details of an image array
def detalles(img):
    print()
    print("size= ", img.shape)
    print("max= ", np.max(img))
    print("min= ", np.min(img))

y = x[:,:,0] # Extracting the first channel of the image
detalles(y)

# Function to segment an image based on a threshold value
def segmenta(x, t):
    (F, C) = x.shape
    Y = np.zeros((F, C), np.uint8)
    area = 0
    for i in range(F):
        for j in range(C):
            if x[i, j] > t:
                Y[i, j] = 255
                area = area + 1
    print("area= ", area)
    return Y

# Segmenting the image
Y = segmenta(y, 120)
detalles(Y)
plt.imshow(Y, cmap="gray")
plt.show()

'''
x=np.zeros((20,20))
plt.imshow(x,cmap='gray')

x[0,0]=255;plt.imshow(x,cmap="gray")'''

'''
# Creating a 20x20 pixel matrix with all values set to 0 (black)
imagen = np.zeros((20, 20))

# Defining the points forming the letter "D" (in coordinates (row, column))
points_d = [(0, 0), (0, 1), (0, 2),
            (1, 0),
            (2, 0),
            (3, 0), (3, 1), (3, 2)]

# Assigning the value 255 (white) to the pixels forming the letter "D"
for point in points_d:
    imagen[point] = 255

# Displaying the image
plt.imshow(imagen, cmap="gray")
plt.show()'''
