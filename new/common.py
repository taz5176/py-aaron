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


    def path_exist(folder=None, file=None):
        """
        Method to check if path exist

        Args:
            folder (str, optional): Folder name. Defaults to None.
            file (str, optional): File name. Defaults to None.

        Returns:
            bool: True if path exist, else false
        """
        if folder is None:
            folder = ''
        if file is None:
            file = ''
        new_path = os.path.join(os.getcwd(), folder, file)
        return os.path.exists(new_path)


    def get_new_filepath(folder=None, file=None):
        """
        Method to get the file or folder full path

        Args:
            folder (str, optional): Folder name. 
                Defaults to None.
            file (str, optional): File name. 
                Defaults to None.

        Returns:
            str: File or folder full path
        """
        if folder is None:
            folder = ''
        if file is None:
            file = ''
        if not Common.path_exist(folder):
            os.mkdir(folder)
        return os.path.join(os.getcwd(), folder, file)


    def output_path(folder=None, file=None):
        if folder is None:
            folder = ''
        if file is None:
            file = ''
        if not os.path.join(os.getcwd(), folder):
            os.mkdir(folder)
        return os.path.join(os.getcwd(), folder, file)


if __name__ == '__main__':
    # for testing
    print(Common.get_datetime_str())
