"""
oPirator
Copyright (C) 2021 4r3st3r

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from mycroft import MycroftSkill
from mycroft.messagebus.message import Message

import time
import RPi.GPIO as GPIO

__author__ = '4r3st3r'

# GPIO pins
BUTTON = 11
LED = 16
SPEAKER_RELAY = 13
MIC_RELAY = 15

global isOffHook
isOffHook = True


class oPirator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)

            GPIO.setup(LED, GPIO.OUT)
            GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(SPEAKER_RELAY, GPIO.OUT)
            GPIO.setup(MIC_RELAY, GPIO.OUT)

            GPIO.output(MIC_RELAY, GPIO.LOW) # Set the mic to be off as default

            GPIO.add_event_detect(BUTTON, GPIO.BOTH, bouncetime=500)

        except GPIO.error:
            self.log.warning("Can't initialize GPIO - skill will not load")
            self.speak_dialog("error.initialise")

        finally:
            self.schedule_repeating_event(self.handle_button,
                                          None, 0.1, 'oPirator')
            self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
            self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)

    def handle_button(self, message):
        global isOffHook

        if GPIO.input(BUTTON) == 1 and isOffHook is False:  # If phone now is on hook
            isOffHook = True

            self.log.info("---- PHONE ON HOOK ----")
            self.bus.emit(Message("mycroft.stop"))  # Stop all actions

            if GPIO.input(BUTTON) == 0:      # Checks if the button has remained down or not
                time.sleep(1)                # If it does not pass these tests, then it is only
                if GPIO.input(BUTTON) == 0:  # Being reset, and so should not mute the mic
                    time.sleep(1)
                    if GPIO.input(BUTTON) == 0:
                        self.bus.emit(Message("mycroft.mic.mute"))  # Mute Mycroft
                        GPIO.output(MIC_RELAY, GPIO.LOW)  # Deactivate mic
                        GPIO.output(SPEAKER_RELAY, GPIO.HIGH)  # Activate loudspeaker

        elif GPIO.input(BUTTON) == 0 and isOffHook is True:  # If phone is now off hook
            isOffHook = False

            GPIO.output(MIC_RELAY, GPIO.HIGH)  # Activate Microphone

            self.log.info("---- PHONE OFF HOOK ----")
            self.bus.emit(Message("mycroft.mic.unmute"))  # Unmute Mycroft
            self.bus.emit(Message("mycroft.mic.listen"))  # Start listening


    def handle_listener_started(self, message):  # code to execute when active listening begins...
        GPIO.output(MIC_RELAY, GPIO.HIGH)  # Activate Microphone
        GPIO.output(LED, GPIO.HIGH)
        self.bus.emit(Message("mycroft.mic.unmute"))  # Unmute Mycroft

    def handle_listener_ended(self, message):  # code to execute when listening stops
        GPIO.output(MIC_RELAY, GPIO.LOW)  # Deactivate Microphone
        GPIO.output(LED, GPIO.LOW)
        self.bus.emit(Message("mycroft.mic.mute"))  # Mute Mycroft


def create_skill():
    return oPirator()


'''
    def handle_button(self, message):
        press_threshold = 2

        if GPIO.event_detected(BUTTON):
            self.log.info("GPIO.event_detected")
            pressed_time = time.time()

            if GPIO.input(BUTTON, GPIO.RISING):  # If button is being pressed
                pressed_time = time.time() - pressed_time  # Calculate the time it was pressed for

                if pressed_time < press_threshold:  # If short press:
                    self.bus.emit(Message("mycroft.stop"))  # Stop current action
                    time.sleep(0.2)  # Wait
                    self.bus.emit(Message("mycroft.mic.listen"))  # Start listening again for new command

                else:  # If long press
                    self.bus.emit(Message("mycroft.stop"))  # Stop all actions
                    GPIO.output(MIC_RELAY, GPIO.LOW)  # Deactivate mic
                    GPIO.output(SPEAKER_RELAY, GPIO.HIGH)  # Activate loudspeaker

            elif GPIO.input(BUTTON, GPIO.FALLING):  # If button is now not being pressed
                self.bus.emit(Message("mycroft.mic.listen"))  # Start listening
                GPIO.output(MIC_RELAY, GPIO.HIGH)  # Activate Microphone
'''
