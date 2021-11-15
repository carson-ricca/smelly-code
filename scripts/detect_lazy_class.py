import ast

from constants import Constants
from util import compute_length


def detect_lazy_class(file, count):
    """
        :param file: The file to evaluate.
        :param count: The pre-existing count of lazy_class in the directory.
        :return: The updated count of lazy_class in the directory.
        """
    ast_root = ast.parse(file.read())
    for node in ast.walk(ast_root):
        if isinstance(node, ast.ClassDef):
            if compute_length(node) < Constants.MIN_CLASS_LENGTH:
                count += 1
    return count
