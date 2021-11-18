import ast


def detect_function_chains(file, count):
    """
        :param file: The file to evaluate.
        :param count: The pre-existing count of function_chains in the directory.
        :return: The updated count of function_chains in the directory.
        """
    ast_root = ast.parse(file.read())
    line_num = 0
    for node in ast.walk(ast_root):
        if isinstance(node, ast.Call):
            if hasattr(node.func, 'value'):
                if line_num != node.lineno:
                    line_num = node.lineno
                    count += 1
    return count
