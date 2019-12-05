import wpilib

from ctre import ControlMode
from ctre import WPI_TalonSRX
from wpilib import SpeedControllerGroup

from wpilib.command import Subsystem
from wpilib.smartdashboard import SmartDashboard
from subsystems.drivetrain import robotMap
from commands.tank_drive import *

class Drivetrain(self):
    self.left = wpilib.SpeedControllerGroup(robotMap.motorLeftFront, robotMap.motorLeftMiddle, robotMap.motorLeftBack)
    self.right = wpilib.SpeedControllerGroup(robotMap.motorRightFront, robotMap.motorRightMiddle, robotMap.motorRightBack)