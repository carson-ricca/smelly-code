import ast


def detect_data_class(file, count):
    """
    :param file: The file to evaluate.
    :param count: The pre-existing count of data_class in the directory.
    :return: The updated count of data_class in the directory.
    """
    ast_root = ast.parse(file.read())
    for node in ast.walk(ast_root):
        if isinstance(node, ast.ClassDef):
            nodes = node.body
            if _determine_only_setters_and_getters(nodes):
                count += 1
    return count


def _determine_only_setters_and_getters(nodes):
    """
    A helper function used to determine if the class node is a data class or not.
    :param nodes: The nodes that are the children of the class node.
    :return: A boolean that describes if the class is a data class or not.
    """
    is_data_class = False
    for node in nodes:
        if _is_init_node(node) or _is_manual_setter_or_getter(node) or _is_property_setter_node(
                node) or _is_property_node(node) or _is_manual_assignment(node):
            is_data_class = True
        else:
            is_data_class = False
            break
    return is_data_class


def _is_init_node(node):
    """
    Determines if node is a class init node.
    :param node: The node to check.
    :return: A boolean.
    """
    if isinstance(node, ast.FunctionDef) and node.name == '__init__':
        return True
    return False


def _is_manual_setter_or_getter(node):
    """
    Checks if a node is of the manual setter and getter variety.
    :param node: The node to check.
    :return: A boolean.
    """
    if isinstance(node, ast.FunctionDef) and (node.name.startswith('get_') or node.name.startswith('set_')):
        return True
    return False


def _is_property_setter_node(node):
    """
    Determines if it has the property.setter decorator.
    :param node: The node to check.
    :return: A boolean.
    """
    if isinstance(node, ast.FunctionDef) and (
            len(node.decorator_list) != 0 and isinstance(node.decorator_list[0], ast.Attribute)):
        if node.decorator_list[0].attr == 'setter':
            return True
    return False


def _is_property_node(node):
    """
    Determines if it has the property decorator.
    :param node: The node to check.
    :return: A boolean.
    """
    if isinstance(node, ast.FunctionDef) and (
            len(node.decorator_list) != 0 and isinstance(node.decorator_list[0], ast.Name)):
        if node.decorator_list[0].id == 'property':
            return True
    return False


def _is_manual_assignment(node):
    """
    Determines if for manual setter and getters they were set up properly.
    :param node: The node to check.
    :return: A boolean.
    """
    if isinstance(node, ast.Assign) and node.value.func.id == 'property':
        return True
    return False
