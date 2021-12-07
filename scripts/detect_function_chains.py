from constants import Constants

CHAINED_FUNCTION = ').'


def detect_function_chains(file, count):
    """
    :param file: The file to evaluate.
    :param count: The pre-existing count of function_chains in the directory.
    :return: The updated count of function_chains in the directory.
    """

    lines = file.readlines()
    for line in lines:
        if line.count(CHAINED_FUNCTION) > Constants.MAX_CHAINED_FUNCTIONS:
            count += 1
    return count
