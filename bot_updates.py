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
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & wait > 100:
            break
        wait += 1

    # After the loop release the cap object
    vid.release()
    out.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

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



