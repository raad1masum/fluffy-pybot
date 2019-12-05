def robotMap(self):

    # Motor Map
    self.motorLeftFront = 10;
    self.motorLeftMiddle = 21;
    self.motorLeftBack = 23;
    self.motorRightFront = 11;
    self.motorRightMiddle = 20;
    self.motorRightBack = 22;

    # Xbox Controller Map
    self.xboxController = 0;
    self.leftStickY = 1;
    self.rightStickY = 5;
    self.xButton = 3;
    self.yButton = 4;

    # Joystick Controller Map
    self.joystickController = 1;
    self.shotgunStickY = 2;
    self.shotgunStickX = 3;

    #  Gyro map
    self.gyro = 9;

    # Weights
    self.leftStickNerf = 0.7;
    self.rightStickNerf = 0.7;
    self.leftSlow = 0.24;
    self.rightSlow = -0.24;
    self.rotateSpeed = 0.35;
    self.rotateSpeedSlow = 0.25;