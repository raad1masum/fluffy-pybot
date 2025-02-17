import magicbot
import wpilib
import wpilib.drive
import math
import navx

import robot_map
from oi import xboxController
from wpilib.command import Command
from wpilib.drive import DifferentialDrive
from commandbased import CommandBasedRobot
from subsystems import drivetrain
from commands import gyro_straight
from commands import tank_drive
from wpilib import XboxController

class Robot(magicbot.MagicRobot):

    def createObjects(self):
        """
        Objects are created here.
        """
        robot_map.robotMap(self)

    def robotPeriodic(self):
        """
        Executed periodically regardless of mode.
        """
        pass

    def autonomousInit(self):
        """
        Prepare for autonomous mode.
        """
        self.navx.reset()
        
    def autonomous(self):
        """
        Start autonomous mode.
        """
        gyro_straight.GyroStraight()

    def disabledInit(self):
        """
        Executed once right away when robot is disabled.
        """
        # Reset Gyro to 0
        drivetrain.Drivetrain.gyro(self)

    def disabledPeriodic(self):
        """
        Executed periodically while robot is disabled.
        Useful for testing.
        """
        drivetrain.Drivetrain.gyro(self)

    def teleopInit(self):
        """
        Executed when teleoperated mode begins.
        """
        pass

    def teleopPeriodic(self):
        """
        Executed periodically while robot is in teleoperated mode.
        """
        
        tank_drive.TankDrive.drive(xboxController.leftStickY * robot_map.nerf, xboxController.rightStickY * robot_map.nerf)

if __name__ == '__main__':
    wpilib.run(Robot)