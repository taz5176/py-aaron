import random, datetime
import time

class Device():
    
    def __init__(self, dt, loop, result):
        self.result = {
            'dt': dt,
            'loop': loop,
            'status': None,
            'retry': 0,
            'result': result
        }
        
        
    def update(self, status, retry, result):
        # self.update_device_dt(dt)
        self.update_device_status(status)
        self.update_device_retry(retry)
        self.update_device_result(result)
        

    def update_device_dt(self, dt):
        self.result['dt'] = dt
        

    def update_device_loop(self, loop):
        self.result['loop'] = loop
        
        
    def update_device_status(self, status):
        self.result['status'] = status
        
        
    def update_device_retry(self, retry):
        self.result['retry'] = retry
        
        
    def update_device_result(self, result):
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
        self.test_retries = retries
        self.all_results = []
        
        
    def update_test_result(self, device):
        self.all_results.append(device)


    def print_all_results(self):
        for i in self.all_results:
            print(i.result)
            
    
    def run(self, loops=10):
        print('>>> Beginning Check Device Status')
        for loop in range(loops):
            print(f' Loop {loop+1}:', end=' ')

            for retry in range(self.test_retries+1):
                device = Device(Testing.get_dt(), 
                                loop+1,
                                Testing.RESULT['NOT_RUN'])
                
                # simulate run test to get status
                status = get_device_status()
                print(f'{status}')
                
                if status == Testing.STATUS['NORMAL']:
                    result = Testing.RESULT['PASS']
                    device.update(status, retry, result)
                    self.update_test_result(device)
                    break
                
                elif status == Testing.STATUS['ABNORMAL']:
                    result = Testing.RESULT['FAIL']
                    device.update(status, retry, result)
                    self.update_test_result(device)
                    break
                
                elif status == Testing.STATUS['NO_DISK']:
                    result = Testing.RESULT['FAIL']
                    device.update(status, retry, result)
                    self.update_test_result(device)
                    if retry == 0:
                        print('>>>> No Disk Found, Beginning Retry')
                    if retry < self.test_retries:
                        print(f'>>>> Retry Count {retry+1}:', end=' --- ')
                
            if status == Testing.STATUS['ABNORMAL']:
                break
            
    @staticmethod
    def get_dt():
        dt_now = datetime.datetime.now()
        return datetime.datetime.strftime(dt_now, '%Y%m%dT%H%M%S') 
         

# Main sequence function
def get_device_status():
    
    # Simulate device status
    status = random.choice(["Normal", 
                            "Abnormal", 
                            "No Disk", 
                            "No Disk", 
                            "No Disk"])
    # time.sleep(1)  # Simulate processing time
    return status


def main():
    test = Testing()
    test.run(loops=10)

    # test.print_all_results()
    

if __name__ == '__main__':
    main()