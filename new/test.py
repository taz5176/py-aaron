from device import Device
from common import Common
from logger import Logger
from constants import LOGLEVEL, RESULT, STATUS
from status_generator import Status_Generator


class Test(Device):
    """
    Device class 
    to run tests and store all results

    Args:
        Device (obj): store 1 run result
            including retries
    """
    def __init__(
            self,
            test_loops,
            max_retries
    ):
        """
        Method to initialise Device class

        Args:
            test_loops (int): Number of tests to run
            max_retries (int): Max. no. of retries
        """
        self.test_loops = test_loops
        self.max_retries = max_retries
        self.all_results = []


    def update(self, device, status, retry, test_result):
        """
        Method to update device test result to
         test_result list

        Args:
            device (obj): Store 1 run result
            status (str): Device return status
            retry (int): Max. no. of retries
            test_result (str): Test result (pass/fail)
        """
        device.update_result(
            status,
            retry,
            test_result
        )
        self.all_results.append(device)

    
    def run(self, log):
        """
        Method to run tests, display and save results

        Args:
            log (obj): Logger instance
        """
        log.info('Check Device Status Test... Starting')
        log.info(f'> Test loops: {self.test_loops}, Max retries: {self.max_retries}')
        
        status_gen = Status_Generator()
        for loop in range(self.test_loops):
            log.info(f'****** LOOP {loop+1}: Starting')
            
            for retry in range(self.max_retries+1):
                device = Device(
                    Common.get_datetime_str(),
                    loop+1,
                    RESULT['NOT_RUN']
                )
                status = status_gen.check_status()
                log.info(f'* Status: {status}')
                if status == STATUS['ABNORMAL']:
                    result = RESULT['FAIL']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    log.debug(f'{device.result}')
                    break

                elif status == STATUS['NORMAL']:
                    result = RESULT['PASS']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    log.debug(f'{device.result}')
                    break

                elif status == STATUS['NO_DEVICE']:
                    result = RESULT['FAIL']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    log.debug(f'{device.result}')
                    if retry < self.max_retries:
                        log.info(f'>>> Retry {retry+1}')
            
            log.info(f'****** LOOP {loop+1}: {result}')

            # to exit testing
            if status == STATUS['ABNORMAL']:
                break
        
        log.info('Check Device Status Test... Complete')
    
        # for i in self.all_results:
        #     print(i.result)

        # data = self.all_results
        # for k in data[0].result.keys():
        #     print(k, end=',')
        # print()
        # for i in data:
        #     for v in i.result.values():
        #         print(v, end=',')
        #     print()


def main():
    """
    Main method to execute
    """
    # log = Logger(
    #     loglevel=LOGLEVEL['INFO']
    # ).log
    log = Logger(
        logfile_name=f'{Common.get_datetime_str()}.log',
        loglevel=LOGLEVEL['INFO']
    ).log
    test = Test(
        test_loops=10,
        max_retries=3
    )
    test.run(log)


if __name__ == '__main__':
    main()