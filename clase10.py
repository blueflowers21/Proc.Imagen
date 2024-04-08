import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/KID.png")

img1 = img[:,:,0]
plt.imshow(img1, cmap="gray")
plt.show()
flat = img1.flatten()
Xc = img1.copy()
X1 = 255* ((Xc - Xc.min())/(Xc.max() - Xc.min()))
X1 = X1.astype(np.uint8)

plt.imshow(X1,cmap="gray")
plt.show()

#plt.hist(flat,bins=256)

#plt.show()
def histograma(a,bins):
    histo = np.zeros(bins)
    for pixel in a:
        histo[pixel]+=1
    return histo
X3= cv2.equalizeHist(img1)

res = np.hstack((img1,X1,X3))
plt.imshow(res,cmap="gray")
plt.show()

histo1 = histograma(img1,256)
plt.plot(histo1)
#plt.show()


histo2 = histograma(X1, 256)
plt.plot(histo2)

histo3 = histograma(X3, 256)
plt.plot(histo3)