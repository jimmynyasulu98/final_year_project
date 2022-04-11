""" a python file containing all arduino related task ranging from sensor
 inputs to all corresponding outputs output """

# Import required libraries
from pyfirmata import Arduino, util
import bot_updates
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
    pattern = [0.8, 0.4] # alternate delay values for on and off
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


# Associate port and board with pyFirmata
port = 'COM3'
board = Arduino(port)

# Use iterator thread to avoid buffer overflow
it = util.Iterator(board)
it.start()

# Define pins for sensors
pir = Sensor('d', '5', 'i').get_input_value(board)
windowPin = Sensor('d', '4', 'i').get_input_value(board)
# framePin = Sensor('d', '9', 'i').get_input_value(board)

# Defining bot details
url = "https://api.telegram.org/bot5024428855:AAGcCjR-P83R9w2D107mes-dntXzuQyNvd0/sendMessage"
chatID = "-625423112"


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

        else:
            # Do nothing if the value is force
            pass
        # Ignore case when receiving None value from pin
        windowPinValue = windowPin.read()
        if windowPinValue is None:
            pass
        elif windowPinValue is True:
            # Send notification to bot
			# Check if the person opening windows is a member of house using the trained model
            labelsList = bot_updates.face_recognition()
			#
            if len(labelsList) < 3: #list should contain atleast three 85% confident for accuracy purpose 
                bot_updates.send_message(url, bot_updates.get_window_open_detected(), chatID)
                bot_updates.capture_video()
                bot_updates.send_video('output1.avi', chatID)
				buzzer(6, 10)


        else:
            # Do nothing if the value is force
            pass

    # Release the board
    board.exit()


if __name__ == "__main__":
    run_loop()
