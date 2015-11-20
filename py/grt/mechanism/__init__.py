class PickupShooter:
    def __init__(self, motor1, motor2):
        self.motor1 = motor1
        self.motor2 = motor2
        
    def start(self, power):
        self.motor1.set(power)
        self.motor2.set(-power)
        
    def stop(self):
        self.motor1.set(0)
        self.motor2.set(0)
        