#Group 1: Tim Joyce, Max Medina, Lara Nunes, Michael Sousa

from naoqi import ALProxy
import Robot_IP_Address
import time
import almath
import script_findLandMark
import script_actionCan
import joint_holdCan
import motion_moveTo
import math

#minimum distance for when robot is close enough to box
minDist = 0.70
#landMarkBig = 0.17
#using smaller landmark
landMarkSize = 0.115

#vision_localization.py from nao website put into function
#robot should be localizing landmark since this only runs after findLandMark which detects if landmark
#is in front of robot or not
def landmark_localization(landMarkSize):
    # -*- encoding: UTF-8 -*-

    # Set here your robot's ip.
    ip = Robot_IP_Address.IP
    # Set here the size of the landmark in meters.
    landmarkTheoreticalSize = landMarkSize  # in meters
    # Set here the current camera ("CameraTop" or "CameraBottom").
    currentCamera = "CameraTop"

    memoryProxy = ALProxy("ALMemory", ip, 9559)
    landmarkProxy = ALProxy("ALLandMarkDetection", ip, 9559)

    # Subscribe to LandmarkDetected event from ALLandMarkDetection proxy.
    landmarkProxy.subscribe("landmarkTest")

    # Wait for a mark to be detected.
    markData = memoryProxy.getData("LandmarkDetected")
    while (markData is None or len(markData) == 0):
        markData = memoryProxy.getData("LandmarkDetected")

    # Retrieve landmark center position in radians.
    wzCamera = markData[1][0][0][1]
    wyCamera = markData[1][0][0][2]

    # Retrieve landmark angular size in radians.
    angularSize = markData[1][0][0][3]

    # Compute distance to landmark.
    distanceFromCameraToLandmark = landmarkTheoreticalSize / (2 * math.tan(angularSize / 2))

    motionProxy = ALProxy("ALMotion", ip, 9559)

    # Get current camera position in NAO space.
    transform = motionProxy.getTransform(currentCamera, 2, True)
    transformList = almath.vectorFloat(transform)
    robotToCamera = almath.Transform(transformList)

    # Compute the rotation to point towards the landmark.
    cameraToLandmarkRotationTransform = almath.Transform_from3DRotation(0, wyCamera, wzCamera)

    # Compute the translation to reach the landmark.
    cameraToLandmarkTranslationTransform = almath.Transform(distanceFromCameraToLandmark, 0, 0)

    # Combine all transformations to get the landmark position in NAO space.
    robotToLandmark = robotToCamera * cameraToLandmarkRotationTransform * cameraToLandmarkTranslationTransform

    print "x " + str(robotToLandmark.r1_c4) + " (in meters)"
    print "y " + str(robotToLandmark.r2_c4) + " (in meters)"
    print "z " + str(robotToLandmark.r3_c4) + " (in meters)"

    landmarkProxy.unsubscribe("landmarkTest")

    #returns x, y, and z coords from landmark localization
    #x: forward(+) and back(-), y: left(+) and right(-)
    return (robotToLandmark.r1_c4, robotToLandmark.r2_c4, robotToLandmark.r1_c4)

def move_to_landmark(motion,landMarkSize):
    #added this while loop so robot can find landmark when it loses it between detect and localize
    while (script_findLandMark.detect_landmark(motion, landMarkSize) is False):
        id = motion.post.moveTo(0, 0, 30 * almath.TO_RAD)
        motion.wait(id, 0)
    # x,y,z = landmark_localization()
    x, y, z = landmark_localization(landMarkSize)
    print x, y, z

    print "Hello I run"
    #if landmark is more than minDist away
    if (x > minDist):
        id = motion.post.moveTo(x/4.0,y/4.0, 0)
        motion.wait(id, 0)
        print ("Robot is ", x, " m away from the landmark")
        return x, y
    else:
        print ("Robot has reached it's destination, x:", x, " y:", y, " z: ", z," coords")
        return x, y
    #hypotenuse from x and y get theta for move
    #robot doesn't like to go straight so cutting length down when far will keep it more on track
    #if dist > something big
        #motion.post.moveTo(x/4,y/4,0)
    #else if dist > middle
        #motion.post.moveTo(x/2,y/2,0)
    #else if dist is <= close
        #move head down using z coord
        #motion.post.moveTo(x,y,0)
    #else robot at destination
        #return

def main():
    #initializing the robot
    motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
    tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
    motion.setStiffnesses("Body", 1.0)
    id = motion.post.moveInit()
    motion.wait(id, 0)

    #calls script for robot to hold can
    script_actionCan.lift_can(motion)

    #variable to hold x, y coordinates from localization data to determine which direction
    #robot rotates in
    xDist = 0.0
    yDist = 0.0

    #detect landmark loop and move to landmark will be in one big while loop that
    #stops when robot is at "destination" ie close to landmark where it will begin to think about throwing can away
    #while (destination is false):
    while (True):
        #rotates "in place" until it sees the landmark
        while(script_findLandMark.detect_landmark(motion,landMarkSize) is False):
            #robot moves something degrees times almath's conversion to rads
            #robot rotates left if it loses landmark location and it was to it's left
            if (yDist >= 0.0):
                id = motion.post.moveTo(0,0, 30 * almath.TO_RAD)
                motion.wait(id,0)
            #robot rotates right  if it loses landmark location and it was to it's right
            else:
                id = motion.post.moveTo(0,0, -30 * almath.TO_RAD)
                motion.wait(id,0)
        #tts.say("I found the landmark")

        #calls move to landmark function after detecting landmark
        """
        code bug: called move_to_landmark twice and robot would lose landmark since second time it runs,
        landmark localization may not be able to find landmark since robot moved after running running
        detect_landmark function
        """
        #move_to_landmark(motion,landMarkSize)
        print move_to_landmark(motion,landMarkSize)
        #returns x and y values from move to landmark
        xDist, yDist = move_to_landmark(motion,landMarkSize)
        print xDist
        #if robot is close enough to it's location, break out of this loop
        if (xDist <= minDist):
            break

    script_actionCan.raise_arm(motion)
    #probably going to have a scripts for raising and then throwing can in there
    # code for getting closer to bin  based off desired method can go here
    id = motion.post.moveTo(0.22, 0, 0)
    motion.wait(id, 0)

    #drops can into bin
    id = motion.post.moveTo(0, 0, 45 * almath.TO_RAD)
    motion.wait(id, 0)
    script_actionCan.drop_can(motion)

    #Chappie did it! Replace with better quote if desired
    tts.say("Chappie if you want to be in the gang you have to be cool, like daddy!")

    #backs away from bin
    id = motion.post.moveTo(-0.30, 0, 0)
    tts.say("Look how daddy walks! Look how cool it's! Need to keep it gangsta' Chappie!")
    motion.wait(id, 0)

    #insert victory dance/pose here
    id = motion.post.setWalkArmsEnabled(True, True)
    motion.wait(id, 0)
    script_actionCan.victory_dance(motion)
    tts.say("Don't laugh, I'm being cool!")

    #Chappie rests
    motion.rest()

if __name__ == "__main__":
    main()
