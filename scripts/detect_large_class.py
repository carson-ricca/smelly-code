import ast

from constants import Constants
from util import compute_length


def detect_large_class(file, count):
    """
            :param file: The file to evaluate.
            :param count: The pre-existing count of large_class in the directory.
            :return: The updated count of large_class in the directory.
            """
    ast_root = ast.parse(file.read())
    for node in ast.walk(ast_root):
        if isinstance(node, ast.ClassDef):
            print(ast.dump(node))
            if compute_length(node) > Constants.MAX_CLASS_LENGTH:
                count += 1
    return count
