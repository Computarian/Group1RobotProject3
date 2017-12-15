# -*- encoding: UTF-8 -*-

import sys
from naoqi import ALProxy
import time
import almath
import Robot_IP_Address

def joint_raise_arm(motionProxy):
    
    
   

    #motionProxy.setStiffnesses("Head", 1.0)
    motionProxy.setStiffnesses("LArm", 1.0)
   
    motionProxy.setStiffnesses("RArm", 1.0)

    # Simple command for the HeadYaw joint at 10% max speed
    #names            = "HeadYaw"
    names = "LShoulderPitch"
    names2 = "RShoulderPitch"
    
    angles           = 10*almath.TO_RAD
    
    fractionMaxSpeed = 0.1
    #motionProxy.setAngles(names,angles,fractionMaxSpeed)
    motionProxy.setAngles(names2, angles, fractionMaxSpeed)

    #commented this out so the robot doesn't drop arm in this function
    #time.sleep(3)
    #motionProxy.setStiffnesses("RArm", 0.0)

