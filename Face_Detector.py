import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img2.jpg')

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
print(face_coordinates)

# Draw rectangles

cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 2), 2)

# This shows the name of the window that pops up: Clever programmer face detector followed by the image you want to show which we have defined above.
cv2.imshow('Face Detector', grayscaled_img)
cv2.waitKey()

print("Hello")