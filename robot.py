import magicbot
import wpilib
import wpilib.drive
import math
import navx

import robot_map
from subsystems.drivetrain import robotMap

class Robot(magicbot.MagicRobot):
    def robotPeriodic(self):
        """
        Executed periodically regardless of mode.
        """
        pass

    def autonomous(self):
        """
        Prepare for and start autonomous mode.
        """
        # Call autonomous
        super().autonomous()

    def disabledInit(self):
        """
        Executed once right away when robot is disabled.
        """
        # Reset Gyro to 0
        self.navx.reset()

    def disabledPeriodic(self):
        """
        Executed periodically while robot is disabled.
        Useful for testing.
        """
        pass

    def teleopInit(self):
        """
        Executed when teleoperated mode begins.
        """

    def teleopPeriodic(self):
        """
        Executed periodically while robot is in teleoperated mode.
        """