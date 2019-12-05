import wpilib
import navx

import robot_map
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems import drivetrain
from commands import tank_drive

class gyroStraight(self):

    if abs(navx.getAngle()) <= 3:
        tank_drive.TankDrive.tankDriveRobot.tankDrive(robot_map.leftSlow - navx.getAngle(), robot_map.rightSlow - navx.getAngle())
    
    elif abs(navx.getAngle()) < 10:
        if abs(navx.getAngle()) <= 3:
            tank_drive.TankDrive.tankDriveRobot.tankDrive(robot_map.leftSlow - navx.getAngle(), robot_map.rightSlow - navx.getAngle())

        tank_drive.TankDrive.tankDriveRobot.tankDrive(robot_map.leftSlow - navx.getAngle(), robot_map.rightSlow - navx.getAngle())