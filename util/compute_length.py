import ast


def compute_length(node):
    """
    A helper function for determining the line length given a node.
    :param node: The node to determine the line length for.
    :return: The number of lines in the function/class described by the node.
    """
    max_line_num = node.lineno
    min_line_num = node.lineno
    for node in ast.walk(node):
        if hasattr(node, 'lineno'):
            min_line_num = min(min_line_num, node.lineno)
            max_line_num = max(max_line_num, node.lineno)
    return max_line_num - min_line_num
