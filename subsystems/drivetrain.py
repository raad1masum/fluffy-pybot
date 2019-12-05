import wpilib

from ctre import ControlMode
from ctre import WPI_TalonSRX
from wpilib import SpeedControllerGroup

import navx

from wpilib.command import Subsystem
from wpilib.smartdashboard import SmartDashboard
from subsystems.drivetrain import robotMap
from commands.tank_drive import *

def run():
    raise ValueError()

class Drivetrain(self):

    # initialize motors
    self.motorLeftFront = robotMap.motorLeftFront
    self.motorLeftMiddle = robotMap.motorLeftMiddle
    self.motorLeftBack = robotMap.motorLeftBack
    self.left = wpilib.SpeedControllerGroup(robotMap.motorLeftFront, robotMap.motorLeftMiddle, robotMap.motorLeftBack)
    self.motorRightFront = robotMap.motorRightFront
    self.motorRightMiddle = robotMap.motorRightMiddle
    self.motorRightBack = robotMap.motorRightBack
    self.right = wpilib.SpeedControllerGroup(robotMap.motorRightFront, robotMap.motorRightMiddle, robotMap.motorRightBack)

    # initialize drive sticks
    self.leftStick = robotMap.xboxControllerLeftStickY
    self.rightStick = robotMap.xboxControllerRightStickY

    # initialize gyro
    self.navx = navx.AHRS.create_spi()
    self.analog = wpilib.AnalogInput(navx.getNavxAnalogInChannel(robotMap.gyro))

    def gyroDisabled(self):

        self.logger.info("Entered disabled mode")

        self.timer.reset()
        self.timer.start()

        while self.isDisabled():

            if self.timer.hasPeriodPassed(0.5):
                self.sd.putBoolean(
                    "SupportsDisplacement", self.navx._isDisplacementSupported()
                )
                self.sd.putBoolean("IsCalibrating: ", self.navx.isCalibrating())
                self.sd.putBoolean("IsConnected: ", self.navx.isConnected())
                self.sd.putNumber("Angle: ", self.navx.getAngle())
                self.sd.putNumber("Pitch: ", self.navx.getPitch())
                self.sd.putNumber("Yaw: ", self.navx.getYaw())
                self.sd.putNumber("Roll: ", self.navx.getRoll())
                self.sd.putNumber("Analog: ", self.analog.getVoltage())
                self.sd.putNumber("Timestamp: " , self.navx.getLastSensorTimestamp())

            wpilib.Timer.delay(0.010)

if __name__ == "__main__":
    wpilib.run(Drivetrain())
