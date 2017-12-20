#Group 1: Tim Joyce, Max Medina, Lara Nunes, Michael Sousa

from naoqi import ALProxy
import Robot_IP_Address

motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)

id = motion.post.setWalkArmsEnabled(True, True)

motion.rest()