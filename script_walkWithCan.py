from naoqi import ALProxy
import Robot_IP_Address
import time
import joint_holdCan

motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
#motion.setStiffnesses("Body", 1.0)
motion.moveInit()
time.sleep(3)
joint_holdCan.main(Robot_IP_Address.IP)
time.sleep(3)
motion.openHand('RHand')
time.sleep(3.0)
motion.closeHand('RHand')
time.sleep(3)
motion.post.moveTo(0.5, 0, 0)
time.sleep(5)
#motion.post.moveTo(0, 0, 3.1415)
#time.sleep(10)
#motion.post.moveTo(0, 0, 6.28318531 )
#time.sleep(10)
#motion.rest()