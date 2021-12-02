from pathlib import Path

from scripts.detect_cyclomatic_complexity import detect_cyclomatic_complexity
from scripts.detect_data_class import detect_data_class
from scripts.detect_function_chains import detect_function_chains
from scripts.detect_function_length import detect_function_length
from scripts.detect_god_line import detect_god_line
from scripts.detect_identifier_size import detect_identifier_size
from scripts.detect_large_class import detect_large_class
from scripts.detect_lazy_class import detect_lazy_class
from scripts.detect_many_parameters import detect_many_parameters
from scripts.detect_middle_man import detect_middle_man


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
    large_class = 0
    function_chains = 0
    data_class = 0
    middle_man = 0
    cyclomatic_complexity = 0

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
            f.seek(0)
            function_chains = detect_function_chains(f, function_chains)
            f.seek(0)
            large_class = detect_large_class(f, large_class)
            f.seek(0)
            data_class = detect_data_class(f, data_class)
            f.seek(0)
            middle_man = detect_middle_man(f, middle_man)
            f.seek(0)
            cyclomatic_complexity = detect_cyclomatic_complexity(f, cyclomatic_complexity)
    print('Count: {0}\nGod Lines: {1}\nToo Many Parameters: {2}\nIdentifier Size: {3}\nFunction Too Long: {4}\nLazy '
          'Class: {5}\nFunction Chains: {6}\nLarge Class: {7}\nData Class: {8}\nMiddle Man: {9}\nCyclomatic '
          'Complexity: {10} '
          .format(count, god_lines, too_many_parameters, identifier_size, function_length, lazy_class, function_chains,
                  large_class, data_class, middle_man, cyclomatic_complexity))
