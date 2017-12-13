from naoqi import ALProxy
import Robot_IP_Address
#Our robot has trouble deciding on an IP sometimes
IP_1 = "10.16.96.51"
IP_2 = "10.19.203.172"
IP_3 = "10.20.196.11"
IP_4 = "10.16.96.29"
IP_5 = "10.16.96.41"
IP_6 = "10.16.96.29"

tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
#tts.setLanguage("Brazilian")
tts.say("Hello!")

