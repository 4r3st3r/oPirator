# OperatorPi
This skill should allow for Picroft to start up when the phone is removed from the hook, and turn off when it is placed back on the hook. 


May be neceesary to allow Mycroft access to the GPIO pins via:

`sudo usermod -g gpio mycroft`


It might also be neceesary to follow [these instructions](https://github.com/MycroftAI/enclosure-picroft/pull/148/commits/1df02f3fea8d56327a5a109a120483c69ba44408) and delete these lines in `/etc/mycroft/mycroft.conf`


TODO: Allow for a relay to be used to switch the speaker when the phone is on the hook. This will allow for a 'loudspeaker' to be used when the phone is down for alarms etc. BUT this will not allow the Mycroft to listen unless the phone is picked up.

Possible TODO: Make a relay which only connects the connection to the mic when the phone is off the hook. This way there is no possible way of Mycroft listening unintenionally. 
