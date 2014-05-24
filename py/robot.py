__author__ = "Sidd Karamcheti, Calvin Huang, Alex Mallery, Dhruv Rajan"

crio_native = True
try:
    import wpilib
except ImportError:
    from pyfrc import wpilib
    crio_native = False


from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.sensors.gyro import Gyro
from grt.core import SensorPoller, Constants
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import ArcadeDriveController
from grt.mechanism.motorset import Motorset
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
#from config import sp, hid_sp, dt, ds
from grt.sensors.twist_joystick import TwistJoystick
from grt.mechanism.centric_controller import CentricDriveController
from grt.mechanism.mecanum_dt import MecanumDT
import time

try:
    auto = basicauto
except NameError:
    auto_exists = False


class MyRobot(wpilib.SimpleRobot):
    def __init__(self):
        self.watchdog = wpilib.GetWatchdog()
        import config
        self.sp = config.sp
        self.hid_sp = config.hid_sp
        

    def Disabled(self):
        if auto_exists:
            auto.stop_autonomous()
        self.watchdog.SetEnabled(False)
        while self.IsDisabled():
            tinit = time.time()
            self.sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))

    if auto_exists:
        def Autonomous(self):
            global auto
            dt.upshift()
            self.watchdog.SetEnabled(False)

            if ds.GetDigitalIn(1):
                auto = twoballauto
            else:
                auto = basicauto

            auto.run_autonomous()
            while self.IsAutonomous() and self.IsEnabled():
                tinit = time.time()
                sp.poll()
                wpilib.Wait(0.04 - (time.time() - tinit))
            auto.stop_autonomous()
    else:
        def Autonomous(self):
            pass

    def OperatorControl(self):
        #dt.downshift()  # start in low gear for tele
        self.watchdog.SetExpiration(0.25)
        self.watchdog.SetEnabled(True)

        if auto_exists:
            auto.stop_autonomous()

        while self.IsOperatorControl() and self.IsEnabled():
            self.watchdog.Feed()
            tinit = time.time()
            self.sp.poll()
            self.hid_sp.poll()
            wpilib.Wait(0.04 - (time.time() - tinit))


def run():
    robot = MyRobot()
    robot.StartCompetition()
    if not crio_native:
        return robot

if not crio_native:
    if __name__ == '__main__':
        wpilib.run(min_version='2014.4.0')


#Old robot.py __init__ code from before config worked
"""constants = Constants()
        #Pin/Port map

        #Use the motors in the order fl, fr, rl, rr.
        fl_motor = wpilib.Talon(1)
        fr_motor = wpilib.Talon(2)
        rl_motor = wpilib.Talon(3)
        rr_motor = wpilib.Talon(4)

        #Solenoids + Relays
        compressor_pin = 1
        dt_shifter = wpilib.Solenoid(1)

        #Digital Sensors
        left_encoder = Encoder(3, 4, constants['dt_dpp'], reverse=True)
        right_encoder = Encoder(1, 2, constants['dt_dpp'])
        pressure_sensor_pin = 14

        #Analog Sensors
        gyro = Gyro(2)

        # Controllers
        driver_stick = TwistJoystick(1)
        xbox_controller = XboxJoystick(2)

        dt = MecanumDT(fl_motor, fr_motor, rl_motor, rr_motor, left_encoder=left_encoder, right_encoder=right_encoder, gyro=gyro)

        #Compressor
        compressor = wpilib.Compressor(pressure_sensor_pin, compressor_pin)
        compressor.Start()

        #Mechs

        #Teleop Controllers
        ac = CentricDriveController(dt, driver_stick)



        ds = wpilib.DriverStation.GetInstance()




        #Autonomous

        #Sensor Pollers
        self.sp = SensorPoller((gyro, dt.right_encoder,
                           dt.left_encoder))
        self.hid_sp = SensorPoller((driver_stick, xbox_controller))  # human interface devices"""
