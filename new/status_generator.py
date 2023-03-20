import random, time

from constants import STATUS


class Status_Generator:
    """
    Status_Generator class to generate random device status
    """
    def _init_(self):
        """
        Status genertor class constructor
        """
        self.status = "No Device"
    

    def check_status(self):
        """
        Method to generate random device status

        Returns:
            str: Device status
        """
        status = [v for v in STATUS.values()]
        # generate status: 
        #   higher weightage = higher possibility
        #   lower weight = lower possibility
        #   0 = not possible
        # weights=('Abnormal', 'Normal', 'No Device')
        self.status = random.choices(status, weights=(1, 3, 6))[0]
        # time.sleep(1)
        return self.status


if __name__ == '__main__':
    # for testing
    device = Status_Generator()
    for i in range(10):
        print(device.check_status())