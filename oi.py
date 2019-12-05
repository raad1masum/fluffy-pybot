import wpilib
import robot_map
from wpilib import XboxController

def xboxController(self):
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """
    self.xboxController = robot_map.xboxController
    self.leftStickY = XboxController.getY(robot_map.xboxControllerLeftStickY)
    self.rightStickY = XboxController.getY(robot_map.xboxControllerRightStickY)

