import wpilib

from ctre.wpi_talonsrx import WPI_TalonSRX

def robotMap(self):

    # Motor Map
    self.motorLeftFront = WPI_TalonSRX(10)
    self.motorLeftMiddle = WPI_TalonSRX(21)
    self.motorLeftBack = WPI_TalonSRX(23)
    self.motorRightFront = WPI_TalonSRX(11)
    self.motorRightMiddle = WPI_TalonSRX(20)
    self.motorRightBack = WPI_TalonSRX(22)

    # Xbox Controller Map
    self.xboxController = wpilib.XboxController(0)
    self.xboxControllerLeftStickY = wpilib.XboxController(1)
    self.xboxControllerRightStickY = wpilib.XboxController(5)
    self.xboxControllerXButton = wpilib.XboxController(3)
    self.xboxControllerYButton = wpilib.XboxController(4)

    # Joystick Controller Map
    self.joystickController = wpilib.Joystick(1)
    self.joystickStickY = wpilib.Joystick(2)
    self.joystickStickX = wpilib.Joystick(3)

    #  Gyro map
    self.gyro = 9

    # Weights
    self.nerf = 0.6
    self.leftStickNerf = 0.6
    self.rightStickNerf = 0.6
    self.leftSlow = 0.24
    self.rightSlow = -0.24
    self.rotateSpeed = 0.35
    self.rotateSpeedSlow = 0.25