import ast

from constants import Constants


def detect_identifier_size(file, count):
    """
    Determines if any of the identifiers are too long or too short.
    :param file: The file to evaluate.
    :param count: The pre-existing count of identifier_size in the directory.
    :return: The updated count of identifier_size in the directory.
    """
    ast_root = ast.parse(file.read())
    for node in ast.walk(ast_root):
        if isinstance(node, ast.FunctionDef):
            if _check_identifier_length(node.name) is True:
                count += 1
        if isinstance(node, ast.Name):
            if _check_identifier_length(node.id) is True:
                count += 1
        if isinstance(node, ast.ClassDef):
            if _check_identifier_length(node.name) is True:
                count += 1
    return count


def _check_identifier_length(identifier):
    """
    Determines if the identifier is too long or too short in comparison to a set constant.
    :param identifier: The identifier to check.
    :return: A boolean that describes whether the identifier is too long or too short.
    """
    if len(identifier) > Constants.MAX_IDENTIFIER_LENGTH or len(identifier) < Constants.MIN_IDENTIFIER_LENGTH:
        return True
    return False
