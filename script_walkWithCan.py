from naoqi import ALProxy
import Robot_IP_Address
import time
import almath

#rotating joints to better hold can code
def pos_arms(motion):
    #wrist yaw is rotating wrist
    #shoulder roll is angle of shoulder away from robot body
    r_wrist = "RWristYaw"
    #l_wrist = "LWristYaw"
    r_shoulderRoll = "RShoulderRoll"
    #l_shoulderRoll = "LShoulderRoll"
    r_shoulderPitch = "RShoulderPitch"
    #l_shoulderPitch = "LShoulderPitch"
    headPitch = "HeadPitch"

    #editing these values will adjust angles
    angleLists_r_wrist = 100.0 * almath.TO_RAD
    #angleLists_l_wrist = -100.0 * almath.TO_RAD
    angleLists_r_shoulderRoll = 10 * almath.TO_RAD
    #angleLists_l_shoulderRoll = -10* almath.TO_RAD
    angleLists_r_shoulderPitch = -45 * almath.TO_RAD
    #angleLists_l_shoulderPitch = 5 * almath.TO_RAD
    angleLists_headPitch = 25 * almath.TO_RAD
    timeLists = 1.0
    isAbsolute = True

    #moves head up
    id = motion.post.angleInterpolation(headPitch, angleLists_headPitch, timeLists, isAbsolute)

    #moves shoulders up
    id = motion.post.angleInterpolation(r_shoulderPitch, angleLists_r_shoulderPitch, timeLists, isAbsolute)
    motion.wait(id, 0)
    #id = motion.post.angleInterpolation(l_shoulderPitch, angleLists_l_shoulderPitch, timeLists, isAbsolute)
    #motion.wait(id, 0)

    #rotates wrists
    id = motion.post.angleInterpolation(r_wrist, angleLists_r_wrist, timeLists, isAbsolute)
    motion.wait(id, 0)
    #id = motion.post.angleInterpolation(l_wrist, angleLists_l_wrist, timeLists, isAbsolute)
    #motion.wait(id, 0)

    #moves arms towards each other
    id = motion.post.angleInterpolation(r_shoulderRoll, angleLists_r_shoulderRoll, timeLists, isAbsolute)
    motion.wait(id, 0)
    #id = motion.post.angleInterpolation(l_shoulderRoll, angleLists_l_shoulderRoll, timeLists, isAbsolute)
    #motion.wait(id, 0)

    id = motion.post.setWalkArmsEnabled(True, False)
    motion.wait(id, 0)

def main():
    motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
    #tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
    motion.setStiffnesses("Body", 1.0)
    id = motion.post.moveInit()
    motion.wait(id, 0)

    pos_arms(motion)
    id = motion.post.openHand('RHand')
    motion.wait(id, 0)
    #id = motion.post.openHand('LHand')
    #motion.wait(id, 0)

    id = motion.post.closeHand('RHand')
    motion.wait(id, 0)
    #id = motion.post.closeHand('LHand')
    #motion.wait(id, 0)

    id = motion.post.moveTo(0.25, 0, 0)
    motion.wait(id, 0)

    #motion.post.moveTo(0.5, 0, 0)
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