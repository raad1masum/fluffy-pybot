import wpilib

from wpilib.drive import DifferentialDrive
from wpilib.command import Subsystem
from wpilib.command import Commands
from wpilib.smartdashboard import SmartDashboard
from subsystems.drivetrain import robotMap

class TankDrive(self):
    self.tankDriveRobot = DifferentialDrive(Subsystem.drivetrain.leftSideMotors, Subsystem.drivetrain.rightSideMotors)