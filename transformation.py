import cv2 as cv
import numpy as np

img = cv.imread('Screenshot (133).png')
cv.imshow('notrans',img)

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimen = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimen)
translated = translate(img,100,300)
cv.imshow('yestrans',translated)
cv.waitKey(0)

#rotate