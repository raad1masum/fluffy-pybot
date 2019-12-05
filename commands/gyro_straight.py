import wpilib
import navx

import robot_map
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems import drivetrain
from commands import tank_drive

class gyroStraight():
    if abs(navx.getAngle()) <= 3:
        