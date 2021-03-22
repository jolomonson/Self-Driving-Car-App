#Image Detection with Cars
'''
import cv2
from random import randrange
#our image file
img = cv2.imread('Images/Cars/carFleet.jfif')
import cv2
from random import randrange
#our image file
img = cv2.imread('Images/carFleet.jfif')
#our pre-trained car classifier
carTracker = cv2.CascadeClassifier('carDetector.xml')
#Convert to grayscaled image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Classfying Image
imageCoordinate = carTracker.detectMultiScale(grayImg)
#print(trainedImage)
print(imageCoordinate)
#Draw Rectangles
jed = [cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1) for (x,y,w,h) in imageCoordinate]
#Displaying Images
cv2.imshow('Car Detector[Image]', img)
cv2.waitKey()
print('Code Completed')
'''
