import wpilib

import robot_map
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems import drivetrain
from commands import tank_drive
from wpilib.drive import DifferentialDrive

class TankDrive():
    def drive(self):
        self.tankDriveRobot = DifferentialDrive(drivetrain.leftSideMotors, drivetrain.rightSideMotors)