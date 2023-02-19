import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lab.jpg')
cv.imshow('lab',img)

blank = np.zeros(img.shape[:2],dtype = 'uint8')
cv.imshow('blank',blank)

circle = cv.circle(blank,(300,300),100,(255,255,255),thickness = -1)
cv.imshow('circle',circle)

mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('mask',mask)
colors = ('b','g','r')

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)