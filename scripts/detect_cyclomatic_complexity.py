import ast, asttokens

from constants import Constants


def detect_cyclomatic_complexity(file, count):
    """
    A function that determines the cyclomatic_complexity of a class.
    :param file: The file to evaluate.
    :param count: The pre-existing count of cyclomatic_complexity in the directory.
    :return: The updated count of cyclomatic complexity in the directory.
    """
    complexity = 0
    ast_root = asttokens.ASTTokens(file.read(), parse=True)
    for node in ast.walk(ast_root.tree):
        if isinstance(node, ast.ClassDef):
            lines = [x.strip() for x in ast_root.get_text(node).split('\n')]
            for line in lines:
                if any(x in line for x in Constants.CYCLOMATIC_COMPLEXITY_FACTORS):
                    complexity += 1
    if complexity > Constants.MAX_CYCLOMATIC_COMPLEXITY:
        count += 1
    return count
