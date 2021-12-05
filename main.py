from pathlib import Path

from detect_code_smells import detect_code_smells
from export_dataframe import export_dataframe
from plot_dataframe import plot_dataframe

INPUT_PATH = Path('test_files')
OUTPUT_PATH = Path('output')

if __name__ == "__main__":
    dataframe = detect_code_smells(INPUT_PATH)
    export_dataframe(dataframe, OUTPUT_PATH)
    plot_dataframe(dataframe)
