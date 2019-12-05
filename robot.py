import magicbot
import wpilib
import wpilib.drive
import math
import navx

import robot_map
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems import drivetrain
from commands import gyro_straight
from commands import tank_drive

class Robot(magicbot.MagicRobot):

    def createObjects(self):
        """
        Objects are created here.
        """
        robot_map.robotMap()

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
        self.navx.reset()
        drivetrain.gyro.gyroDisabled()

    def disabledPeriodic(self):
        """
        Executed periodically while robot is disabled.
        Useful for testing.
        """
        drivetrain.gyro.gyroDisabled()

    def teleopInit(self):
        """
        Executed when teleoperated mode begins.
        """
        tank_drive.TankDrive.tankDriveRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """
        Executed periodically while robot is in teleoperated mode.
        """
        tank_drive.TankDrive.tankDriveRobot(self.leftStick.getY() * robot_map.nerf, self.rightStick.getY() * robot_map.nerf)