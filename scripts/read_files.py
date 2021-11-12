from pathlib import Path

from scripts.detect_god_line import detect_god_line


def read_files(directory):
    """
    Function used to iterate and read over all python files within a specified directory.
    :param directory: The directory to begin with.
    :return:
    """
    count = 0
    god_lines = 0
    files = directory.glob('**/*.py')
    for file in files:
        count += 1
        with open(Path(file), 'r') as f:
            god_lines = detect_god_line(f, god_lines)
    print(count, god_lines)
