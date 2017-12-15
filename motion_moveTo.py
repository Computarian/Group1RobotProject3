# -*- encoding: UTF-8 -*-

import sys
import math
from naoqi import ALProxy
import Robot_IP_Address


def move_forward(motionProxy):
    PORT = 9559

   
    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Example showing the moveTo command
    # The units for this command are meters and radians
    x  = 0
    y  = .4
    theta  = math.pi/2
    #theta = 0
    motionProxy.moveTo(x, y, theta)

    #theta is rotation over z axis
    # Will block until move Task is finished
    motionProxy.stopMove()
    motionProxy.rest()
    ########
    # NOTE #
    ########
    # If moveTo() method does nothing on the robot,
    # read the section about walk protection in the
    # Locomotion control overview page.



  
