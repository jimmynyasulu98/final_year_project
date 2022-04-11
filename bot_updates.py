""" Bot updates contains all necessary message updates
    to be sent to a remote user after an event has
    occurred at home
"""
import datetime
import requests
import cv2

def send_message(link, message, chat_Id):
    try:
        params = {
            "chat_id": chat_Id,
            "text": str(message)
        }
        requests.get(link, data=params)
    except Exception as e:
        pass

def capture_video():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640, 480))
    # define a video capture object
    vid = cv2.VideoCapture(0)
    wait = 0
    while (True):

        # Capture the video frame
        # by frame

        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('video', frame)
        out.write(frame)
        #Exit loop when specifies seconds reached
        if cv2.waitKey(1) & wait > 100:
            break
        wait += 1

    # After the loop release the cap object
    vid.release()
    out.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
	
# Face recognition
def face_recognition():
    face_cascade = cv2.CascadeClassifier('haarcascade.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("faces_trained.yml")
    labels = []
    cap = cv2.VideoCapture(0)
    wait = 0  # wait keyword to be used to terminate frame

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:  # get image from region of interest
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            result = recognizer.predict(roi_gray)

            if result[1] < 500:
                confidence = int(100 * (1 - (result[1]) / 300))
                # display_string = str(confidence) + " % Confidence it is user"
                # print(display_string)
            if confidence > 85:
                labels.append(confidence)

            img_item = "7.png"
            cv2.imwrite(img_item, roi_color)

            color = (255, 0, 0)  # BGR 0-255
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        # Display the resulting frame and quit when reach specifies seconds
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & wait > 100:
            break
        wait += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return labels		

def send_video(file, chat_Id):
    try:
        files = {'document': open(file, 'rb')}
        requests.post('https://api.telegram.org/bot5024428855:AAGcCjR-P83R9w2D107mes-dntXzuQyNvd0/sendDocument?chat_id={}'
                      .format(chat_Id), files=files)
    except Exception as a:
        url = "https://api.telegram.org/bot5024428855:AAGcCjR-P83R9w2D107mes-dntXzuQyNvd0/sendMessage"
        chatID = "-625423112"
        message = 'Failed to capture a photo'
        send_message(url,message, chatID)

def get_motion_detected():
    return "\U000026A0 Alert! There is motion detected inside the house at {}". \
        format(datetime.datetime.now())


def get_abnormal_temperature_detected():
    return "\U000026A0 Alert! An abnormal temperature detected in the house at {}. Possible fire flames" \
           " occurred \U0001F525". \
        format(datetime.datetime.now())


def get_door_open_detected():
    return "\U000026A0 Alert! The Window has been opened at {}. Please find out if anyone is around at home". \
        format(datetime.datetime.now())


def get_door_closed_detected():
    return "Alert! The door closed at {}". \
        format(datetime.datetime.now())



