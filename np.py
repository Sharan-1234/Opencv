import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype ='uint8')
cv.imshow('blank',blank)

# blank[60:100 , 300:400] = 255,255,255
# cv.imshow('green',blank)
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness = -1)
cv.circle(blank,(0,0),40,(255,0,0,),thickness = -1)
cv.line(blank,(0,0),(250,250),(255,255,255),thickness = 4)
text = cv.putText(blank.copy(), 'Hello',(100,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),2)
cv.imshow('box',blank)
cv.imshow('text',text)
cv.waitKey(0)

