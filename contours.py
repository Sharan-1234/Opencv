import cv2 as cv
import numpy as np

img = cv.imread('Screenshot (133).png')
cv.imshow('img',img)
res = cv.resize(img,(500,500),interpolation = cv.INTER_AREA)
cv.imshow('res',res)
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayimg',grey)

blur = cv.blur(img,(5,5))
cv.imshow('blur',blur)
cv.waitKey(0)
