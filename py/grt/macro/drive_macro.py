__author__ = 'dhruv'

import core.GRTConstants as GRTConstants
import py.grt.core.GRTMacro as GRTMacro
import edu.wpi.first.wpilibj.PIDController as PIDController
import edu.wpi.first.wpilibj.PIDOutput
import edu.wpi.first.wpilibj.PIDSource
import event.listeners.ConstantUpdateListener
import py.grt.mechanism.drivetrain as drivetrain
import py.grt.sensors.encoder as GRTEncoder


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

class Macrodrive(GRTMacro):
    dt = drivetrain()
    left_initial_distance = None
    right_initial_distance = None
    DT_contoller = PIDController()
    straight_contoller = PIDController()
    left_encoder = GRTEncoder()
    right_encoder = GRTEncoder()
    speed = None
    left_sf = 1
    right_sf = 1
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
    DTsource