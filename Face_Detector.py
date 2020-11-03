import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img2.jpg')

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
print(face_coordinates)

# Draw rectangles
# (x, y, w, h) = face_coordinates[0]

# Detect multiple people - we need to loop through the array
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 6)

# This shows the name of the window that pops up: Clever programmer face detector followed by the image you want to show which we have defined above.
cv2.imshow('Face Detector', img)
cv2.waitKey()

print("Hello")