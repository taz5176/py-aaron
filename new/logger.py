import logging

from constants import LOGLEVEL


class Logger:
    """
    Logger class
    """
    def __init__(
            self,
            logfile_name=None,
            loglevel=LOGLEVEL['DEBUG']
    ):
        """
        Logger class constructor

        Args:
            logfile_name (str, optional): Log filename. 
                Set filename to save execution log.
            loglevel (int, optional): Defaults to INFO.
                0   - NOTSET
                10  - DEBUG
                20  - INFO
                30  - WARNING
                40  - ERROR
                50  - CRITICAL
        """
        self.logfile_name = logfile_name if logfile_name else None
        self.loglevel = loglevel 
        self.init_logging()
    

    def init_logging(self):
        """
        Method to intialise logging
        """
        log_formatter = logging.Formatter(
            "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        log = logging.getLogger()
        log.setLevel(self.loglevel)
        log.addHandler(console_handler)
        if self.logfile_name is not None:
            file_handler = logging.FileHandler(f'{self.logfile_name}')
            file_handler.setFormatter(log_formatter)
            log.addHandler(file_handler)
        self.log = log


if __name__ == '__main__':
    # for testing
    mylogger = Logger(logfile_name='test.log',
                        loglevel=LOGLEVEL['INFO'])
    mylogger.log.debug('debug message')
    mylogger.log.info('info message')
    mylogger.log.warning('warn message')
    mylogger.log.error('error message')
    mylogger.log.critical('critical message')