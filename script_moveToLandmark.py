from naoqi import ALProxy
import Robot_IP_Address
import time
import almath
import script_findLandMark
import script_holdCan

def landmark_localization():
    # -*- encoding: UTF-8 -*-
    from naoqi import ALProxy

    import math
    import almath
    import Robot_IP_Address

    # Set here your robto's ip.
    ip = Robot_IP_Address.IP
    # Set here the size of the landmark in meters.
    landmarkTheoreticalSize = 0.17  # in meters
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


def move_to_landmark(motion):
    #x,y,z = landmark_localization()

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
    print "Hi"

def main():
    motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
    tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
    motion.setStiffnesses("Body", 1.0)
    id = motion.post.moveInit()
    motion.wait(id, 0)
    script_holdCan.pos_arms(motion)

    #rotates "in place" until it sees the landmark
    while(script_findLandMark.detect_landmark(motion) is False):
        id = motion.post.moveTo(0,0, 10 * almath.TO_RAD)
        motion.wait(id,0)
    tts.say("I found the landmark")
    motion.rest()
    #while not at destination
        #script_findLandMark.detect_landmark(motion)
        #move_to_landmark(motion)

if __name__ == "__main__":
    main()