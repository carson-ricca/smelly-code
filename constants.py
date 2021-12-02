class Constants:
    # The length when a warning is thrown in PyCharm for a line being too long.
    MAX_LINE_LENGTH = 120

    # The number of acceptable parameters for a function.
    MAX_PARAMETERS = 3

    # The maximum allowed length of an identifier based on the PEP-8 standard.
    MAX_IDENTIFIER_LENGTH = 79

    # The minimum allowed length of an identifier.
    MIN_IDENTIFIER_LENGTH = 3

    # The maximum allowed number of lines for a function.
    MAX_FUNCTION_LENGTH = 30

    # An arbitrary number to indicate that a class is too short.
    MIN_CLASS_LENGTH = 10

    # An arbitrary number to indicate that a class is too long.
    MAX_CLASS_LENGTH = 100

    # The percentage of functions that delegate to other functions to be determined a middle man class.
    MIDDLE_MAN_PERCENTAGE = 0.5

    # The maximum cyclomatic complexity allowed for a class.
    MAX_CYCLOMATIC_COMPLEXITY = 20

    # A list describing what increase the cyclomatic complexity by 1.
    CYCLOMATIC_COMPLEXITY_FACTORS = ['if ', 'for ', 'while ', 'case ', 'except ', ' and ', ' or ', 'elif ', 'def ']
