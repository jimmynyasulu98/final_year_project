""" Bot updates contains all necessary message updates
    to be sent to a remote user after an event has
    occurred at home
"""
import datetime
import requests


def get_motion_detected():
    return "Alert! There is motion detected inside the house at {}". \
        format(datetime.datetime.now())


def get_abnormal_temperature_detected():
    return "Alert! An abnormal temperature detected in the house at {}". \
        format(datetime.datetime.now())


def get_door_open_detected():
    return "Alert! The door opened at {}". \
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
