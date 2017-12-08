from naoqi import ALProxy
import Robot_IP_Address

motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)

motion.rest()