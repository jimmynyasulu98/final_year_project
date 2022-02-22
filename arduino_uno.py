""" a python file containing all arduino related task ranging from sensor
 inputs to all corresponding outputs output """

# Import required libraries
from pyfirmata import Arduino, util
import bot_updates
import database
import time
from datetime import datetime


# Class for all sensors to be used
class Sensor:
    def __init__(self, pin_category, pin_cumber, pin_type, ):
        self.pin_category = pin_category
        self.pin_number = pin_cumber
        self.pin_type = pin_type

    def get_input_value(self, arduino_board):
        return arduino_board.get_pin('{}:{}:{}'.format
                                     (self.pin_category, self.pin_number, self.pin_type))


# Buzzer function to be called if an incidence has happened
def buzzer(pin, recurrence):
    pattern = [0.8, 0.4]
    flag = True
    for i in range(recurrence):
        for delay in pattern:
            if flag is True:
                board.digital[pin].write(1)
                flag = False
                time.sleep(1)
            else:
                board.digital[pin].write(0)
                flag = True
                time.sleep(1)
    board.digital[pin].write(0)


# return the temperature readings
def get_temperature(analog_input):
    if analog_input is None:
        pass
    else:
        voltage_at_pin_in_millivolts = analog_input * (5000 / 1024)
        return voltage_at_pin_in_millivolts


# Associate port and board with pyFirmata
port = 'COM1'
board = Arduino(port)

# Use iterator thread to avoid buffer overflow
it = util.Iterator(board)
it.start()

# Define pins for sensors
pir = Sensor('d', '7', 'i').get_input_value(board)
doorPin = Sensor('d', '8', 'i').get_input_value(board)
framePin = Sensor('d', '9', 'i').get_input_value(board)

# Output pins
# redPin = 12
# greenPin = 13

# Defining bot details
url = "https://api.telegram.org/bot5024428855:AAGcCjR-P83R9w2D107mes-dntXzuQyNvd0/sendMessage"
chatID = "-625423112"

# create a database connection
connection = database.connect()
database.create_tables(connection)


# While loop to repeatedly execute
def run_loop():
    while True:

        pirValue = pir.read()
        # Ignore case when receiving None value from pin
        if pirValue is None:
            pass
        elif pirValue is True:
            # Send notification to bot and update database
            bot_updates.send_message(url, bot_updates.get_motion_detected(), chatID)
            bot_updates.capture_video()
            buzzer(6, 10)
            bot_updates.send_video('output1.avi', chatID)
            database.insert_update(connection, 'motion_sensor', 'motion', datetime.now())

        else:
            # Do nothing if the value is force
            pass
        # Ignore case when receiving None value from pin
        doorPinValue = doorPin.read()
        if doorPinValue is None:
            pass
        elif doorPinValue is True:
            # Send notification to bot and update database
            bot_updates.send_message(url, bot_updates.get_door_open_detected(), chatID)
            bot_updates.capture_video()
            buzzer(6, 10)
            bot_updates.send_video('output1.avi', chatID)
            database.insert_update(connection, 'door_sensor', 'opened', datetime.now())

        else:
            # Do nothing if the value is force
            pass

    # Release the board
    board.exit()


if __name__ == "__main__":
    run_loop()
