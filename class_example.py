import random, sys


class Device():
    
    def __init__(self, loop, result):
        self.result = {
            'loop': loop,
            'status': None,
            'retry': 0,
            'result': result
        }
        
        
    def update(self, status, retry, result):
        self.update_status(status)
        self.update_retry(retry)
        self.update_result(result)
        # print(self.result)
        
        
    def update_loop(self, loop):
        self.result['loop'] = loop
        
        
    def update_status(self, status):
        self.result['status'] = status
        
        
    def update_retry(self, retry):
        self.result['retry'] = retry
        
        
    def update_result(self, result):
        self.result['result'] = result


class Testing(Device):
    
    STATUS = {
        'NORMAL': 'Normal',
        'ABNORMAL': 'Abnormal',
        'NO_DISK': 'No Disk'
    }
    
    RESULT = {
        'PASS': 'Pass',
        'FAIL': 'Fail',
        'NOT_RUN': 'Not run'
    }
    
    def __init__(self,
                 retries=3):
        # super.__init__(self)
        self.retries = retries
        self.summary = []
        
        
    def update_result(self, device):
        self.summary.append(device)
        
    
    def run(self, loops=10):

        for loop in range(loops):
            # device = Device(loop, Testing.RESULT['NOT_RUN'])

            for retry in range(self.retries+1):
                device = Device(loop, Testing.RESULT['NOT_RUN'])
                # simulate run test to get status
                status = get_device_status()
                
                if status == Testing.STATUS['NORMAL']:
                    result = Testing.RESULT['PASS']
                    device.update(status, retry, result)
                    self.update_result(device)
                    break
                
                elif status == Testing.STATUS['ABNORMAL']:
                    result = Testing.RESULT['FAIL']
                    device.update(status, retry, result)
                    self.update_result(device)
                    break
                
                elif status == Testing.STATUS['NO_DISK'] and retry < self.retries+1:
                    result = Testing.RESULT['FAIL']
                    device.update(status, retry, result)
                    self.update_result(device)
                    
            # self.update_result(device)
            if status == Testing.STATUS['ABNORMAL']:
                break
            
         

# Main sequence function
def get_device_status():
    
    # Simulate device status
    status = random.choice(["Normal", "Abnormal", "No Disk", "No Disk", "No Disk"])
    # time.sleep(1)  # Simulate processing time
    return status


def main():
    test = Testing()
    test.run(loops=10)
    for i in test.summary:
        print(i.result)
    

if __name__ == '__main__':
    main()