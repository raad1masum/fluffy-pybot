import wpilib

xboxController = 0
xboxControllerLeftStickY = 1
xboxControlleRightStickY = 5

def robotMap(self):

    # Motor Map
    self.motorLeftFront = 10
    self.motorLeftMiddle = 21
    self.motorLeftBack = 23
    self.motorRightFront = 11
    self.motorRightMiddle = 20
    self.motorRightBack = 22

    # Xbox Controller Map
    self.xboxController = 0
    self.xboxControllerLeftStickY = 1
    self.xboxControllerRightStickY = 5
    self.xboxControllerXButton = 3
    self.xboxControllerYButton = 4

    # Joystick Controller Map
    self.joystickController = 1
    self.joystickStickY = 2
    self.joystickStickX = 3

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