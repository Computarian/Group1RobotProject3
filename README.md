# Group1RobotProject3
NAO Robot Project

Chappie!

Group 1: Tim Joyce, Max Medina, Lara Nunes, Michael Sousa

TODO: Edge cases: Robot is close to landmark but is at an angle and landmark looks different. Robot doesn't have way to deal with landmark bin if it's not in it's line of sight at the start (Would have to program wandering walk, which would take into account robot not knowing where edge of the world is)

-Robot's neck motor for head pitching causes head to fall down or backward, which is bad for stability

## Mike's Code Cheat Sheet: [>O_O]>[]----->[*]  12/14/17 ##

**.gitIgnore**: files for git to ignore (we don't need your .pyc's!)

**almotion_moveCustomization**: File from Nao website for customized walk

**almotion_moveTo**: File from Nao website for more detailed moveTo function

**almotion_wbEffectorControlArm**: File from Nao website with details about arm controls

**joint_holdCan**: Tim's code for editing joint movements, slightly edited by Mike (sorry)

**motion_moveTo**: Not sure why this one still here *shrugs*

**nao_helloWorldTest**: Useful to tell when robot can start working, aside from saying "OGNAK GNOUK", also has list of IP's

**nao_walkAndTalkTest**: Short test for robot to walk and talk

**README.md**: Hello!

### Main Project Files begin ###

**Robot_IP_Address**: One file to change IP, will change it in all files as long as it's imported and use Robot_IP_Address.IP

**script_actionCan**: Want to do something with Nao and holding the can? Functions for it are here

**script_findLandmark**: uses vision_landMarkDetection code from nao website inside a function to detect a landmark, returns a bool value

**script_moveToLandMark**: control robot's movements when looking for landmark, also morphed into the main file at some point

**stop_Chappie**: runs motion.rest() if Chappie needs to stop before he hurts someone, or more likely himself

### Main Project Files end ###

**vision_landMarkDetection**: File from Nao website, used to detect if and what landmark the robot can see

**vision_localization**: File from Nao website, used to find x,y,z coords of landmark
