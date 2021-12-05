import os.path
import pandas as pd
from matplotlib import pyplot as plt
from pathlib import Path

from scripts import detect_god_line, detect_many_parameters, detect_identifier_size, detect_function_length, \
    detect_lazy_class, detect_function_chains, detect_large_class, detect_data_class, detect_middle_man, \
    detect_cyclomatic_complexity
from util import mkdir_if_not_exists


def detect_code_smells(input_path, output_path):
    """
    Function used to iterate and read over all python files within a specified directory. It detects the code smells
    at the same time.
    :param input_path: The directory to begin with.
    :param output_path: The directory to output the code smell csv to.
    :return: A dataframe with all the files and code smells formatted for exporting.
    """
    mkdir_if_not_exists(output_path)
    dataframe = pd.DataFrame(
        columns=['File Name', 'God Lines', 'Too Many Parameters', 'Identifier Size', 'Function Length', 'Lazy Class',
                 'Function Chains', 'Large Class', 'Data Class', 'Middle Man', 'Cyclomatic Complexity']
    )
    count = 0
    files = input_path.glob('**/*.py')
    for file in files:
        god_lines = 0
        too_many_parameters = 0
        identifier_size = 0
        function_length = 0
        lazy_class = 0
        large_class = 0
        function_chains = 0
        data_class = 0
        middle_man = 0
        cyclomatic_complexity = 0
        count += 1

        with open(Path(file), 'r') as f:
            file_name = os.path.basename(file)
            god_lines = detect_god_line(f, god_lines)
            f.seek(0)
            too_many_parameters = detect_many_parameters(f, too_many_parameters)
            f.seek(0)
            identifier_size = detect_identifier_size(f, identifier_size)
            f.seek(0)
            function_length = detect_function_length(f, function_length)
            f.seek(0)
            lazy_class = detect_lazy_class(f, lazy_class)
            f.seek(0)
            function_chains = detect_function_chains(f, function_chains)
            f.seek(0)
            large_class = detect_large_class(f, large_class)
            f.seek(0)
            data_class = detect_data_class(f, data_class)
            f.seek(0)
            middle_man = detect_middle_man(f, middle_man)
            f.seek(0)
            cyclomatic_complexity = detect_cyclomatic_complexity(f, cyclomatic_complexity)
            _print_output(count, god_lines, too_many_parameters, identifier_size, function_length, lazy_class,
                          function_chains, large_class, data_class, middle_man, cyclomatic_complexity, file_name)
            dataframe = _add_to_dataframe(god_lines, too_many_parameters, identifier_size, function_length, lazy_class,
                                          function_chains, large_class, data_class, middle_man, cyclomatic_complexity,
                                          file_name, dataframe)
    dataframe.to_csv(f'{output_path}/code_smells.csv', index=False)
    _plot_code_smells(dataframe)


def _plot_code_smells(dataframe):
    """
    Plots the data for all files.
    :param dataframe: The dataframe that contains all detected code smells.
    """
    total_code_smells = {
        'GL': dataframe['God Lines'].sum(),
        'TMP': dataframe['Too Many Parameters'].sum(),
        'IS': dataframe['Identifier Size'].sum(),
        'FL': dataframe['Function Length'].sum(),
        'LC': dataframe['Lazy Class'].sum(),
        'FC': dataframe['Function Chains'].sum(),
        'LGC': dataframe['Large Class'].sum(),
        'DC': dataframe['Data Class'].sum(),
        'MM': dataframe['Middle Man'].sum(),
        'CC': dataframe['Cyclomatic Complexity'].sum()
    }
    plt.bar(total_code_smells.keys(), total_code_smells.values())
    plt.ylabel('Count')
    plt.xlabel('Code Smells')
    plt.title('Number of Code Smells Detected')
    plt.show()


def _add_to_dataframe(god_lines, too_many_parameters, identifier_size, function_length, lazy_class, function_chains,
                      large_class, data_class, middle_man, cyclomatic_complexity, file_name, dataframe):
    """
    Adds the current file's code smells to the dataframe.
    :param god_lines: The number of god line smells.
    :param too_many_parameters: The number of too many parameter smells.
    :param identifier_size: THe number of identifier size smells.
    :param function_length: The number of function length smells.
    :param lazy_class: The number of lazy class smells.
    :param function_chains: The number of function chain smells.
    :param large_class: The number of large class smells.
    :param data_class: The number of data class smells.
    :param middle_man: The number of middle man smells.
    :param cyclomatic_complexity: The number of cyclomatic complexity smells.
    :param file_name: The current filename.
    :param dataframe: The dataframe with all existing entries.
    :return: The dataframe with the new row added.
    """
    dataframe.loc[dataframe.shape[0]] = [file_name, god_lines, too_many_parameters, identifier_size, function_length,
                                         lazy_class, function_chains, large_class, data_class, middle_man,
                                         cyclomatic_complexity]
    return dataframe


def _print_output(count, god_lines, too_many_parameters, identifier_size, function_length, lazy_class, function_chains,
                  large_class, data_class, middle_man, cyclomatic_complexity, file_name):
    """
    Prints the results for each file to the console.
    :param count: The current count of files that have been iterated over.
    :param god_lines: The number of god line smells.
    :param too_many_parameters: The number of too many parameter smells.
    :param identifier_size: THe number of identifier size smells.
    :param function_length: The number of function length smells.
    :param lazy_class: The number of lazy class smells.
    :param function_chains: The number of function chain smells.
    :param large_class: The number of large class smells.
    :param data_class: The number of data class smells.
    :param middle_man: The number of middle man smells.
    :param cyclomatic_complexity: The number of cyclomatic complexity smells.
    :param file_name: The current filename.
    """
    print('-' * 25)
    print(file_name)
    print(
        f'Count: {count}\nGod Lines: {god_lines}\nToo Many Parameters: {too_many_parameters}'
        f'\nIdentifier Size: {identifier_size}\nFunction Too Long: {function_length}\nLazy Class: {lazy_class}'
        f'\nFunction Chains: {function_chains}\nLarge Class: {large_class}\nData Class: {data_class}'
        f'\nMiddle Man: {middle_man}\nCyclomatic Complexity: {cyclomatic_complexity}')
    print('-' * 25)
