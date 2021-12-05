from matplotlib import pyplot as plt


def plot_dataframe(dataframe):
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