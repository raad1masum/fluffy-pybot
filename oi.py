import wpilib
import robot_map
from wpilib import XboxController

def getController():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    xboxController = robot_map.xboxController
    xboxControllerRightStickY = robot_map.xboxControllerRightStickY
    xboxControllerLeftStickY = robot_map.xboxControllerLeftStickY