from naoqi import ALProxy
import Robot_IP_Address
import time
import joint_holdCan
import almath

def walk_with_raised_fist(motion):

    id = motion.post.setStiffnesses("Body", 1.0)
    motion.wait(id,0)
    id = motion.post.moveInit()
    motion.wait(id,0)

    #wrist yaw is rotating wrist
    #shoulder roll is angle of shoulder away from robot body
    r_shoulder = "RShoulderRoll"
    r_shoulderPitch = "RShoulderPitch"
    head = "HeadPitch"

    #editing these values will adjust angles
    angleLists_r_shoulder = 15 * almath.TO_RAD
    angleLists_r_shoulderPitch = -10 * almath.TO_RAD
    angleLists_head = 10 * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True

    #motion.angleInterpolation(r_wrist, angleLists_r_wrist, timeLists, isAbsolute)
    #motion.angleInterpolation(l_wrist, angleLists_l_wrist, timeLists, isAbsolute)
    id = motion.post.angleInterpolation(r_shoulder, angleLists_r_shoulder, timeLists, isAbsolute)
    motion.wait(id,0)
    #motion.angleInterpolation(l_shoulder, angleLists_l_shoulder, timeLists, isAbsolute)

    id = motion.post.angleInterpolation(r_shoulderPitch, angleLists_r_shoulderPitch, timeLists, isAbsolute)
    motion.wait(id,0)
    id = motion.post.angleInterpolation(head, angleLists_head, timeLists, isAbsolute)
    motion.wait(id,0)

    #disable arm
    motion.setWalkArmsEnabled(False, False)
    id = motion.post.moveTo(0.5, 0, 0)
    motion.wait(id, 0)

    motion.rest()

def main():
    motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
    walk_with_raised_fist(motion)

if __name__ == "__main__":
    main()