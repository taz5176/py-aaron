
import json, os

from device import Device
from common import Common
# from comm import Common
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
            folder='raw',
            input=None,
            output=f'{Common.get_datetime_str()}.csv'
    ):
        """
        Method to initialise Device class

        Args:
            test_loops (int): Number of tests to run
            max_retries (int): Max. no. of retries
            log (obj): Logging obj
            folder (str, optional): Folder contains test
                test files. Defaults to 'raw' folder 
            file (str, optional): Test data filename. 
                Defaults to current datetime.
        """
        self.test_loops = test_loops
        self.max_retries = max_retries
        self.all_results = []
        self.log = log
        self.folder = folder
        self.input = input
        self.output = output
        # initialise status summary to 0
        self.status_summary = {
            STATUS['ABNORMAL']: 0,
            STATUS['NORMAL']: 0,
            STATUS['NO_DEVICE']: 0
        }
        # initialise summary table to empty list
        self.summary_table = []


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


    def save_data(self):
        """
        Method to save test data to file
        """
        # check if file exist
        file_exist = Common.path_exist(self.folder, self.output)
        if file_exist:
            wr_mode = 'a'
        else:
            wr_mode = 'w'
        
        # get file full path
        file_path = Common.get_new_filepath(
            folder=self.folder, 
            file=self.output
        )
        with open(file_path, wr_mode) as wf:
            # if file doesn't exist, to write header first
            if not file_exist:
                for k in self.all_results[0].result.keys():
                    wf.write(k)
                    if k != list(self.all_results[0].result.keys())[-1]:
                        wf.write(',')
                wf.write('\n')
            # write current test result data to file
            for i in self.all_results:
                for v in i.result.values():
                    wf.write(str(v))
                    if v != list(i.result.values())[-1]:
                        wf.write(',')
                wf.write('\n')
            self.log.debug(f'Write data to {self.output}')


    def read_data(self, fullpath):
        try:
            self.log.info(f'Reading {fullpath}')
            with open(fullpath, 'r') as rf:
                next(rf)
                lines = rf.readlines()

                for line in lines:
                    line = line.strip('\n')
                    items = line.split(',')
                    device = Device(
                        dt=items[0],
                        loop=int(items[1]),
                        status=items[2],
                        retry=int(items[3]),
                        test_result=items[4]
                    )
                    self.log.debug(f'\n{device.result}')
                    self.all_results.append(device)
            self.log.info('File read and processed successfully')
            return True

        except Exception as e:
            self.log.error(e)


    def get_status_summary(self):
        """
        Method to display status summary
        """
        for i in self.all_results:
            if i.result['retry'] == 0:
                self.status_summary[i.result['status']] += 1
        self.log.info(
            f'Status summary: \n{json.dumps(self.status_summary, indent=2)}'
        )


    def get_summary_table(self):
        """
        Method to display summary table
        """
        for n, i in enumerate(self.all_results):
            if i.result['retry'] == 0:
                each_loop = {'Loop':i.result['loop']}
                each_loop.update({'Status':i.result['status']})
                self.summary_table.append(each_loop)
            
            result = f'{"Retry " if i.result["retry"] > 0 else ""}{i.result["test_result"]}'
            self.summary_table[i.result['loop']-1].update({'Result':result})
        self.log.debug(f'Summary table: \n{json.dumps(self.summary_table, indent=2)}')


    def process(self):
        self.log.info('Processing data file... Starting')
        if self.read_data(os.path.join(os.getcwd(), 'raw', '20230321T200118.csv')):
        # self.read_data(os.path.join(os.getcwd(), 'raw', '20230322T113029.csv'))

            self.get_status_summary()
            self.get_summary_table()
        self.log.info('Processing data file... Complete')

    
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
            self.log.info(f'>>> LOOP {loop+1}: Starting')
            
            for retry in range(self.max_retries+1):
                device = Device(
                    Common.get_datetime_str(),
                    loop+1,
                    RESULT['NOT_RUN']
                )
                status = status_gen.check_status()
                if retry == 0:
                    self.log.info(f'Status: {status}')
                else:
                    self.log.debug(f'Status: {status}')
                if status == STATUS['ABNORMAL']:
                    result = RESULT['FAIL']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    self.log.debug(f'\n{device.result}')
                    break

                elif status == STATUS['NORMAL']:
                    result = RESULT['PASS']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    self.log.debug(f'\n{device.result}')
                    break

                elif status == STATUS['NO_DEVICE']:
                    result = RESULT['FAIL']
                    self.update(
                        device,
                        status,
                        retry,
                        result
                    )
                    self.log.debug(f'\n{device.result}')
                    if retry < self.max_retries:
                        self.log.debug(f'>>>> Retry {retry+1}')
            
            self.log.info(f'>>> LOOP {loop+1}: {"Retry " if retry > 0 else ""}{result}')

            # to exit testing
            if status == STATUS['ABNORMAL']:
                break
        
        self.log.info('Check Device Status Test... Complete')
        self.save_data()
        self.get_status_summary()
        self.get_summary_table()


def main():
    """
    Main method to execute
    """
    # log = Logger(
    #     loglevel=LOGLEVEL['DEBUG']
    # ).log
    log = Logger(
        loglevel=LOGLEVEL['INFO']
    ).log
    test = Test(
        test_loops=10,
        max_retries=3,
        log=log
    )
    test.run()
    # test.process()


if __name__ == '__main__':
    main()