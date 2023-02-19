import cv2 as cv

img = cv.imread('v-2.jpg')
cv.imshow('face',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_casacde = cv.CascadeClassifier('haar_face.xml')

faces = haar_casacde.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 3)
print("the number of faces",len(faces))

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('detected',img)
cv.waitKey(0)