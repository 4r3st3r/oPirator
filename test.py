"""
This is a simple program to test if the theory works
"""

import time
import RPi.GPIO as GPIO

# GPIO pins
BUTTON = 3
LED = 5
SPEAKER_RELAY = 7
MIC_RELAY = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SPEAKER_RELAY, GPIO.OUT)
GPIO.setup(MIC_RELAY, GPIO.OUT)

GPIO.add_event_detect(BUTTON, GPIO.BOTH, bouncetime=500)


def handle_button():
    if GPIO.event_detected(BUTTON):
        print("GPIO.event_detected")

        print(GPIO.input(BUTTON))

        if GPIO.input(BUTTON) == 0:  # If button is being pressed
            print("---- PHONE ON HOOK ----")
            print("mycroft.stop")  # Stop all actions
            GPIO.output(MIC_RELAY, GPIO.LOW)  # Deactivate mic
            print('MIC OFF')
            time.sleep(2)

            if GPIO.input(BUTTON) == 0:
                GPIO.output(SPEAKER_RELAY, GPIO.HIGH)  # Activate loudspeaker
                print('SPEAKER ON')

        elif GPIO.input(BUTTON) == 1:  # If button is now not being pressed
            print("---- PHONE OFF HOOK ----")
            print("mycroft.mic.listen")  # Start listening
            GPIO.output(MIC_RELAY, GPIO.HIGH)  # Activate Microphone
            print("MIC ON")


while True:
    handle_button()
