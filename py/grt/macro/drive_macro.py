__author__ = 'dhruv'

import controller.DeadReckoner
import core.GRTConstants
import core.GRTMacro
import edu.wpi.first.wpilibj.PIDController
import edu.wpi.first.wpilibj.PIDOutput
import edu.wpi.first.wpilibj.PIDSource
import event.listeners.ConstantUpdateListener
import grt.mechanism.drivetrain
import grt.sensors.encoder


class GRTPIDSource(PIDSource):
    def __init__(self):
        PIDSource.__init__(self)

    def pidGet(self, right_traveled_distance, left_traveled_distance):
        distance = -(right_traveled_distance() + left_traveled_distance())/2
        print("Distance Traveled: " + distance)
        return distance


class GRTPIDOutput(PIDOutput):
    def __init__(self):
        PIDOutput.__init__(self)

    def pidWrite(self, output, setSpeed, updateMotorSpeeds):
        setSpeed(output)
        updateMotorSpeeds()

class Macrodrive()