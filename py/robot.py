

import wpilib
import time
import os


class MyRobot(wpilib.SampleRobot):
    def __init__(self):
        super().__init__()
        import config
        self.hid_sp = config.hid_sp
        self.ds = config.ds


    def disabled(self):
        while self.isDisabled():
            tinit = time.time()
            self.hid_sp.poll()
            self.safeSleep(tinit, .04)
    
    def autonomous(self):
        # define auto here
        pass
    
    def operatorControl(self):
        i2c = wpilib.I2C(wpilib.I2C.Port.kOnboard, 40)
        i2c.transaction(bytes([61, 7]), 1)

        try:
            f = open('/home/lvuser/py/gyro.txt','w')
            f.write("gyro_x, gyro_y, gyro_z" + "\n")
        except IOError:
            print('cannot open', arg)
        else:
            print("Successfully opene the fil\n")

            while self.isOperatorControl() and self.isEnabled():
                tinit = time.time()
                self.hid_sp.poll()

                #data = i2c.read(0x18, 2)
                data = i2c.transaction(bytes([0]), 40)
                #print(str(data[0x14] + 256 * data[0x15]) + ", " + str(data[0x16] + 256 * data[0x17]) + ", " + str(data[0x18] + 256 * data[0x19]))
                gyro_x = data[0x14] + 256 * data[0x15]
                gyro_y = data[0x16] + 256 * data[0x17]
                gyro_z = data[0x18] + 256 * data[0x19]
                
                if (gyro_x < (2**15)):
                    gyro_x = gyro_x
                else:
                    gyro_x = gyro_x - 2**16

                if (gyro_y < (2**15)):
                    gyro_y = gyro_y
                else:
                    gyro_y = gyro_y - 2**16

                if (gyro_z < (2**15)):
                    gyro_z = gyro_z
                else:
                    gyro_z = gyro_z - 2**16

                print(gyro_x)
                print(gyro_y)
                print(gyro_z)

                #print("working")
                f.write(str(gyro_x) + ", " + str(gyro_y) + ", " + str(gyro_z) + "\n")


                self.safeSleep(tinit, .04)
            f.close()
            
    def safeSleep(self, tinit, duration):
        tdif = .04 - (time.time() - tinit)
        if tdif > 0:
            time.sleep(tdif)
        if tdif <= 0:
            print("Code running slowly!")


if __name__ == "__main__":
    wpilib.run(MyRobot)
