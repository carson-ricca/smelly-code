import os


def mkdir_if_not_exists(path: str, multiple_directories=False):
    """
    Creates a directory if it doesn't already exist.
    :param path: The path to create the new directory.
    :param multiple_directories: A boolean that determines whether the path will need multiple directories.
    """
    if not os.path.exists(path):
        if not multiple_directories:
            os.mkdir(path)
        else:
            os.makedirs(path)
