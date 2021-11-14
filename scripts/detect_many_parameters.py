import ast

from constants import Constants


def detect_many_parameters(file, count):
    """
    Determines the number of functions that have too many parameters.
    :param file: The file to evaluate.
    :param count: The pre-existing count of too_many_parameters in the directory.
    :return: The updated count of too_many_parameters in the directory.
    """
    ast_root = ast.parse(file.read())
    for node in ast.walk(ast_root):
        if isinstance(node, ast.FunctionDef):
            if len(node.args.args) > Constants.MAX_PARAMETERS:
                count += 1
    return count
