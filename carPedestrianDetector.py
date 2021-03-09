import cv2
from random import randrange
#our image file
img = cv2.imread('Images/cars3.png')
#our pre-trained car classifier
carTracker = cv2.CascadeClassifier('carDetector.xml')
#Convert to grayscaled image
grayScaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Classfying Image
trainedImage = carTracker.detectMultiScale(grayScaled)
#print(trainedImage)
#Draw Rectangles
for x,y,w,h in trainedImage:
    cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)))
cv2.imshow('Fleet of cars', img)
cv2.waitKey()
print('Code Completed')