from naoqi import ALProxy
import Robot_IP_Address
import time

def detect_landmark(motion):
    try:
        landMarkProxy = ALProxy("ALLandMarkDetection", Robot_IP_Address.IP, 9559)
    except Exception, e:
        print "Error when creating landmark detection proxy:"
        print str(e)
        exit(1)

    # Subscribe to the ALLandMarkDetection proxy
    # This means that the module will write in ALMemory with
    # the given period below
    period = 500
    landMarkProxy.subscribe("Test_LandMark", period, 0.0)

    # ALMemory variable where the ALLandMarkdetection modules
    # outputs its results
    memValue = "LandmarkDetected"

    # Create a proxy to ALMemory
    try:
        memoryProxy = ALProxy("ALMemory", Robot_IP_Address.IP, 9559)
    except Exception, e:
        print "Error when creating memory proxy:"
        print str(e)
        exit(1)

    # A simple loop that reads the memValue and checks whether landmarks are detected.
    #edited this value from 20 to something lower so it doesn't take as long to see if there's a landmark
    for i in range(0, 5):
        time.sleep(0.5)
        val = memoryProxy.getData(memValue)

        print ""
        print "*****"
        print ""

        # Check whether we got a valid output.
        if (val and isinstance(val, list) and len(val) >= 2):
            #returns bool value True if it sees a landmark
            return True
            # We detected naomarks !
            # For each mark, we can read its shape info and ID.

            # First Field = TimeStamp.
            timeStamp = val[0]

            # Second Field = array of Mark_Info's.
            markInfoArray = val[1]

            try:
                # Browse the markInfoArray to get info on each detected mark.
                for markInfo in markInfoArray:
                    # First Field = Shape info.
                    markShapeInfo = markInfo[0]

                    # Second Field = Extra info (ie, mark ID).
                    markExtraInfo = markInfo[1]
                    print "mark  ID: %d" % (markExtraInfo[0])
                    print "  alpha %.3f - beta %.3f" % (markShapeInfo[1], markShapeInfo[2])
                    print "  width %.3f - height %.3f" % (markShapeInfo[3], markShapeInfo[4])

            except Exception, e:
                print "Naomarks detected, but it seems getData is invalid. ALValue ="
                print val
                print "Error msg %s" % (str(e))
        else:
            print "No landmark detected"
    # bool returns false if no landmark
    return False

    # Unsubscribe the module.
    landMarkProxy.unsubscribe("Test_LandMark")

    print "Test terminated successfully."

def main():
    motion = ALProxy("ALMotion", Robot_IP_Address.IP, 9559)
    tts = ALProxy("ALTextToSpeech", Robot_IP_Address.IP, 9559)
    motion.setStiffnesses("Body", 1.0)
    id = motion.post.moveInit()
    motion.wait(id, 0)

    if detect_landmark(motion):
        print "We found a landmark!"

    else:
        print "We did not find a landmark"

if __name__ == "__main__":
    main()