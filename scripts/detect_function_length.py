import ast

from constants import Constants
from util import compute_length


def detect_function_length(file, count):
    """
    :param file: The file to evaluate.
    :param count: The pre-existing count of function_length in the directory.
    :return: The updated count of function_length in the directory.
    """
    ast_root = ast.parse(file.read())
    for node in ast.walk(ast_root):
        if isinstance(node, ast.FunctionDef):
            if compute_length(node) > Constants.MAX_FUNCTION_LENGTH:
                count += 1
    return count
