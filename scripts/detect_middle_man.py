import ast

from constants import Constants


def detect_middle_man(file, count):
    """
        :param file: The file to evaluate.
        :param count: The pre-existing count of middle_man in the directory.
        :return: The updated count of middle_man in the directory.
        """
    ast_root = ast.parse(file.read())
    for node in ast.walk(ast_root):
        if isinstance(node, ast.ClassDef):
            nodes = node.body
            if _determine_middle_man(nodes):
                count += 1
    return count


def _determine_middle_man(nodes):
    """
    A helper class to determine if the class is a middle man.
    :param nodes: The nodes that encompass the class to check.
    :return: A boolean, stating whether the class is a middle man or not.
    """
    total_num_of_functions = 0
    total_num_of_delegates = 0
    for node in nodes:
        num_items = 0
        if isinstance(node, ast.FunctionDef):
            total_num_of_functions += 1
            if node.name != '__init__':
                body_items = node.body
                for item in body_items:
                    if isinstance(item, ast.Expr) and isinstance(item.value, ast.Call):
                        num_items += 1
                if num_items == len(body_items):
                    total_num_of_delegates += 1
            else:
                total_num_of_functions -= 1
    if total_num_of_functions == 0:
        return False
    return (total_num_of_delegates / total_num_of_functions) >= Constants.MIDDLE_MAN_PERCENTAGE
