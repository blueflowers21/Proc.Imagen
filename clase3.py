import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt

X = np.zeros((20, 20))


plt.imshow(X, cmap="gray")
plt.show()


x = imread("onerice.bmp")