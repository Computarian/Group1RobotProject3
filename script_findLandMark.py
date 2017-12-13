from naoqi import ALProxy
import Robot_IP_Address
import vision_landMarkDetection

def find_the_landmark(motion):

def main():
    motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
    tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
    motion.setStiffnesses("Body", 1.0)
    id = motion.post.moveInit()
    motion.wait(id, 0)

    find_the_landmark(motion)

if __name__ == "__main__":
    main()