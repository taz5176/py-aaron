import random

class Status:
    def _init_(self):
        self.status = "No Device"
    
    def check_status(self):
        # Simulate checking the status of the device
        self.status = random.choice(["Normal", "Abnormal", "No Device"])
        return self.status


""" testing """
device = Status()

for i in range(10):
    print(device.check_status())