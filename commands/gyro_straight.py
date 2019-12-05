import wpilib
import navx

import robot_map
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems import drivetrain
from commands import tank_drive

class gyroStraight():

    if abs(navx.getAngle()) <= 3:
        tank_drive.TankDrive.tankDriveRobot(robot_map.leftSlow - navx.getAngle(), robot_map.rightSlow - navx.getAngle())
    
    elif abs(navx.getAngle()) < 10:

        if navx.getAngle() > 0:
            tank_drive.TankDrive.tankDriveRobot(robot_map.leftSlow, 1.1 * robot_map.rightSlow)

        elif navx.getAngle() < 0:
            tank_drive.TankDrive.tankDriveRobot(1.1 * robot_map.leftSlow, robot_map.rightSlow)
        
    else:

        if navx.getAngle() > 0:

            while navx.getAngle > 10:
                tank_drive.TankDrive.tankDriveRobot(-robot_map.rotateSpeed, -robot_map.rotateSpeed)
                
            while navx.getAngle > 0:
                tank_drive.TankDrive.tankDriveRobot(-robot_map.rotateSpeedSlow, -robot_map.rotateSpeedSlow)
            
            while navx.getAngle < 0:
                tank_drive.TankDrive.tankDriveRobot(robot_map.rotateSpeedSlow, robot_map.rotateSpeedSlow)

        else:

            while navx.getAngle() > -10:
                tank_drive.TankDrive.tankDriveRobot(robot_map.rotateSpeed, robot_map.rotateSpeed)
            
            while navx.getAngle() < 0:
                tank_drive.TankDrive.tankDriveRobot(robot_map.rotateSpeedSlow, robot_map.rotateSpeedSlow)
            
            while navx.getAngle() > 0:
                tank_drive.TankDrive.tankDriveRobot(-robot_map.rotateSpeedSlow, -robot_map.rotateSpeedSlow)