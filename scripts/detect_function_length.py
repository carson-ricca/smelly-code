import ast

from constants import Constants


def detect_function_length(file, count):
    """
    :param file: The file to evaluate.
    :param count: The pre-existing count of function_length in the directory.
    :return: The updated count of function_length in the directory.
    """
    ast_root = ast.parse(file.read())
    for node in ast.walk(ast_root):
        if isinstance(node, ast.FunctionDef):
            if _compute_function_length(node) > Constants.MAX_FUNCTION_LENGTH:
                count += 1
    return count


def _compute_function_length(node):
    """
    A helper function for determining the line length given a node.
    :param node: The node to determine the line length for.
    :return: The number of lines in the function described by the node.
    """
    max_line_num = node.lineno
    min_line_num = node.lineno
    for node in ast.walk(node):
        if hasattr(node, 'lineno'):
            min_line_num = min(min_line_num, node.lineno)
            max_line_num = max(max_line_num, node.lineno)
    return max_line_num - min_line_num
