import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('lab.jpg')
cv.imshow('lab',img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# blank = np.zeros(img.shape[:2],dtype = 'uint8')
# circle = cv.circle(blank,(250,250),100,(255,255,255),-1)
# mask = cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow('nask',mask)

# gray_hist = cv.calcHist([img],[0],mask,[256],[0,256])

plt.figure()
plt.title('hist')
plt.xlabel('Bins')
plt.ylabel('Soething')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
# plt.plot(gray_hist)
# plt.xlim([0,256])
plt.show()
cv.waitKey(0)