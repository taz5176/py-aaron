import datetime

from pathlib import Path


class Common:
    """
    Class for commonly used functions
    - get datetime string 
    """
    def get_datetime_str() -> str:
        """
        Method to get current datetime string

        Returns:
            str: Current datetime
        """
        dt = datetime.datetime.now()
        return datetime.datetime.strftime(dt, '%Y%m%dT%H%M%S')
    

    def path_exist(fullpath: str) -> bool:
        """
        Method to check if path exist

        Args:
            fullpath (str): Full path to be checked

        Returns:
            bool: Path exists?
        """
        return True if Path(fullpath).exists() else False
    

    def path_join(file: str, folder=None) -> str:
        """
        Method to join path to current working
        directory

        Args:
            path (str): Folder or file name

        Returns:
            str: New path
        """
        if folder is None:
            p = Path.cwd()
        else:
            p = Path(Path.cwd() / folder)
        return Path(p / file)


    def create_folder(folder: str) -> str:
        """
        Method to create folder

        Args:
            folder (str): folder to be created

        Returns:
            str: result message
        """
        p = Path(Path.cwd() / folder)
        if not Common.path_exist(p):
            Path(Path.cwd() / folder).mkdir()
        #     return True
        # return False


if __name__ == '__main__':
    # testing
    # print(Common.get_datetime_str())
    # print(Common.path_exist(Path.cwd()))
    print(Common.create_folder('test'))
    # print(Common.path_join('test'))