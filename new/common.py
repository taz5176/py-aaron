import datetime, os


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


    def file_exist(filename):
        filepath = os.path.join(os.getcwd(), filename)
        return os.path.exists(filepath)


if __name__ == '__main__':
    # for testing
    print(Common.get_datetime_str())
