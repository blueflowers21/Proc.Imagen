import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt
#x = np.array([1,2,3,4])
#print(x.shape)
 
'''y=np.zeros((2,3,4))  #para hacer matrices de ceros de tres filas y cuatro columnas repetidamente 2
print(y)
print(y.shape)
#esto para reformar una matriz
y.shape=(3,8)
print(y)'''
'''X = np.zeros((20,20))
plt.imshow(X,cmap="gray")'''
 
 
x = imread("images/rices.png")
plt.imshow(x)
print(x.shape)
#plt.show()
def details(img):
    print()
    print("size= ",img.shape)
    print("max= ",np.max(img))
    print("min= ",np.min(img))
 
y= x[:,:,0]
details(y)
 
def segmenta(x,t):
    (F,C)=x.shape
    Y = np.zeros((F,C))
    area= 0
    for i in range(F):
        for j in range (C):
            if x[i,j] > t:
                Y[i,j]= 255
                area = area +1 
    print()
    print("area= ", area)
    return Y
Y = segmenta (y,120)
details(Y)
plt.imshow(Y, cmap="gray")
plt.show()


# Read and display an image
x = imread("images/rices.png")  # Read the image "rices.png"
plt.imshow(x)  # Display the image using Matplotlib
print(x.shape)  # Print the shape of the image (height, width, channels)

# Function to print details of an image
def details(img):
    print()
    print("size= ", img.shape)  # Print the shape of the image
    print("max= ", np.max(img))  # Print the maximum pixel value
    print("min= ", np.min(img))  # Print the minimum pixel value

# Extract the first channel of the image
y = x[:,:,0]
details(y)  # Print details of the extracted channel

# Function to segment the image based on a threshold value
def segmenta(x, t):
    (F,C) = x.shape  # Get the shape of the image
    Y = np.zeros((F,C))  # Create an array of zeros with the same shape as the image
    area = 0  # Initialize area counter
    for i in range(F):  # Iterate through the rows
        for j in range(C):  # Iterate through the columns
            if x[i,j] > t:  # Check if pixel value is greater than the threshold
                Y[i,j] = 255  # Set pixel value to 255 (white)
                area = area + 1  # Increment area counter
    print("area= ", area)  # Print the area of the segmented region
    return Y  # Return the segmented image

# Segment the image with a threshold value of 120
Y = segmenta(y, 120)
details(Y)  # Print details of the segmented image
plt.imshow(Y, cmap="gray")  # Display the segmented image using Matplotlib
plt.show()  # Show the plot
