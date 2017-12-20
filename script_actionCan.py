#Group 1: Tim Joyce, Max Medina, Lara Nunes, Michael Sousa

from naoqi import ALProxy
import Robot_IP_Address
import time
import almath
import script_findLandMark

#rotating joints to better hold can code
def lift_can(motion):
    #wrist yaw is rotating wrist
    #shoulder roll is angle of shoulder away from robot body
    r_wrist = "RWristYaw"
    l_wrist = "LWristYaw"
    r_shoulderRoll = "RShoulderRoll"
    l_shoulderRoll = "LShoulderRoll"
    r_shoulderPitch = "RShoulderPitch"
    l_shoulderPitch = "LShoulderPitch"
    headPitch = "HeadPitch"

    #editing these values will adjust angles
    angleLists_r_wrist = 100.0 * almath.TO_RAD
    angleLists_l_wrist = -100.0 * almath.TO_RAD
    angleLists_r_shoulderRoll = 10 * almath.TO_RAD
    angleLists_l_shoulderRoll = -10* almath.TO_RAD
    angleLists_r_shoulderPitch = 90 * almath.TO_RAD
    angleLists_l_shoulderPitch = -45 * almath.TO_RAD
    angleLists_headPitch = 0 * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True

    #moves head into position
    id = motion.post.angleInterpolation(headPitch, angleLists_headPitch, timeLists, isAbsolute)
    motion.wait(id, 0)


    #moves shoulders up
    #id = motion.post.angleInterpolation(r_shoulderPitch, angleLists_r_shoulderPitch, timeLists, isAbsolute)
    #motion.wait(id, 0)
    #id = motion.post.angleInterpolation(l_shoulderPitch, angleLists_l_shoulderPitch, timeLists, isAbsolute)
    #motion.wait(id, 0)

    #rotates wrists
    id = motion.post.angleInterpolation(r_wrist, angleLists_r_wrist, timeLists, isAbsolute)
    motion.wait(id, 0)
    #id = motion.post.angleInterpolation(l_wrist, angleLists_l_wrist, timeLists, isAbsolute)
    #motion.wait(id, 0)

    #moves arms towards each other
    #id = motion.post.angleInterpolation(r_shoulderRoll, angleLists_r_shoulderRoll, timeLists, isAbsolute)
    #motion.wait(id, 0)
    #id = motion.post.angleInterpolation(l_shoulderRoll, angleLists_l_shoulderRoll, timeLists, isAbsolute)
    #motion.wait(id, 0)

    #disables right arm motor so robot can walk without lowering arm
    id = motion.post.setWalkArmsEnabled(True, False)
    motion.wait(id, 0)

    id = motion.post.openHand('RHand')
    motion.wait(id, 0)

    id = motion.post.closeHand('RHand')
    motion.wait(id, 0)
    time.sleep(3)
    #id = motion.post.moveTo(1.0, 0, 0)
    #motion.wait(id, 0)
    #time.sleep(2)

#code to raise can before tossing can go here
def raise_arm(motion):
    #wrist yaw is rotating wrist
    #shoulder roll is angle of shoulder away from robot body
    r_wrist = "RWristYaw"
    l_wrist = "LWristYaw"
    r_shoulderRoll = "RShoulderRoll"
    l_shoulderRoll = "LShoulderRoll"
    r_shoulderPitch = "RShoulderPitch"
    l_shoulderPitch = "LShoulderPitch"

    #editing these values will adjust angles
    angleLists_r_wrist = 100.0 * almath.TO_RAD
    angleLists_l_wrist = -100.0 * almath.TO_RAD
    angleLists_r_shoulderRoll = 10 * almath.TO_RAD
    angleLists_l_shoulderRoll = -10* almath.TO_RAD
    angleLists_r_shoulderPitch = 10*almath.TO_RAD
    angleLists_l_shoulderPitch = -45 * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True

    id = motion.post.angleInterpolation(r_shoulderPitch, angleLists_r_shoulderPitch, timeLists, isAbsolute)
    motion.wait(id, 0)

#code to drop can in bin can go here
def drop_can(motion):
    #wrist yaw is rotating wrist
    #shoulder roll is angle of shoulder away from robot body
    r_wrist = "RWristYaw"
    l_wrist = "LWristYaw"
    r_elbow = "RElbowRoll"
    r_shoulderRoll = "RShoulderRoll"
    l_shoulderRoll = "LShoulderRoll"
    r_shoulderPitch = "RShoulderPitch"
    l_shoulderPitch = "LShoulderPitch"

    #editing these values will adjust angles
    angleLists_r_wrist = 0 * almath.TO_RAD
    angleLists_l_wrist = -100 * almath.TO_RAD
    angleLists_r_elbowRoll = 45 * almath.TO_RAD
    angleLists_r_shoulderRoll = -18 * almath.TO_RAD
    angleLists_l_shoulderRoll = -10* almath.TO_RAD
    angleLists_r_shoulderPitch = 90 * almath.TO_RAD
    angleLists_l_shoulderPitch = -45 * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True

    #moves arm to left
    id = motion.post.angleInterpolation(r_shoulderRoll, angleLists_r_shoulderRoll, timeLists, isAbsolute)
    motion.wait(id, 0)

    #rotates elbow
    #id = motion.post.angleInterpolation(r_elbow, angleLists_r_elbowRoll, timeLists, isAbsolute)
    #motion.wait(id, 0)

    #rotates wrist
    id = motion.post.angleInterpolation(r_wrist, angleLists_r_wrist, timeLists, isAbsolute)
    motion.wait(id, 0)

    id = motion.post.openHand("RHand")
    motion.wait(id, 0)

def victory_dance(motion):
    r_wrist = "RWristYaw"
    l_wrist = "LWristYaw"
    r_elbow = "RElbowRoll"
    l_elbow = "LElbowRoll"
    r_shoulderRoll = "RShoulderRoll"
    l_shoulderRoll = "LShoulderRoll"
    r_shoulderPitch = "RShoulderPitch"
    l_shoulderPitch = "LShoulderPitch"
    r_elbowYaw = "RElbowYaw"
    headPitch = "HeadPitch"
    headYaw = "HeadYaw"

    # editing these values will adjust angles
    angleLists_r_wrist = 90 * almath.TO_RAD
    angleLists_l_wrist = -90 * almath.TO_RAD
    angleLists_r_elbowRoll = 88.5 * almath.TO_RAD
    angleLists_l_elbowRoll = 0 * almath.TO_RAD
    angleLists_r_shoulderRoll = 18 * almath.TO_RAD
    angleLists_l_shoulderRoll = 76 * almath.TO_RAD
    angleLists_r_shoulderPitch = -15 * almath.TO_RAD
    angleLists_l_shoulderPitch = -90 * almath.TO_RAD
    angleLists_r_elbowYaw = 30 * almath.TO_RAD
    angleLists_headPitch = 29.5 * almath.TO_RAD
    angleLists_headYaw = -45 * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True

    #attempt to make Chappie dab
    #left arm movement
    id = motion.post.angleInterpolation(l_shoulderPitch, angleLists_l_shoulderPitch, timeLists, isAbsolute)
    motion.wait(id, 0)
    id = motion.post.angleInterpolation(l_shoulderRoll, angleLists_l_shoulderRoll, timeLists, isAbsolute)
    motion.wait(id, 0)
    id = motion.post.angleInterpolation(l_elbow, angleLists_l_elbowRoll, timeLists, isAbsolute)
    motion.wait(id, 0)

    #right arm movement
    id = motion.post.angleInterpolation(r_shoulderPitch, angleLists_r_shoulderPitch, timeLists, isAbsolute)
    motion.wait(id, 0)
    id = motion.post.angleInterpolation(r_shoulderRoll, angleLists_r_shoulderRoll, timeLists, isAbsolute)
    motion.wait(id, 0)
    id = motion.post.angleInterpolation(r_elbow, angleLists_r_elbowRoll, timeLists, isAbsolute)
    motion.wait(id, 0)
    id = motion.post.angleInterpolation(r_elbowYaw, angleLists_r_elbowYaw, timeLists, isAbsolute)
    motion.wait(id, 0)

    #head movement
    id = motion.post.angleInterpolation(headPitch,angleLists_headPitch, timeLists, isAbsolute)
    motion.wait(id, 0)
    id = motion.post.angleInterpolation(headYaw, angleLists_headYaw, timeLists, isAbsolute)
    motion.wait(id, 0)

def main():
    motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
    tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
    motion.setStiffnesses("Body", 1.0)
    id = motion.post.moveInit()
    motion.wait(id, 0)
    time.sleep(3)

    victory_dance(motion)

    """"
    id = motion.post.openHand('RHand')
    motion.wait(id, 0)
    #id = motion.post.openHand('LHand')
    #motion.wait(id, 0)

    id = motion.post.closeHand('RHand')
    motion.wait(id, 0)
    #id = motion.post.closeHand('LHand')
    #motion.wait(id, 0)
    """

    """
    i = 0
    while(i < 4):
        id = motion.post.moveTo(0.25, 0, 0)
        motion.wait(id, 0)
        time.sleep(1)
        i=i+1
    """

    #time.sleep(5)
    #motion.post.moveTo(0, 0, 3.1415)
    #time.sleep(10)
    #motion.post.moveTo(0, 0, 6.28318531 )
    #time.sleep(3)

    id = motion.post.setWalkArmsEnabled(True, True)
    motion.wait(id, 0)
    motion.rest()

if __name__ == "__main__":
    main()