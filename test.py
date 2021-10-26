"""
This is a simple program to test if the theory works
"""

import time
import RPi.GPIO as GPIO

# GPIO pins
BUTTON = 23
LED = 25
SPEAKER_RELAY = 22
MIC_RELAY = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(SPEAKER_RELAY, GPIO.OUT)
GPIO.setup(MIC_RELAY, GPIO.OUT)

GPIO.add_event_detect(BUTTON, GPIO.FALLING, bouncetime=500)
GPIO.add_event_detect(BUTTON, GPIO.RISING, bouncetime=500)


def handle_button():
    press_threshold = 2

    if GPIO.event_detected(BUTTON):
        print("GPIO.event_detected")
        pressed_time = time.time()

        if GPIO.input(BUTTON, GPIO.RISING):  # If button is being pressed
            pressed_time = time.time() - pressed_time  # Calculate the time it was pressed for

            if pressed_time < press_threshold:  # If short press:
                print("---- RESET BUTTON PRESSED ----")
                print("mycroft.stop")  # Stop current action
                time.sleep(0.2)  # Wait
                print("mycroft.mic.listen")  # Start listening again for new command

            else:  # If long press
                print("---- PHONE ON HOOK ----")
                print("mycroft.stop")  # Stop all actions
                GPIO.output(MIC_RELAY, GPIO.LOW)  # Deactivate mic
                print('MIC OFF')
                GPIO.output(SPEAKER_RELAY, GPIO.HIGH)  # Activate loudspeaker
                print('SPEAKER ON')

        elif GPIO.input(BUTTON, GPIO.FALLING):  # If button is now not being pressed
            print("---- PHONE OFF HOOK ----")
            print("mycroft.mic.listen")  # Start listening
            GPIO.output(MIC_RELAY, GPIO.HIGH)  # Activate Microphone
            print("MIC ON")


while True:
    handle_button()
