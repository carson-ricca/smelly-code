from pathlib import Path

from scripts.detect_god_line import detect_god_line
from scripts.detect_identifier_size import detect_identifier_size
from scripts.detect_many_parameters import detect_many_parameters


def read_files(directory):
    """
    Function used to iterate and read over all python files within a specified directory.
    :param directory: The directory to begin with.
    :return:
    """
    count = 0
    god_lines = 0
    too_many_parameters = 0
    identifier_size = 0
    files = directory.glob('**/*.py')
    for file in files:
        count += 1
        with open(Path(file), 'r') as f:
            god_lines = detect_god_line(f, god_lines)
            f.seek(0)
            too_many_parameters = detect_many_parameters(f, too_many_parameters)
            f.seek(0)
            identifier_size = detect_identifier_size(f, identifier_size)
    print('Count: {0}\nGod Lines: {1}\nToo Many Parameters: {2}\nIdentifier Size: {3}'
          .format(count, god_lines, too_many_parameters, identifier_size))
