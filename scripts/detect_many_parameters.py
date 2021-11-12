import re

from constants import Constants


def detect_many_parameters(file, count):
    """
    Determines the number of functions that have too many parameters.
    :param file: The file to evaluate.
    :param count: The pre-existing count of too_many_parameters in the directory.
    :return: The updated count of too_many_parameters in the directory.
    :param file:
    :param count:
    :return:
    """
    pattern = '\(([^)]+)'
    lines = file.readlines()
    for line in lines:
        if 'def ' in line:
            parameters = re.search(pattern, line).group(1)
            parameters_list = parameters.split(',')
            if len(parameters_list) > Constants.MAX_PARAMETERS:
                count += 1
    return count
