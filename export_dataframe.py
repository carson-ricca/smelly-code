from util import mkdir_if_not_exists


def export_dataframe(dataframe, output_path):
    """
    Exports the dataframe to a csv file.
    :param dataframe: The dataframe.
    :param output_path: The path to output to.
    """
    mkdir_if_not_exists(output_path)
    dataframe.to_csv(f'{output_path}/code_smells.csv', index=False)
