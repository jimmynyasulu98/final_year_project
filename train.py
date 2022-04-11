import os.path

import cv2 as cv
import numpy as np

# img = cv.imread('pics/jimmy/8.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('face', gray)
people = ['jimmy', 'king']
DIR = r'pics'
x_train = [] # X-train array
y_train = [] # Y-train array
haar_casecade = cv.CascadeClassifier('haarcascade.xml') # classfier for training model


def create_train(): # loping through direction and subdirectories containing pictures
    for person in people:  
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            image_path = os.path.join(path, img)
            image_array = cv.imread(image_path)
            gray = cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)
            faces = haar_casecade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
			# selecting region of intreset and assigning to array
			# x-train contains pictures
			# Y-train contains coresponding index of the person in people list
            for (x, y, w, h) in faces:
                faces_region_of_interest = gray[y:y + h, x:x + w]
                x_train.append(faces_region_of_interest)
                y_train.append(label)


print("Training the model!!-------------------------")
create_train()
x_train = np.array(x_train, dtype='object')
y_train = np.array(y_train)

face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.train(x_train, y_train)
print("Training done!!------------------------------")
face_recogniser.save('faces_trained.yml')
np.save("x_train.npy", x_train)
np.save("y_train.npy", y_train)
# print(len(x_train))
# print(len(y_train))
