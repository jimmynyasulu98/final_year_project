""" Bot updates contains all necessary message updates
    to be sent to a remote user after an event has
    occurred at home
"""
import datetime


def get_motion_detected():
    return "Alert! There is motion detected inside the house at {}".\
        format(datetime.datetime.now())


def get_abnormal_temperature_detected():
    return "Alert! An abnormal temperature detected in the house at {}".\
        format(datetime.datetime.now())


def get_door_open_detected():
    return "Alert! The door opened at {}".\
        format(datetime.datetime.now())


