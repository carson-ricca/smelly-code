from constants import Constants


def detect_god_line(file, count):
    """
    Determines the number of god_lines in a given file.
    :param file: The file to evaluate.
    :param count: The pre-existing count of god_lines in the directory.
    :return: The updated count of god_lines in the directory.
    """
    lines = file.readlines()
    for line in lines:
        if len(line) > Constants.MAX_LINE_LENGTH:
            count += 1
    return count
