# -*- encoding: UTF-8 -*-

import sys
from naoqi import ALProxy
import time
import almath
import Robot_IP_Address

def main(robotIP):
    PORT = 9559

    try:
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
    except Exception,e:
        print "Could not create proxy to ALMotion"
        print "Error was: ",e
        sys.exit(1)

    #motionProxy.setStiffnesses("Head", 1.0)
    motionProxy.setStiffnesses("LArm", 1.0)
    motionProxy.setStiffnesses("RArm", 1.0)

    # Simple command for the HeadYaw joint at 10% max speed
    #names            = "HeadYaw"
    names = "LShoulderPitch"
    names2 = "RShoulderPitch"
    
    angles           = 10*almath.TO_RAD
    
    fractionMaxSpeed = 0.1
    motionProxy.setAngles(names,angles,fractionMaxSpeed)
    motionProxy.setAngles(names2, angles, fractionMaxSpeed)

    #commented this out so the robot doesn't drop arm in this function
    #time.sleep(3)
    #motionProxy.setStiffnesses("RArm", 0.0)

if __name__ == "__main__":
    robotIp = Robot_IP_Address.IP

    if len(sys.argv) <= 1:
        print "Usage python almotion_controllingjoints.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    main(robotIp)
