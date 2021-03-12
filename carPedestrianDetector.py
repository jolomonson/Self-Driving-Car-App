import cv2
from random import randrange
#our image file
img = cv2.imread('Images/carFleet.jfif')
#our pre-trained car classifier
carTracker = cv2.CascadeClassifier('carDetector.xml')
#Convert to grayscaled image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Classfying Image
trainedImage = carTracker.detectMultiScale(grayImg)
#print(trainedImage)
print(trainedImage)
#Draw Rectangles
jed = [cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1) for (x,y,w,h) in trainedImage]
#Displaying Images
cv2.imshow('Car Detector', img)
cv2.waitKey()
print('Code Completed')

'''
# Video Detection
video = cv2.VideoCapture('Videos/')
trainedClassifier = cv2.CascadeClassifier('carDetector.xml')
while True:
    #Reading Frame
    read_successful, frame = video.read()
    
'''