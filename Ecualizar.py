# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:49:30 2024

@author: Bruna Antelo
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("valeria.png")
#plt.imshow(img, cmap="gray")
#plt.show()

def ecualizar(canal):
    Xc = canal.copy()
    X1 = 255 * ((Xc - Xc.min()) / (Xc.max() - Xc.min()))
    return X1.astype(np.uint8)


B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]

B_e = ecualizar(B)
G_e = ecualizar(G)
R_e = ecualizar(R)


img_ecualizada = np.stack((R_e, G_e, B_e), axis=-1)
plt.imshow(img_ecualizada)
plt.show()