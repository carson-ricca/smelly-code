import unittest
from pathlib import Path

from detect_code_smells import detect_code_smells

INPUT_PATH = Path('test_files')


class TestCodeSmellDetection(unittest.TestCase):
    def test_code_smell_detection(self):
        dataframe = detect_code_smells(INPUT_PATH)
        self.assertEqual(dataframe['God Lines'].sum(), 31)
        self.assertEqual(dataframe['Too Many Parameters'].sum(), 4)
        self.assertEqual(dataframe['Identifier Size'].sum(), 113)
        self.assertEqual(dataframe['Function Length'].sum(), 3)
        self.assertEqual(dataframe['Lazy Class'].sum(), 1)
        self.assertEqual(dataframe['Function Chains'].sum(), 1)
        self.assertEqual(dataframe['Large Class'].sum(), 1)
        self.assertEqual(dataframe['Data Class'].sum(), 2)
        self.assertEqual(dataframe['Middle Man'].sum(), 1)
        self.assertEqual(dataframe['Cyclomatic Complexity'].sum(), 1)


if __name__ == "__main__":
    unittest.main()
