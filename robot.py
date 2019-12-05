import magicbot
import wpilib
import wpilib.drive
import math
import navx

import robot_map
from subsystems import drivetrain
from subsystems.drivetrain import robotMap
from wpilib.command import Commands

class Robot(magicbot.MagicRobot):
    def robotPeriodic(self):
        """
        Executed periodically regardless of mode.
        """
        pass

    def autonomousInit(self):
        """
        Prepare for autonomous mode.
        """
        pass
        
    def autonomous(self):
        """
        Start autonomous mode.
        """
        # Call autonomous
        # super().autonomous()
        pass

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
        Commands.tank_drive.TankDrive.tankDriveRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """
        Executed periodically while robot is in teleoperated mode.
        """
        Commands.tank_drive.TankDrive.tankDriveRobot.tankDrive(self.leftStick.getY() * -1, self.rightStick.getY() * -1)