__author__ = 'dhruv and alex m'


import core.GRTConstants as GRTConstants
import grt.mechanism.drivetrain as drivetrain
import grt.sensors.encoder as GRTEncoder
#import controller.DeadReckoner
import core.GRTConstants
import core.GRTMacro

import wpilib
import grt.mechanism.drivetrain

#import event.listeners.ConstantUpdateListener
import grt.mechanism.drivetrain
import grt.sensors.encoder





"""
* Creates a new Driving Macro
                        *
                        * @param dt GRTDriveTrain object
                                                  * @param distance distance to travel in meters (assumes travel in straight line)
* @param timeout time in ms
                         */"""


class Macrodrive(core.GRTMacro):
    dt = drivetrain
    left_initial_distance = None
    right_initial_distance = None
    DTContoller = wpilib.PIDController()
    straight_contoller = wpilib.PIDController()
    left_encoder = GRTEncoder()
    right_encoder = GRTEncoder()
    speed = None
    leftSF = 1
    rightSF = 1
    DTP = None
    DTI = None
    DTD = None
    CP = None
    CI = None
    CD = None
    TOLERANCE = None
    MAX_MOTOR_OUTPUT = None

    distance = None
    previously_on_target = False

    def __init__(self, dt, distance, timeout):
        GRTMacro.__init__("Drive Macro", timeout)
        self.dt = dt
        self.distance = distance
        self.leftEncoder = dt.getLeftEncoder()
        self.rightEncoder = dt.getRightEncoder()
        self.updateConstants()
        # GRTConstants.addListener(self) TODO
    def initialize(self):
        self.leftInitialDistance = self.leftEncoder.getDistance()
        self.rightInitialDistance = self.rightEncoder.getDistance()

        self.DTController.setSetpoint(self.distance)
        self.straightController.setSetpoint(0)
        self.DTController.enable()
        self.straightController.enable()

        self.leftSF = self.rightSF = 1
        print("MACRODRIVE is initialized")

    class DTSource(wpilib.PIDSource):
        def __init__(self):
            wpilib.PIDSource.__init__(self)
        def pidGet(self, right_traveled_distance, left_traveled_distance):
            self.distance = -(right_traveled_distance() + left_traveled_distance())/2
            print("Distance Traveled: " + self.distance)
            return self.distance


    class DTOutput(wpilib.PIDOutput):
        def __init__(self):
            wpilib.PIDOutput.__init__(self)
        def pidWrite(self, output, setSpeed, updateMotorSpeeds):
            setSpeed(output)
            updateMotorSpeeds()



    def updateMotorSpeeds(self):
        print("Speed: " + self.speed + "\tleftSF: " + self.leftSF + "\trightSF: " + self.rightSF)
        self.dt.setMotorSpeeds(self.speed * self.leftSF, self.speed * self.rightSF)

    def rightTraveledDistance(self):
        return self.rightEncoder.getDistance() - self.rightInitialDistance

    def leftTraveledDistance(self):
        return self.leftEncoder.getDistance() - self.leftInitialDistance


    DTController = wpilib.PIDController(DTP, DTI, DTD, DTSource, DTOutput)
    straightController = wpilib.PIDController(CP, CI, CD, straightSource, straightOutput)
    straightController.setOutputRange(0, 1)
        """
    * Use distance difference, rather than speed difference, to keep
    * robot straight
    """
    class straightSource(wpilib.PIDSource):
        def __init__(self):
            wpilib.PIDSource.__init__(self)
        def pidGet(self):
            return self.rightTraveledDistance() - self.leftTraveledDistance()

    class straightOutput(wpilib.PIDOutput):
        def __init__(self):
            wpilib.PIDOutput.__init__(self)
        def pidWrite(self, output):
            modifier = Math.abs(output)
            print(output)
            #concise code is better code
            rightSF = 2 - self.modifier - (leftSF = 1 - (self.speed * output < 0 ? self.modifier : 0))
            #print("Left Speed: " + leftSF)
            #print("Right Speed: " + rightSF)
            self.updateMotorSpeeds()





    def perform(self):
        print("DTerror: " + DTController.getError())

        if (DTController.onTarget()):
            print("On target!")
            if (self.previouslyOnTarget):
                self.notifyFinished()
            else:
                self.previouslyOnTarget = True
        else:
            self.previouslyOnTarget = False

    def die(self):
        self.dt.setMotorSpeeds(0, 0)
        DTController.disable()
        self.straightController.disable()
        self.DeadReckoner.notifyDrive(self.getDistanceTraveled())


    def getDistanceTraveled(self):
        return (leftTraveledDistance() + rightTraveledDistance()) / 2


    def updateConstants(self):
        self.DTP = GRTConstants.getValue("DMP")
        self.DTI = GRTConstants.getValue("DMI")
        self.DTD = GRTConstants.getValue("DMD")
        self.CP = GRTConstants.getValue("DMCP")
        self.CI = GRTConstants.getValue("DMCI")
        self.CD = GRTConstants.getValue("DMCD")
        self.TOLERANCE = GRTConstants.getValue("DMTol")
        self.MAX_MOTOR_OUTPUT = GRTConstants.getValue("DMMax")

        DTController.setPID(self.DTP, self.DTI, self.DTD)
        self.straightController.setPID(self.CP, self.CI, self.CD)
        DTController.setAbsoluteTolerance(self.TOLERANCE)
        DTController.setOutputRange(-self.MAX_MOTOR_OUTPUT, self.MAX_MOTOR_OUTPUT)