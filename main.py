from pathlib import Path

from detect_code_smells import detect_code_smells

INPUT_PATH = Path('test_files')
OUTPUT_PATH = Path('output')

if __name__ == "__main__":
    detect_code_smells(INPUT_PATH, OUTPUT_PATH)
