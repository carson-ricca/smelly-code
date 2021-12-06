from zipfile import ZipFile

from detect_code_smells import detect_code_smells
from export_dataframe import export_dataframe
from plot_dataframe import plot_dataframe

DATA_PATH = 'data/canvas-gamification-master.zip'
DECOMPRESSED_DATA_PATH = 'data'
INPUT_PATH = 'data/canvas-gamification-master'
OUTPUT_PATH = 'output'

if __name__ == "__main__":
    with ZipFile(DATA_PATH, 'r') as zipfile:
        zipfile.extractall(DECOMPRESSED_DATA_PATH)
    dataframe = detect_code_smells(INPUT_PATH)
    export_dataframe(dataframe, OUTPUT_PATH)
    plot_dataframe(dataframe)
