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
cv2.imshow('Car Detection[Image]', img)
cv2.waitKey()
print('Code Completed')

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
    cv2.imshow('Car Detection[Video]', frame)
    key = cv2.waitKey(1)
    # Stop if Q is pressed
    if key == 81 or key == 113:
        break
video.release()

#Video Detection with Pedestrians
import cv2
from random import randrange
video = cv2.VideoCapture('Videos/Pedestrians Compilation_1080pFHR.mp4')
trainedClassifier = cv2.CascadeClassifier('pedestrianDetector.xml')
while True:
    readSuccessful, frame = video.read()
    if readSuccessful:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#Coverting the color
    else:
        break
    trainedFrames = trainedClassifier.detectMultiScale(grayFrame)
    coordinates = [cv2.rectangle(frame, (x,y),(x+w, y+h),(randrange(256),randrange(256),randrange(256)), 1) for (x,y,w,h) in trainedFrames]
    cv2.imshow('Detecting Pedestrians', frame)
    key = cv2.waitKey(1)
    # Stop if Q is pressed
    if key == 81 or key == 113:
        break

video.release()
'''
#Video Detection with cars and pedestrians
import cv2
from random import randrange
video = cv2.VideoCapture('Videos/Pedestrians Compilation_1080pFHR.mp4')
trainedCarClassifier = cv2.CascadeClassifier('carDetector.xml')
trainedPedestrianClassifier = cv2.CascadeClassifier('pedestrianDetector.xml')
while True:
    (readSuccessful, frame) = video.read()
    if readSuccessful:
        #Converting colored frame to gray
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Getting Coordinates(Car and Pedestrians) from each specified frame
        trainedCarFrame = trainedCarClassifier.detectMultiScale(grayFrame)
        trainedPedestrianFrame = trainedPedestrianClassifier.detectMultiScale(grayFrame)
        #Drawing Rectangles on frames
        carCoordinates = [cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1) for (x,y,w,h) in trainedCarFrame]
        pedestrianCoordinates = [cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) for (x,y,w,h) in trainedPedestrianFrame]
        #Displaying each trained frame of cars and pedestrians respectively
        cv2.imshow('Car and Pedestrians Detection',frame)
    else:
        break

    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

video.release()
print(trainedCarFrame)
