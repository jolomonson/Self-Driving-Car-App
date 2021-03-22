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
# Video Detection with Cars
import cv2
from random import randrange
video = cv2.VideoCapture('Videos/Pedestrians Compilation_1080pFHR.mp4')
trainedClassifier = cv2.CascadeClassifier('carDetector.xml')
while True:
    #Reading Frame
    read_successful, frame = video.read()
    if read_successful:
        #Covert to grayScale
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    #Detecting Cars
    trainedFrames = trainedClassifier.detectMultiScale(grayFrame)
    #Drawing Rectangles
    coordinates = [cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(256),randrange(256),randrange(256))) for (x,y,w,h) in trainedFrames]
    cv2.imshow('Car Detector[Video]', frame)
    key = cv2.waitKey(1)
    # Stop if Q is pressed
    if key == 81 or key == 113:
        break
video.release()
#Pedestrians Detection
