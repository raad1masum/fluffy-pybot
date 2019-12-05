import wpilib

from ctre import ControlMode
from ctre import WPI_TalonSRX
from wpilib import SpeedControllerGroup
from wpilib.drive import DifferentialDrive

import navx

import robot_map
from wpilib.smartdashboard import SmartDashboard
from wpilib.command import Command
from commandbased import CommandBasedRobot

def run():
    raise ValueError()

class Drivetrain():
    def init(self):

        # initialize wpilib stuff
        self.sd = wpilib.SmartDashboard
        self.timer = wpilib.Timer()

        # initialize motors
        self.motorLeftFront = robot_map.motorLeftFront
        self.motorLeftMiddle = robot_map.motorLeftMiddle
        self.motorLeftBack = robot_map.motorLeftBack
        self.leftSideMotors = wpilib.SpeedControllerGroup(robot_map.motorLeftFront, robot_map.motorLeftMiddle, robot_map.motorLeftBack)
        self.motorRightFront = robot_map.motorRightFront
        self.motorRightMiddle = robot_map.motorRightMiddle
        self.motorRightBack = robot_map.motorRightBack
        self.rightSideMotors = wpilib.SpeedControllerGroup(robot_map.motorRightFront, robot_map.motorRightMiddle, robot_map.motorRightBack)

        # initialize drive sticks
        self.leftStick = robot_map.xboxControllerLeftStickY
        self.rightStick = robot_map.xboxControllerRightStickY

        # initialize gyro
        self.navx = navx.AHRS.create_spi()
        self.analog = wpilib.AnalogInput(navx.getNavxAnalogInChannel(robot_map.gyro))

    def motors(self):

        def speedLeftMotors(self, speed):
            Drivetrain.leftSideMotors.set(ControlMode.PercentOutput, -speed)

        def speedRightMotors(self, speed):
            Drivetrain.rightSideMotors.set(ControlMode.PercentOutput, speed)

    def gyro(self):

        def gyroDisabled(self):

            self.logger.info("Entered disabled mode")

            self.timer.reset()
            self.timer.start()

            while self.isDisabled():

                if self.timer.hasPeriodPassed(0.5):
                    self.sd.putBoolean("SupportsDisplacement: ", self.navx._isDisplacementSupported())
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
