import datetime


class Common:
    """
    Class for commonly used functions
    - get datetime string 
    """
    def get_datetime_str():
        """
        Method to get current datetime string

        Returns:
            str: Current datetime
        """
        dt = datetime.datetime.now()
        return datetime.datetime.strftime(dt, '%Y%m%dT%H%M%S')
    

    def save_file(filename, data):
        with open(filename, 'w') as wf:
            for k in data[0].result.keys():
                wf.write(k, end=',')
            wf.write('\n')
            for i in data:
                for v in i.result.values():
                    wf.write(v, end=',')
                wf.write('\n')


if __name__ == '__main__':
    # for testing
    print(Common.get_datetime_str())
