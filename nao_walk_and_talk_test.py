from naoqi import ALProxy
import Robot_IP_Address
import time
motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
motion.setStiffnesses("Body", 1.0)
motion.moveInit()
motion.post.moveTo(0, 0, 6.28318531 )
time.sleep(10)
motion.post.moveTo(0, 0, 6.28318531 )

tts.say("I'm walking")