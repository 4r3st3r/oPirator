# oPirator
 
The aim of this git is to help in buidling an 'operator' based on Picroft, that is, a home assistant that values privacy so much that it cannot listen when you dont want them to. This can be done as simply as wiring in a button which only allows the home assistant to listen when the button is pressed. However, for Aesthetic purposes, it is better to retrofit the Pi to an old telepone, intercom system or radio. This way you can use the inbuilt mic and speaker from the device, and your home assistant will look like a normal part of your home. 

This project uses [Mycroft.ai](https://mycroft.ai) - or more specifially their open-source Raspberry Pi version Picroft - to provide the home assistant part of this. Mycroft.ai is an open-source home assistant, and while they focus heavily on privacy and promise to *"ever sell your data or give you advertisements on our technology"* the aim of this git is to hack the Picroft system to enforce that policy and so create a home-assistant that only listens when you allow it to.  

There are two parts to the build, the software and the hardware. The hardware part will obviosuly be different depending on the device you are retrofitting your Picroft into, but the basic idea is the same. The use of relays to allow access to the speaker and mic is optional - the oPirator Skill does already include commands to mic Mycroft's mic, but it may provide more peace of mind for those more security concerned. 

# Software
1. Firstly, download, flash and install Picroft on your Raspberry Pi according to [the instructions](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft). 

  * Setting up the mic and audio is handled automatically by Picroft's setup wizard, so follow those instructions carefully. Make sure you select the correct options for however you have connected the speaker and microphone from the telephone. 
  * It might be necessary to follow [these instructions](https://github.com/MycroftAI/enclosure-picroft/pull/148/commits/1df02f3fea8d56327a5a109a120483c69ba44408) and delete these lines in `/etc/mycroft/mycroft.conf` if your audio / mic does not work. This happened with my first install, the only sound I was getting was some white noise which increased in volume as I turned up the volume in Mycroft. 

2. The next step is activating the skill which allows Mycroft to be activated by just picking up the handset:

  * You may need to allow Mycroft access to the GPIO pins via:
`sudo usermod -g gpio mycroft`

3. Then need to navigate into the Mycroft Core from the command line via:

`cd mycroft-core`

4. And simply use Mycroft's inbuilt skills manager to download this git and install it:

`mycroft-msm install https://github.com/4r3st3r/operatorPi`
(Hopefullt this skill will soon be inclucded within the Mycroft Skill Store, so it may be made as simple as asking Mycroft to *install the Operator Skill*

Then you are all done! When you pick up the reciever you should simple be able to ask Mycroft a question - without the need to say *"Hey Mycroft"*. When you put the reciver down, Mycroft will immediately stop whatever he is doing, and the mic will be muted. 

# Hardware
TODO
________________________
* TODO: Allow for a relay to be used to switch the speaker when the phone is on the hook. This will allow for a 'loudspeaker' to be used when the phone is down for alarms etc. BUT this will not allow the Mycroft to listen unless the phone is picked up.

* TODO: Make a relay which only connects the connection to the mic when the phone is off the hook. This way there is no possible way of Mycroft listening, as it creates a physical barrier to aid the digital barrier to the mic. 
