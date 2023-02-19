import cv2 as cv
import numpy as np

img = cv.imread('img.JPG')
cv.imshow('img',img)

blank = np.zeros(img.shape[0:2], dtype= 'uint8')
cv.imshow('blank',blank)

mask = cv.circle(blank,(100,100),90,(255,255,255),thickness=-1)
cv.imshow('mask',mask)

bitwise = cv.bitwise_and(img,img,mask=mask)
cv.imshow('bitwise',bitwise)
cv.waitKey(0)
