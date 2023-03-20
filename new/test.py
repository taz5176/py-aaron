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
            max_retries,
            log,
            raw_data_file='raw_data.csv'
    ):
        """
        Method to initialise Device class

        Args:
            test_loops (int): Number of tests to run
            max_retries (int): Max. no. of retries
            log (obj): logging obj
            raw_data (str, optional): raw data filename. 
                Defaults to 'raw_data.csv'.
        """
        self.test_loops = test_loops
        self.max_retries = max_retries
        self.all_results = []
        self.log = log
        self.raw_data_file = raw_data_file


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

    
    def run(self):
        """
        Method to run tests, display and save results

        Args:
            log (obj): Logger instance
        """
        self.log.info('Check Device Status Test... Starting')
        self.log.info(f'> Test loops: {self.test_loops}, Max retries: {self.max_retries}')
        
        status_gen = Status_Generator()
        for loop in range(self.test_loops):
            self.log.info(f'****** LOOP {loop+1}: Starting')
            
            for retry in range(self.max_retries+1):
                device = Device(
                    Common.get_datetime_str(),
                    loop+1,
                    RESULT['NOT_RUN']
                )
                status = status_gen.check_status()
                self.log.info(f'* Status: {status}')
                if status == STATUS['ABNORMAL']:
                    result = RESULT['FAIL']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    self.log.debug(f'{device.result}')
                    break

                elif status == STATUS['NORMAL']:
                    result = RESULT['PASS']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    self.log.debug(f'{device.result}')
                    break

                elif status == STATUS['NO_DEVICE']:
                    result = RESULT['FAIL']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    self.log.debug(f'{device.result}')
                    if retry < self.max_retries:
                        self.log.info(f'>>> Retry {retry+1}')
            
            self.log.info(f'****** LOOP {loop+1}: {"Retry" if retry > 0 else ""} {result}')

            # to exit testing
            if status == STATUS['ABNORMAL']:
                break
        
        self.log.info('Check Device Status Test... Complete')
        self.save_file()

        # for i in self.all_results:
        #     print(i.result)


    def save_file(self):
        """
        Method to save test data to file
        """
        # check if file exist
        file_exist = Common.file_exist(self.raw_data_file)
        if file_exist:
            wr_mode = 'a'
        else:
            wr_mode = 'w'
        
        with open(self.raw_data_file, wr_mode) as wf:
            # file not exist, to write header first
            if not file_exist:
                for k in self.all_results[0].result.keys():
                    wf.write(k)
                    if k != list(self.all_results[0].result.keys())[-1]:
                        wf.write(',')
                wf.write('\n')
            # to write current test result raw self.all_results to file
            for i in self.all_results:
                for v in i.result.values():
                    wf.write(str(v))
                    if v != list(i.result.values())[-1]:
                        wf.write(',')
                wf.write('\n')
            self.log.info(f'Write raw data to {self.raw_data_file}')


def main():
    """
    Main method to execute
    """
    # log = Logger(
    #     loglevel=LOGLEVEL['INFO']
    # ).log
    log = Logger(
        logfile_name='test.log',
        loglevel=LOGLEVEL['INFO']
    ).log
    test = Test(
        test_loops=10,
        max_retries=3,
        log=log
    )
    test.run()


if __name__ == '__main__':
    main()