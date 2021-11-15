from pathlib import Path

from scripts.detect_function_length import detect_function_length
from scripts.detect_god_line import detect_god_line
from scripts.detect_identifier_size import detect_identifier_size
from scripts.detect_lazy_class import detect_lazy_class
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
    function_length = 0
    lazy_class = 0

    files = directory.glob('**/*.py')
    for file in files:
        count += 1
        with open(Path(file), 'r') as f:
            god_lines = detect_god_line(f, god_lines)
            f.seek(0)
            too_many_parameters = detect_many_parameters(f, too_many_parameters)
            f.seek(0)
            identifier_size = detect_identifier_size(f, identifier_size)
            f.seek(0)
            function_length = detect_function_length(f, function_length)
            f.seek(0)
            lazy_class = detect_lazy_class(f, lazy_class)
    print('Count: {0}\nGod Lines: {1}\nToo Many Parameters: {2}\nIdentifier Size: {3}\nFunction Too Long: {4}\nLazy '
          'Class: {5} '
          .format(count, god_lines, too_many_parameters, identifier_size, function_length, lazy_class))
