import random, datetime
import time

class Device_Result():
    
    def __init__(self, dt, loop, result):
        self.result = {
            'dt': dt,
            'loop': loop,
            'status': None,
            'retry': 0,
            'result': result
        }
        
        
    def update(self, status, retry, result):
        # self.update_dt(dt)
        self.update_status(status)
        self.update_retry(retry)
        self.update_result(result)
        

    def update_dt(self, dt):
        self.result['dt'] = dt
        

    def update_loop(self, loop):
        self.result['loop'] = loop
        
        
    def update_status(self, status):
        self.result['status'] = status
        
        
    def update_retry(self, retry):
        self.result['retry'] = retry
        
        
    def update_result(self, result):
        self.result['result'] = result


class Testing(Device_Result):
    
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
        
        
    def update_result(self, device):
        self.all_results.append(device)


    def print_summary(self):
        for i in self.all_results:
            print(i)
            
    
    def run(self, loops=10):
        print('>>> Beginning Check Device Status')
        for loop in range(loops):
            print(f' Loop {loop+1}:', end=' ')

            for retry in range(self.test_retries+1):
                device = Device_Result(Testing.get_dt(), 
                                loop+1,
                                Testing.RESULT['NOT_RUN'])
                
                # simulate run test to get status
                status = get_device_status()
                print(f'{status}')
                
                if status == Testing.STATUS['NORMAL']:
                    result = Testing.RESULT['PASS']
                    device.update(status, retry, result)
                    self.update_result(device)
                    # print(f'{status}')
                    break
                
                elif status == Testing.STATUS['ABNORMAL']:
                    result = Testing.RESULT['FAIL']
                    device.update(status, retry, result)
                    self.update_result(device)
                    break
                
                elif status == Testing.STATUS['NO_DISK']:
                    result = Testing.RESULT['FAIL']
                    device.update(status, retry, result)
                    self.update_result(device)
                    if retry == 0:
                        print('>>>> No Disk Found, Beginning Retry')
                    if retry < self.test_retries:
                        print(f'>>>> Retry Count {retry+1}:', end=' --- ')
                
            if status == Testing.STATUS['ABNORMAL']:
                break
            # if retry > 3:
            #     device.update(status, retry, result)
            #     self.update_result(device)
            
    @staticmethod
    def get_dt():
        dt_now = datetime.datetime.now()
        return datetime.datetime.strftime(dt_now, '%Y%m%dT%H%M%S') 
         

# Main sequence function
def get_device_status():
    
    # Simulate device status
    status = random.choice(["Normal", "No Disk", "No Disk", "No Disk"])
    time.sleep(1)  # Simulate processing time
    return status


def main():
    test = Testing()
    test.run(loops=10)

    for i in test.all_results:
        print(i.result)
    

if __name__ == '__main__':
    main()