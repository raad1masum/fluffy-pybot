import wpilib
import navx

import robot_map
from wpilib.command import Command
from commandbased import CommandBasedRobot
from subsystems import drivetrain
from commands import tank_drive

class GyroStraight():

    def gyroStraight(self):

        if abs(self.navx.getAngle()) <= 3:
            tank_drive.TankDrive.tankDriveRobot(robot_map.leftSlow - self.navx.getAngle(), robot_map.rightSlow - self.navx.getAngle())
        
        elif abs(self.navx.getAngle()) < 10:

            if self.navx.getAngle() > 0:
                tank_drive.TankDrive.tankDriveRobot(robot_map.leftSlow, 1.1 * robot_map.rightSlow)

            elif self.navx.getAngle() < 0:
                tank_drive.TankDrive.tankDriveRobot(1.1 * robot_map.leftSlow, robot_map.rightSlow)
            
        else:

            if self.navx.getAngle() > 0:

                while self.navx.getAngle > 10:
                    tank_drive.TankDrive.tankDriveRobot(-robot_map.rotateSpeed, -robot_map.rotateSpeed)
                    
                while self.navx.getAngle > 0:
                    tank_drive.TankDrive.tankDriveRobot(-robot_map.rotateSpeedSlow, -robot_map.rotateSpeedSlow)
                
                while self.navx.getAngle < 0:
                    tank_drive.TankDrive.tankDriveRobot(robot_map.rotateSpeedSlow, robot_map.rotateSpeedSlow)

            else:

                while self.navx.getAngle() > -10:
                    tank_drive.TankDrive.tankDriveRobot(robot_map.rotateSpeed, robot_map.rotateSpeed)
                
                while self.navx.getAngle() < 0:
                    tank_drive.TankDrive.tankDriveRobot(robot_map.rotateSpeedSlow, robot_map.rotateSpeedSlow)
                
                while self.navx.getAngle() > 0:
                    tank_drive.TankDrive.tankDriveRobot(-robot_map.rotateSpeedSlow, -robot_map.rotateSpeedSlow)