import wpilib

from ctre import ControlMode
from ctre import WPI_TalonSRX
from wpilib import SpeedControllerGroup

from wpilib.command import Subsystem
from wpilib.smartdashboard import SmartDashboard
from subsystems.drivetrain import robotMap
from commands.tank_drive import *

class Drivetrain(self):
    
    # initialize motors
    self.motorLeftFront = robotMap.motorLeftFront
    self.motorLeftMiddle = robotMap.motorLeftMiddle
    self.motorLeftBack = robotMap.motorLeftBack
    self.left = wpilib.SpeedControllerGroup(robotMap.motorLeftFront, robotMap.motorLeftMiddle, robotMap.motorLeftBack)
    self.motorRightFront = robotMap.motorRightFront
    self.motorRightMiddle = robotMap.motorRightMiddle
    self.motorRightBack = robotMap.motorRightBack
    self.right = wpilib.SpeedControllerGroup(robotMap.motorRightFront, robotMap.motorRightMiddle, robotMap.motorRightBack)