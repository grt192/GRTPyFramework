__author__ = 'dhruv and alex m'

from grt.core import GRTMacro
import wpilib
import threading

#constants = Constants()


class ElevatorMacro(GRTMacro):
    """
    Drive Macro; drives forwards a certain distance while
    maintaining orientation
    """
    leftSF = 1
    rightSF = -1
 #   DTP = constants['DTP']
  #  DTI = constants['DTI']
   # DTD = constants['DTD']
    #CP = constants['CP']
    #CI = constants['CI']
    #CD = constants['CD']
    #TOLERANCE = constants['DMtol']
    #MAX_MOTOR_OUTPUT = constants['DMMAX']

    distance = None
    previously_on_target = False

    def __init__(self, elevator, distance, timeout):
        """
        Pass drivetrain, distance to travel (ft), and timeout (secs)
        """
        super().__init__(timeout)
        self.elevator= elevator
        self.distance = distance
        self.elevator_encoder = elevator.elevator_encoder
        
        self.setpoint = distance
        #self.dt_output = self.DTOutput(self)
        #self.dt_source = self.DTSource(self)
        #self.straight_source = self.StraightSource(self)
        #self.straight_output = self.StraightOutput(self)
        #self.DTController = wpilib.PIDController(self.DTP, self.DTI, self.DTD, self.dt_source, self.dt_output)
        #self.straight_controller = wpilib.PIDController(self.CP, self.CI, self.CD,
         #                                               self.straight_source, self.straight_output)
        #self.straight_controller.SetOutputRange(0, 1)

        #self.DTController.SetPID(self.DTP, self.DTI, self.DTD)
        #self.straight_controller.SetPID(self.CP, self.CI, self.CD)
        #self.DTController.SetAbsoluteTolerance(self.TOLERANCE)
        #self.DTController.SetOutputRange(-self.MAX_MOTOR_OUTPUT, self.MAX_MOTOR_OUTPUT)

    def initialize(self):
        self.initial_distance = self.elevator_encoder.e.getDistance()
        self.run_elevator_macro()
        

    """
    def initialize(self):
        self.left_initial_distance = self.left_encoder.e.GetDistance()
        self.right_initial_distance = self.right_encoder.e.GetDistance()
        self.right_thread = threading.thread(target=self.run_right_drive_macro)
        self.left_thread = threading.thread(target=self.run_left_drive_macro)
        self.right_thread.start()
        self.left_thread.start()
        

        #self.DTController.SetSetpoint(self.distance)
        #self.straight_controller.SetSetpoint(0)
        #self.DTController.Enable()
        #self.straight_controller.Enable()

        #self.leftSF = self.rightSF = 1
        print("Starting DriveMacro")

    def update_motor_speeds(self):
        self.dt.set_dt_output(self.speed * self.leftSF, self.speed * self.rightSF)
    """
    

    def traveled_distance(self):
        return self.elevator_encoder.distance - self.initial_distance

    def get_distance_traveled(self):
        """
        Return average of left_traveled_distance and right_traveled_distance
        """
        return (self.left_traveled_distance() + self.right_traveled_distance()) / 2

    

    def run_elevator_macro(self):
        if(self.setpoint>0):
            while(self.traveled_distance() < self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(.6)
            while(self.traveled_distance() < self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(.3)
            self.elevator.stop()
        elif(self.setpoint<0):
            while(self.traveled_distance() > self.setpoint * .8):
                print("travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(-.6)
            while(self.traveled_distance() > self.setpoint):
                print("half power travel: %f" % self.traveled_distance())
                self.elevator.elevate_speed(-.3)
            self.elevator.stop()
        self.kill()
    """
    def perform(self):
        #print("DTerror: " + str(self.DTController.GetError()))
        #print("Left Traveled Distance:" + str(self.left_traveled_distance()))
        #print("Right Traveled Distance:" + str(self.right_traveled_distance()))

        #print("Distance Traveled: " + str(self.get_distance_traveled()))
        if (self.DTController.OnTarget()):
            print("On target!")
            if (self.previously_on_target):
                self.kill()
            else:
                self.previously_on_target = True
        else:
            self.previously_on_target = False

    def die(self):
        self.dt.set_dt_output(0, 0)
        #self.DTController.Disable()
        #self.straight_controller.Disable()
    """
    
    
