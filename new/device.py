from common import Common
from constants import RESULT, STATUS


class Device:
    """
    Class to save the each test result including retries
    """
    def __init__(
            self,
            dt,
            loop,
            test_result,
            status=None,
            retry=0
    ):
        """
        Method to initialise Device class

        Args:
            dt (str): Current datetime
            loop (int): Test loop count
            test_result (str): test result (pass/fail)
        """
        self.result = {
            'dt': dt,
            'loop': loop,
            'status': status,
            'retry': retry,
            'test_result': test_result
        }

    
    def update_dt(self, dt):
        """
        Method to update class attribute dt

        Args:
            dt (str): Current datetime
        """
        self.result['df'] = dt


    def update_loop(self, loop):
        """
        Method to update class attribute loop 

        Args:
            loop (int): Test loop count
        """
        self.result['loop'] = loop

    
    def update_status(self, status):
        """
        Method to update class attribute status

        Args:
            status (str): Device return status
        """
        self.result['status'] = status

    
    def update_retry(self, retry):
        """
        Method to update class attribute retry count

        Args:
            retry (int): Test retry count
        """
        self.result['retry'] = retry


    def update_test_result(self, test_result):
        """
        Method to update class attribute test result

        Args:
            test_result (str): Test result (pass/fail)
        """
        self.result['test_result'] = test_result


    def update_result(
            self,
            status, 
            retry, 
            test_result,
            dt=None,
            loop=None
        ):
        """
        Method to update class attribute result by
        updating the below Args class attribute

        Args:
            status (str): Device return status
            retry (int): Test retry count
            test_result (str): Test result (pass/fail)
        """
        if dt is not None:
            self.update_dt(dt)
        if loop is not None:
            self.update_loop(loop)
        self.update_status(status)
        self.update_retry(retry)
        self.update_test_result(test_result)


if __name__ == '__main__':
    # for testing
    test = Device(
        dt=Common.get_datetime_str(),
        loop=2,
        test_result=None
    )
    print(f'\n{test.result}')

    test.update_status(STATUS['NO_DEVICE'])
    test.update_test_result(RESULT['FAIL'])
    print(f'\n{test.result}')
    
    test.update_result(
        status=STATUS['NORMAL'],
        retry=2,
        test_result=RESULT['PASS']
    )
    print(f'\n{test.result}')