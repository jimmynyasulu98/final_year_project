# Import required libraries
from pyfirmata import Arduino, util
import time


# Class for all sensors to be used
class Sensor:
    def __init__(self, pin_category, pin_cumber, pin_type, ):
        self.pin_category = pin_category
        self.pin_number = pin_cumber
        self.pin_type = pin_type

    def get_input_value(self, arduino_board):
        return arduino_board.get_pin('{}:{}:{}'.format
                                     (self.pin_category, self.pin_number, self.pin_type))


# Associate port and board with pyFirmata
port = 'COM1'
board = Arduino(port)

# Use iterator thread to avoid buffer overflow
it = util.Iterator(board)
it.start()

# Define pins for sensors
pirPin = Sensor('d', '7', 'i').get_input_value(board)
doorPin = Sensor('d', '8', 'i').get_input_value(board)
tempPin = Sensor('d', '9', 'i').get_input_value(board)

# Output pins
redPin = 12
greenPin = 13


# While loop to repeatedly execute
def run_loop():
    while True:
        # Ignore case when receiving None value from pin
        pirValue = pirPin.read()

        if pirValue is None:
            time.sleep(1)
            pass

        elif pirValue is True:
            # Send notification to bot and update database
            pass
        else:
            # Do nothing if the value is force
            pass

        doorPinValue = pirPin.read()
        if doorPinValue is None:
            time.sleep(1)
            pass

        elif doorPinValue is True:
            # Send notification to bot and update database
            pass
        else:
            # Do nothing if the value is force
            pass

        # Check the value for temperature sensor
        tempPinValue = pirPin.read()
        if tempPinValue is None:
            time.sleep(1)
            pass

        elif tempPinValue is True:
            # Send notification to bot and update database
            pass
        else:
            # Do nothing if the value is force
            pass

        # Release the board
    board.exit()
