from naoqi import ALProxy
import Robot_IP_Address
import time
import joint_holdCan
import almath

#robot walks with raised fist, used to test walking with raised arm(s)
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

#robot's head seems off, testing to see if it moves up and down
def head_test(motion):
    motion.setStiffnesses("Body", 1.0)
    motion.moveInit()

    headYaw = "HeadYaw"

    angleLists_headYaw = 115 * almath.TO_RAD

    headPitch = "HeadPitch"
    angleLists_headPitch = -38.5 * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True

    id = motion.post.angleInterpolation(headYaw, angleLists_headYaw, timeLists, isAbsolute)
    motion.wait(id, 0)


    id = motion.post.angleInterpolation(headPitch, angleLists_headPitch, timeLists, isAbsolute)
    motion.wait(id, 0)

    angleLists_headYaw = -115 * almath.TO_RAD
    id = motion.post.angleInterpolation(headYaw, angleLists_headYaw, timeLists, isAbsolute)
    motion.wait(id, 0)

    angleLists_headPitch = 28.5 * almath.TO_RAD
    id = motion.post.angleInterpolation(headPitch, angleLists_headPitch, timeLists, isAbsolute)
    motion.wait(id, 0)

    time.sleep(3)
    motion.rest()

def main():
    motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
    #walk_with_raised_fist(motion)
    head_test(motion)

if __name__ == "__main__":
    main()