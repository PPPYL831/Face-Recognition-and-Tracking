import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 320) # set video width
cam.set(4, 240) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

count = 0

while(True):

    ret, img = cam.read()
    #img = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    key = cv2.waitKey(5) & 0xff # Press 'ESC' for exiting video
    if key == ord('q'):
        break
    elif count >= 200: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
cam.release()
cv2.destroyAllWindows()


