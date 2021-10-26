# OperatorPi
 
The aim of this git is to help in buidling an 'operator' based on Picroft, that is, a home assistant where privacy is of such importance that they cannot listen when you dont want them to. This is done by retrofitting a home-telephone, so that the home assistant will only listen when the reciver is picked up. I am using Mycroft.ai - or more specifially their open-source Raspberry Pi version Picroft - to provide the home assistant part of this. This git creates a skill within Picroft that activates the home assistant when the reciever is picked up, and shuts it off when it is placed back down. 

Eventually I hope to wire the microphone into a relay that shuts off all access to it when the reciver is on the phone, as well as add a loud-speaker to the base which mycroft can access when the handset is down: thereby allowing Mycroft to still make annoucements, call the end of timers etc without him hearing what is going on in the room. Currently this is handled by muting the mic when the reciver is down, and unmuting it when it is picked up, but I think it would be good to have a physical disconnect to ensure that there is no way that Mycroft can listen in. 

There are two parts to the build, the software and the hardware.

# Software
Firstly, download, flash and install Picroft on your Raspberry Pi according to [the instructions](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft). 

Setting up the mic and audio is handled automatically by Picroft's setup wizard, so follow those instructions carefully. Make sure you select the correct options for however you have connected the speaker and microphone from the telephone. 
It might be necessary to follow [these instructions](https://github.com/MycroftAI/enclosure-picroft/pull/148/commits/1df02f3fea8d56327a5a109a120483c69ba44408) and delete these lines in `/etc/mycroft/mycroft.conf` if your audio / mic does not work. This happened with my first install, the only sound I was getting was some white noise which increased in volume as I turned up the volume in Mycroft. 

The next step is activating the skill which allows Mycroft to be activated by just picking up the handset:

Firstly it may be necessary to allow Mycroft access to the GPIO pins via:
`sudo usermod -g gpio mycroft`

You then need to navigate into the Mycroft Core from the command line via:

`cd mycroft-core`

Then simply use Mycroft's inbuilt skills manager to download this git and install it:

`mycroft-msm install https://github.com/4r3st3r/operatorPi`
(Hopefullt this skill will soon be inclucded within the Mycroft Skill Store, so it may be made as simple as asking Mycroft to *install the Operator Skill*

Then you are all done! When you pick up the reciever you should simple be able to ask Mycroft a question - without the need to say *"Hey Mycroft"*. When you put the reciver down, Mycroft will immediately stop whatever he is doing and will not be able to hear you. 


________________________
# TODO: Allow for a relay to be used to switch the speaker when the phone is on the hook. This will allow for a 'loudspeaker' to be used when the phone is down for alarms etc. BUT this will not allow the Mycroft to listen unless the phone is picked up.

# TODO: Make a relay which only connects the connection to the mic when the phone is off the hook. This way there is no possible way of Mycroft listening. 
