""" Bot updates contains all necessary message updates
    to be sent to a remote user after an event has
    occurred at home
"""
import datetime
import requests


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


def send_message(link, message, chat_Id):
    params = {
        "chat_id": chat_Id,
        "text": str(message)
    }
    requests.get(link, data=params)
